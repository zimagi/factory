from django.conf import settings

from settings.config import Config

#
# Interface path
#
# Usage: directory = settings.MANAGER.dev_root
#
settings.PROJECT_PATH_MAP["dev_root"] = {
    "directory": "dev",
    "backup": False,
}
