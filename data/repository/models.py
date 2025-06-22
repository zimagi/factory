from django.conf import settings
from systems.models.index import Model, ModelFacade


class RepositoryFacade(ModelFacade("repository")):
    pass


class Repository(Model("repository")):
    pass