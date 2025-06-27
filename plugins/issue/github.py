from github import UnknownObjectException
from systems.plugins.index import BaseProvider


class Provider(BaseProvider("issue", "github")):

    def sdk(self):
        return self._issue_sdk

    def get_comments(self, **params):
        return self._issue_sdk.get_comments(**params)

    @property
    def _issue_sdk(self):
        if not getattr(self, "_issue_sdk_model", None):
            instance = self.check_instance("issue issue sdk")
            try:
                self._issue_sdk_model = instance.repository.get_issue(instance.number)
            except UnknownObjectException:
                self.command.error(
                    f"Issue {instance.number} not found in repository {instance.repository.name}"
                )
        return self._issue_sdk_model
