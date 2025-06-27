from django.conf import settings
from github import UnknownObjectException
from systems.plugins.index import BaseProvider
from utility.ssh import SSH


class Provider(BaseProvider("repository", "github")):

    def sdk(self):
        return self._repo_sdk

    def get_issues(self, **params):
        return self._repo_sdk.get_issues(**params)

    def get_issue(self, id):
        return self._repo_sdk.get_issue(id)

    def get_pull_request(self, id):
        return self._repo_sdk.get_pull(id)

    def initialize_instance(self, instance, created, retry=True):
        repository = self._get_repository(instance, True)

        if not instance.config.get("private_key", None) or not instance.config.get(
            "public_key", None
        ):
            private_key, public_key = SSH.create_ecdsa_keypair()
            instance.config["private_key"] = private_key
            instance.config["public_key"] = public_key

            deploy_key_title = f"@{self.github.get_user().login}:{settings.APP_NAME}"

            for deploy_key in repository.get_keys():
                if deploy_key.title == deploy_key_title:
                    deploy_key.delete()

            deploy_key = repository.create_key(deploy_key_title, public_key, False)
            instance.variables["deploy_key"] = deploy_key.id

    def finalize_instance(self, instance):
        repository = self._get_repository(instance)

        if repository and "deploy_key" in instance.variables:
            repository.get_key(instance.variables["deploy_key"]).delete()

    @property
    def _org_sdk(self):
        if not getattr(self, "_org_sdk_model", None):
            instance = self.check_instance("repository org sdk")
            try:
                self._org_sdk_model = self.github.get_organization(
                    instance.organization.name
                )
            except UnknownObjectException:
                self.command.error(
                    f"Organization {instance.organization.name} not found"
                )

        return self._org_sdk_model

    @property
    def _repo_sdk(self):
        if not getattr(self, "_repo_sdk_model", None):
            instance = self.check_instance("repository repo sdk")
            try:
                self._repo_sdk_model = self._org_sdk.get_repo(instance.name)
            except UnknownObjectException:
                self.command.error(
                    f"Repository {instance.name} not found in organization {instance.organization.name}"
                )

        return self._repo_sdk_model

    def _get_repository(self, instance, create=False):
        try:
            return self._org_sdk.get_repo(instance.name)
        except UnknownObjectException:
            if create:
                return self._org_sdk.create_repo(
                    instance.name,
                    description="",
                    private=True,
                    auto_init=False,
                    allow_rebase_merge=True,
                    allow_squash_merge=True,
                    allow_merge_commit=True,
                    delete_branch_on_merge=False,
                    has_issues=True,
                    has_projects=False,
                    has_downloads=False,
                    has_wiki=False,
                )
            return None
