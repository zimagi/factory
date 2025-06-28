from systems.plugins.index import BaseProvider


class Provider(BaseProvider("source", "github_repositories")):

    def load_items(self, context):
        for repository in self.command.facade("repository").all():
            if repository.provider_type == "github":
                yield repository.sdk

    def load_item(self, repository, context):
        users = self.add_github_users(repository.owner)
        return {
            "contributor": [
                self.get_github_user(info.id, info.model)
                for name, info in users.items()
            ],
            "organization": self.get_github_organization(repository.organization),
            "repository": self.get_github_repository(repository),
        }
