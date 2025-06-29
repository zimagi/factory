from systems.commands.index import Command


class IssueComment(Command("dialog.issue_comment")):

    def exec(self):
        self.success("Posting issue comment")
        self.data("Issue ID", self.github_issue_id)
        self.data("Message", self.dialog_message)
        self.success("Ending command")
