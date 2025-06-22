from django.conf import settings
from systems.models.index import Model, ModelFacade


class PullRequestFacade(ModelFacade("pull_request")):
    pass


class PullRequest(Model("pull_request")):
    pass