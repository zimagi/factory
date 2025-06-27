from django.conf import settings
from systems.models.index import Model, ModelFacade


class IssueFacade(ModelFacade("issue")):
    pass


class Issue(Model("issue")):

    @property
    def sdk(self):
        return self.provider.sdk()

    def get_comments(self, **params):
        return self.provider.get_comments(**params)
