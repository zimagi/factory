from systems.commands.index import Command


class PullRequestComment(Command("dialog.pull_request_comment")):

    def exec(self):
        self.success("Posting pull request comment")
        self.data("Issue ID", self.github_issue_id)
        self.data("Message", self.dialog_message)
