from django.conf import settings
from systems.plugins.index import BasePlugin


class BaseProvider(BasePlugin("organization")):

    def sdk(self):
        raise NotImplementedError(
            "Method sdk() must be implemented in organization providers"
        )

    def get_repositories(self, **params):
        raise NotImplementedError(
            "Method get_repositories(...) must be implemented in organization providers"
        )

    def initialize_instance(self, instance, created):
        # Override in subclasses if needed
        pass

    def prepare_instance(self, instance, created):
        # Override in subclasses if needed
        pass

    def finalize_instance(self, instance):
        # Override in subclasses if needed
        pass
