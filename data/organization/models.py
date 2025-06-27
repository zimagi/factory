from django.conf import settings
from systems.models.index import Model, ModelFacade


class OrganizationFacade(ModelFacade("organization")):
    pass


class Organization(Model("organization")):

    @property
    def sdk(self):
        return self.provider.sdk()

    def get_repositories(self, **params):
        return self.provider.get_repositories(**params)
