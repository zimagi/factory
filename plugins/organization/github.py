from django.conf import settings
from github import UnknownObjectException
from systems.plugins.index import BaseProvider


class Provider(BaseProvider("organization", "github")):

    def sdk(self):
        return self._org_sdk

    def get_repositories(self, **params):
        return self._org_sdk.get_repos(**params)

    @property
    def _org_sdk(self):
        if not getattr(self, "_org_sdk_model", None):
            instance = self.check_instance("organization org sdk")
            try:
                self._org_sdk_model = self.github.get_organization(instance.name)
            except UnknownObjectException:
                self.command.error(f"Organization {instance.name} not found")

        return self._org_sdk_model
