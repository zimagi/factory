from django.conf import settings
from systems.models.index import Model, ModelFacade


class ContributorFacade(ModelFacade("contributor")):
    pass


class Contributor(Model("contributor")):
    pass