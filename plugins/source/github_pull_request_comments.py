from systems.plugins.index import BaseProvider
from utility.data import Collection


class Provider(BaseProvider("source", "github_pull_request_comments")):

    def load_items(self, context):
        facade = self.command.facade("pull_request")
        state_key = "github_pull_request_comments"
        check_time = self.command.get_state(state_key, None)
        current_time = self.command.time.now_string

        for pull_request in facade.filter(provider_type="github", state="open"):
            params = {}
            if check_time:
                params["since"] = self.command.time.to_datetime(check_time)

            for comment in pull_request.get_comments(**params):
                yield {"pull_request": pull_request, "comment": comment}

        if not self.field_disable_save:
            self.command.set_state(state_key, current_time)

    def load_item(self, models, context):
        users = self.add_github_users(models["pull_request"].user)
        return {
            "contributor": [
                self.get_github_user(info.id, info.model)
                for name, info in users.items()
            ],
            "pull_request_comment": self.get_github_pull_request_comment(
                models["pull_request"], models["comment"]
            ),
        }
