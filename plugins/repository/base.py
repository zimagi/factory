import os
import pathlib
import yaml

from django.conf import settings
from systems.plugins.index import BasePlugin
from utility.filesystem import load_file, save_file


class BaseProvider(BasePlugin("repository")):

    def sdk(self):
        raise NotImplementedError(
            "Method sdk() must be implemented in repository providers"
        )

    def get_issues(self, **params):
        raise NotImplementedError(
            "Method get_issues(...) must be implemented in repository providers"
        )

    def get_issue(self, id):
        raise NotImplementedError(
            "Method get_issue(id) must be implemented in repository providers"
        )

    def get_pull_request(self, id):
        raise NotImplementedError(
            "Method get_pull_request(id) must be implemented in repository providers"
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

    def repository_path(self, instance, ensure=True):
        path = os.path.join(
            settings.MANAGER.dev_root,
            self.command.service_id,
            instance.organization.name,
            instance.name,
        )
        if ensure:
            pathlib.Path(path).mkdir(parents=True, exist_ok=True)
        return path

    def get_file_names(self, base_path, *extensions):
        files = []
        for filename in os.listdir(base_path):
            if extensions:
                for ext in extensions:
                    if filename.endswith(f".{ext}"):
                        files.append(filename)
            else:
                files.append(filename)
        return files

    def load_file(self, file_name, binary=False, instance=None):
        if not instance:
            instance = self.check_instance("repository load file")

        repository_path = self.repository_path(instance)
        path = os.path.join(repository_path, file_name)
        return load_file(path, binary)

    def load_yaml(self, file_name, instance=None):
        content = self.load_file(file_name, instance)
        if content:
            content = yaml.safe_load(content)
        return content if content else {}

    def save_file(self, file_name, content="", binary=False, instance=None):
        if not instance:
            instance = self.check_instance("repository save file")

        repository_path = self.repository_path(instance)
        path = os.path.join(repository_path, file_name)

        save_file(path, content, binary)
        return content

    def save_yaml(self, file_name, data=None):
        if not data:
            data = {}
        return self.save_file(file_name, yaml.dump(data))
