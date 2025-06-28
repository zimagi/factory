from django.conf import settings
from systems.models.index import Model, ModelFacade


class PullRequestCommentFacade(ModelFacade("pull_request_comment")):
    pass


class PullRequestComment(Model("pull_request_comment")):
    pass