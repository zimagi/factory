from django.conf import settings
from systems.models.index import Model, ModelFacade


class IssueFacade(ModelFacade("issue")):
    pass


class Issue(Model("issue")):
    pass