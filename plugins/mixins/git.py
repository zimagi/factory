import pathlib

from django.conf import settings
from systems.plugins.index import ProviderMixin
from utility.filesystem import remove_dir


class GitMixin(ProviderMixin("git")):

    def get_remote(self, instance):
        return "origin"

    def get_url(self, instance):
        raise NotImplementedError(
            "Method get_remote must be implemented in repository providers that use the Git mixin"
        )

    def git_update(self, instance):
        repository_path = self.repository_path(instance)

        if not Git.check(repository_path):
            return (
                Git.clone(
                    self.get_url(instance),
                    repository_path,
                    reference=instance.default_branch,
                    **self._get_auth(instance),
                ),
                True,
            )
        return (self.pull(), False)

    def git_remove(self, instance):
        repository_path = self.repository_path(instance)
        remove_dir(pathlib.Path(repository_path))

    def _get_auth(self, instance):
        return {
            "public_key": instance.config.get("public_key", None),
            "private_key": instance.config.get("private_key", None),
        }

    def init(self, instance):
        return Git.init(
            self.repository_path(instance),
            reference=instance.default_branch,
            remote=self.get_remote(instance),
            remote_url=self.get_url(instance),
        )

    def pull(self, instance):
        repository = Git(
            self.repository_path(instance),
            user=self.command.active_user,
            **self._get_auth(instance),
        )
        repository.set_remote(self.get_remote(instance), self.get_url(instance))
        repository.pull(
            remote=self.get_remote(instance), branch=instance.default_branch
        )
        return repository

    def commit(self, instance, message, *files):
        repository = Git(
            self.repository_path(instance),
            user=self.command.active_user,
            **self._get_auth(instance),
        )
        repository.commit(message, *files)
        return repository

    def push(self, instance, branch=None):
        if branch is None:
            branch = instance.default_branch

        repository = Git(
            self.repository_path(instance),
            user=self.command.active_user,
            **self._get_auth(instance),
        )
        repository.set_remote(self.get_remote(instance), self.get_url(instance))
        repository.push(remote=self.get_remote(instance), branch=branch)
        return repository

    def check_dirty(self, instance):
        repository = Git(self.repository_path(instance))
        if repository.check_dirty():
            return True
        return False
