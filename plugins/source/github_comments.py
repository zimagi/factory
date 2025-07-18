from systems.plugins.index import BaseProvider
from utility.data import Collection


class Provider(BaseProvider("source", "github_comments")):

    def load_items(self, context):
        state_key = "github_issue_comments"
        check_time = self.command.get_state(state_key, None)
        current_time = self.command.time.now_string

        for issue in self.command.facade("issue").filter(
            provider_type="github", state="open", pullrequest__isnull=True
        ):
            params = {}
            if check_time:
                params["since"] = self.command.time.to_datetime(check_time)

            for comment in issue.get_comments(**params):
                yield {"issue": issue, "comment": comment}

        if not self.field_disable_save:
            self.command.set_state(state_key, current_time)

    def load_item(self, models, context):
        users = self.add_github_users(models["comment"].user)
        return {
            "contributor": [
                self.get_github_user(info.id, info.model)
                for name, info in users.items()
            ],
            "comment": self.get_github_issue_comment(
                models["issue"], models["comment"]
            ),
        }
