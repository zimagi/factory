from django.conf import settings
from systems.models.index import Model, ModelFacade


class OrganizationFacade(ModelFacade("organization")):
    pass


class Organization(Model("organization")):
    pass