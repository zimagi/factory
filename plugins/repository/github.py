from django.conf import settings
from github import Github, UnknownObjectException
from systems.plugins.index import BaseProvider
from utility.ssh import SSH


class Provider(BaseProvider("repository", "github")):
    @property
    def github_token(self):
        token = settings.GITHUB_TOKEN
        if not token:
            self.command.error(
                "To use GitHub module provider ZIMAGI_GITHUB_TOKEN environment variable must be specified"
            )
        return token

    @property
    def github(self):
        if not getattr(self, "_github", None):
            self._github = Github(self.github_token)
        return self._github

    def get_identifier(self, instance):
        return f"{instance.organization.name}/{instance.name}"

    def get_url(self, instance):
        return f"git@github.com:{self.get_identifier(instance)}.git"

    def initialize_instance(self, instance, created, retry=True):
        if not settings.GITHUB_TOKEN:
            self.command.error(
                "To use GitHub module provider ZIMAGI_GITHUB_TOKEN environment variable must be specified"
            )

        repository = self._get_repository(instance, True)

        instance.external_id = repository.id
        instance.description = repository.description
        instance.private = repository.private
        instance.url = repository.url
        instance.git_url = self.get_url(instance)
        instance.default_branch = repository.default_branch
        instance.topics = repository.topics

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
        if not settings.GITHUB_TOKEN:
            self.command.error(
                "To use GitHub module provider ZIMAGI_GITHUB_TOKEN environment variable must be specified"
            )

        repository = self._get_repository(instance)

        if repository and "deploy_key" in instance.variables:
            repository.get_key(instance.variables["deploy_key"]).delete()

    def _get_repository(self, instance, create=True):
        identifier = self.get_identifier(instance)
        try:
            return self.github.get_repo(identifier)
        except UnknownObjectException:
            if create:
                org_name, repo_name = identifier.split("/")
                org = self.github.get_organization(org_name)

                return org.create_repo(
                    repo_name,
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
