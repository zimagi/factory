from systems.commands import profile


class ProfileComponent(profile.BaseProfileComponent):
    def priority(self):
        return 50

    def run(self, name, config):
        provider = self.pop_value("provider", config)
        repositories = self.pop_info("repositories", config)

        if not provider:
            provider = "github"

        self.exec(
            "organization save",
            organization_key=name,
            organization_fields=config,
            organization_provider_name=provider,
            local=self.command.local,
        )

        def process_repository(repository):
            self.exec(
                "repository save",
                organization_key=name,
                repository_key=repository,
                repository_provider_name=provider,
                local=self.command.local,
            )

        if repositories and self.profile.include_inner("repository"):
            self.run_list(repositories, process_repository)

    def destroy(self, name, config):
        self.exec(
            "organization remove",
            organization_key=name,
            force=True,
            local=self.command.local,
        )
