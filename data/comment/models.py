from django.conf import settings
from systems.models.index import Model, ModelFacade


class CommentFacade(ModelFacade("comment")):
    pass


class Comment(Model("comment")):
    pass