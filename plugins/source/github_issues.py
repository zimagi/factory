from systems.plugins.index import BaseProvider


class Provider(BaseProvider("source", "github_issues")):

    def load_items(self, context):
        state_key = "github_issues"
        check_time = self.command.get_state(state_key, None)
        current_time = self.command.time.now_string

        for repository in self.command.facade("repository").all():
            if repository.provider_type == "github":
                params = {}
                if check_time:
                    params["since"] = self.command.time.to_datetime(check_time)

                for issue in repository.get_issues(**params):
                    if not issue.pull_request:
                        yield issue

        if not self.field_disable_save:
            self.command.set_state(state_key, current_time)

    def load_item(self, issue, context):
        users = self.add_github_users(issue.user, issue.assignee, *issue.assignees)
        return {
            "contributor": [
                self.get_github_user(info.id, info.model)
                for name, info in users.items()
            ],
            "issue": self.get_github_issue(issue),
        }
