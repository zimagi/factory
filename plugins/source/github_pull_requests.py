from systems.plugins.index import BaseProvider


class Provider(BaseProvider("source", "github_pull_requests")):

    def load_items(self, context):
        state_key = "github_pull_requests"
        check_time = self.command.get_state(state_key, None)
        current_time = self.command.time.now_string

        for repository in self.command.facade("repository").all():
            if repository.provider_type == "github":
                params = {}
                if check_time:
                    params["since"] = self.command.time.to_datetime(check_time)

                for issue in repository.get_issues(**params):
                    if issue.pull_request:
                        yield repository.get_pull_request(issue.number)

        if not self.field_disable_save:
            self.command.set_state(state_key, current_time)

    def load_item(self, pull_request, context):
        users = self.add_github_users(
            pull_request.user,
            pull_request.merged_by,
            pull_request.assignee,
            *pull_request.assignees,
            *pull_request.requested_reviewers
        )
        return {
            "contributor": [
                self.get_github_user(info.id, info.model)
                for name, info in users.items()
            ],
            "pull_request": self.get_github_pull_request(pull_request),
        }
