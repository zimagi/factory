from django.conf import settings
from systems.models.index import Model, ModelFacade


class RepositoryFacade(ModelFacade("repository")):
    pass


class Repository(Model("repository")):

    @property
    def sdk(self):
        return self.provider.sdk()

    def get_issues(self, **params):
        return self.provider.get_issues(**params)

    def get_issue(self, id):
        return self.provider.get_issue(id)

    def get_pull_request(self, id):
        return self.provider.get_pull_request(id)
