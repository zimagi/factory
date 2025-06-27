from django.conf import settings
from github import Github

from systems.plugins.index import ProviderMixin


class GithubMixin(ProviderMixin("github")):

    @property
    def _github_token(self):
        token = settings.GITHUB_TOKEN
        if not token:
            self.command.error(
                f"To use GitHub {self.provider_type} provider ZIMAGI_GITHUB_TOKEN environment variable must be specified"
            )
        return token

    @property
    def github(self):
        if not getattr(self, "_github", None):
            self._github = Github(self._github_token)
        return self._github
