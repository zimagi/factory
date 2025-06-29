from systems.commands.index import Command


class GenerateSpec(Command("project.generate_spec")):

    def exec(self):
        self.success("Generating architectural specification")
        self.data("Issue ID", self.github_issue_id)
        self.data("Message", self.llm_prompt)
