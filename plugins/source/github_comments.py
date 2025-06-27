from systems.plugins.index import BaseProvider
from utility.data import Collection


class Provider(BaseProvider("source", "github_comments")):

    def load_items(self, context):
        facade = self.command.facade("issue")
        state_key = "github_issue_comments"
        check_time = self.command.get_state(state_key, None)
        current_time = self.command.time.now_string

        for issue in facade.filter(provider_type="github", state="open"):
            params = {}
            if check_time:
                params["since"] = self.command.time.to_datetime(check_time)

            for comment in issue.get_comments(**params):
                yield Collection(issue=issue, comment=comment)

        if not self.field_disable_save:
            self.command.set_state(state_key, current_time)

    def load_item(self, models, context):
        users = self.add_github_users(issue.user, issue.assignee, *issue.assignees)
        return {
            "contributor": [
                self.get_github_user(info.id, info.model)
                for name, info in users.items()
            ],
            "comment": self.get_github_issue_comment(models.issue, models.comment),
        }
