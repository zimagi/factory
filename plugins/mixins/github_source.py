from systems.plugins.index import ProviderMixin
from utility.data import Collection, get_identifier


class GithubSourceMixin(ProviderMixin("github_source")):

    provider_id = "github"

    def add_github_users(self, *users):
        if not getattr(self, "github_users", None):
            self.github_users = {}

        for user in users:
            if user:
                self.github_users[user.login] = Collection(
                    id=get_identifier([self.provider_id, user.login]),
                    model=user,
                )
        return self.github_users

    def get_github_user(self, id, model):
        return {
            "id": id,  # str
            "provider": self.provider_id,  # str
            "external_id": model.id,  # int
            "node_id": model.node_id,  # str
            "type": model.type,  # str
            "login": model.login,  # str
            "display_login": model.display_login,  # str
            "email": model.email,  # str email
            "notification_email": model.notification_email,  # str email
            "url": model.url,  # str url
            "html_url": model.html_url,  # str url
            "avatar_url": model.avatar_url,  # str url
            "name": model.name,  # str
            "bio": model.bio,  # str
            "blog": model.blog,  # str
            "location": model.location,  # str
            "company": model.company,  # str
            "contributions": model.contributions,  # int
            "collaborators": model.collaborators,  # int
            "followers": model.followers,  # int
            "following": model.following,  # int
            "hireable": model.hireable,  # bool
            "twitter_username": model.twitter_username,  # str
            "created_at": model.created_at,  # datetime
            "updated_at": model.updated_at,  # datetime
        }

    def get_github_organization(self, model):
        return {
            "provider": self.provider_id,  # str
            "external_id": model.id,  # int
            "advanced_security_enabled_for_new_repositories": model.advanced_security_enabled_for_new_repositories,  # bool
            "archived_at": model.archived_at,  # datetime
            "avatar_url": model.avatar_url,  # str url
            "billing_email": model.billing_email,  # str email
            "blog": model.blog,  # str url
            "collaborators": model.collaborators,  # int
            "company": model.company,  # str
            "created_at": model.created_at,  # datetime
            "default_repository_permission": model.default_repository_permission,  # str
            "dependabot_alerts_enabled_for_new_repositories": model.dependabot_alerts_enabled_for_new_repositories,  # bool
            "dependabot_security_updates_enabled_for_new_repositories": model.dependabot_security_updates_enabled_for_new_repositories,  # bool
            "dependency_graph_enabled_for_new_repositories": model.dependency_graph_enabled_for_new_repositories,  # bool
            "description": model.description,  # str
            "disk_usage": model.disk_usage,  # int
            "display_login": model.display_login,  # str
            "email": model.email,  # str email
            "events_url": model.events_url,  # str url
            "followers": model.followers,  # int
            "following": model.following,  # int
            "has_organization_projects": model.has_organization_projects,  # bool
            "has_repository_projects": model.has_repository_projects,  # bool
            "hooks_url": model.hooks_url,  # str url
            "html_url": model.html_url,  # str url
            "is_verified": model.is_verified,  # bool
            "issues_url": model.issues_url,  # str url
            "location": model.location,  # str
            "login": model.login,  # str
            "members_allowed_repository_creation_type": model.members_allowed_repository_creation_type,  # str
            "members_can_create_internal_repositories": model.members_can_create_internal_repositories,  # bool
            "members_can_create_pages": model.members_can_create_pages,  # bool
            "members_can_create_private_pages": model.members_can_create_private_pages,  # bool
            "members_can_create_private_repositories": model.members_can_create_private_repositories,  # bool
            "members_can_create_public_pages": model.members_can_create_public_pages,  # bool
            "members_can_create_public_repositories": model.members_can_create_public_repositories,  # bool
            "members_can_create_repositories": model.members_can_create_repositories,  # bool
            "members_can_fork_private_repositories": model.members_can_fork_private_repositories,  # bool
            "members_url": model.members_url,  # str url
            "name": model.name,  # str
            "node_id": model.node_id,  # str
            "owned_private_repos": model.owned_private_repos,  # int
            "private_gists": model.private_gists,  # int
            "public_gists": model.public_gists,  # int
            "public_members_url": model.public_members_url,  # str url
            "public_repos": model.public_repos,  # int
            "repos_url": model.repos_url,  # str url
            "secret_scanning_enabled_for_new_repositories": model.secret_scanning_enabled_for_new_repositories,  # bool
            "secret_scanning_push_protection_custom_link": model.secret_scanning_push_protection_custom_link,  # str
            "secret_scanning_push_protection_custom_link_enabled": model.secret_scanning_push_protection_custom_link_enabled,  # bool
            "secret_scanning_push_protection_enabled_for_new_repositories": model.secret_scanning_push_protection_enabled_for_new_repositories,  # bool
            "total_private_repos": model.total_private_repos,  # int
            "twitter_username": model.twitter_username,  # str
            "two_factor_requirement_enabled": model.two_factor_requirement_enabled,  # bool
            "type": model.type,  # str
            "updated_at": model.updated_at,  # datetime
            "url": model.url,  # str url
            "web_commit_signoff_required": model.web_commit_signoff_required,  # bool
        }

    def get_github_repository(self, model):
        return {
            "provider": self.provider_id,  # str
            "organization": model.organization.login,  # str
            "external_id": model.id,  # int
            "allow_auto_merge": model.allow_auto_merge,  # bool
            "allow_forking": model.allow_forking,  # bool
            "allow_merge_commit": model.allow_merge_commit,  # bool
            "allow_rebase_merge": model.allow_rebase_merge,  # bool
            "allow_squash_merge": model.allow_squash_merge,  # bool
            "allow_update_branch": model.allow_update_branch,  # bool
            "anonymous_access_enabled": model.anonymous_access_enabled,  # bool
            "archive_url": model.archive_url,  # str url
            "archived": model.archived,  # bool
            "assignees_url": model.assignees_url,  # str url
            "blobs_url": model.blobs_url,  # str url
            "branches_url": model.branches_url,  # str url
            "clone_url": model.clone_url,  # str url
            "collaborators_url": model.collaborators_url,  # str url
            "comments_url": model.comments_url,  # str url
            "commits_url": model.commits_url,  # str url
            "compare_url": model.compare_url,  # str url
            "contents_url": model.contents_url,  # str url
            "contributors_url": model.contributors_url,  # str url
            "created_at": model.created_at,  # datetime
            "default_branch": model.default_branch,  # str
            "delete_branch_on_merge": model.delete_branch_on_merge,  # bool
            "deployments_url": model.deployments_url,  # str url
            "description": model.description,  # str
            "disabled": model.disabled,  # bool
            "downloads_url": model.downloads_url,  # str url
            "events_url": model.events_url,  # str url
            "fork": model.fork,  # bool
            "forks": model.forks,  # int
            "forks_count": model.forks_count,  # int
            "forks_url": model.forks_url,  # str url
            "full_name": model.full_name,  # str
            "git_commits_url": model.git_commits_url,  # str url
            "git_refs_url": model.git_refs_url,  # str url
            "git_tags_url": model.git_tags_url,  # str url
            "git_url": model.git_url,  # str url
            "has_discussions": model.has_discussions,  # bool
            "has_downloads": model.has_downloads,  # bool
            "has_issues": model.has_issues,  # bool
            "has_pages": model.has_pages,  # bool
            "has_projects": model.has_projects,  # bool
            "has_wiki": model.has_wiki,  # bool
            "homepage": model.homepage,  # str url
            "hooks_url": model.hooks_url,  # str url
            "html_url": model.html_url,  # str url
            "is_template": model.is_template,  # bool
            "issue_comment_url": model.issue_comment_url,  # str url
            "issue_events_url": model.issue_events_url,  # str url
            "issues_url": model.issues_url,  # str url
            "keys_url": model.keys_url,  # str url
            "labels_url": model.labels_url,  # str url
            "language": model.language,  # str
            "languages_url": model.languages_url,  # str url
            "license": model.license.name if model.license else None,  # str
            "master_branch": model.master_branch,  # str
            "merge_commit_message": model.merge_commit_message,  # str
            "merge_commit_title": model.merge_commit_title,  # str
            "merges_url": model.merges_url,  # str url
            "milestones_url": model.milestones_url,  # str url
            "mirror_url": model.mirror_url,  # str url
            "name": model.name,  # str
            "network_count": model.network_count,  # int
            "node_id": model.node_id,  # str
            "notifications_url": model.notifications_url,  # str url
            "open_issues": model.open_issues,  # int
            "open_issues_count": model.open_issues_count,  # int
            "owner": self.github_users[model.owner.login].id,  # str
            "private": model.private,  # bool
            "pulls_url": model.pulls_url,  # str url
            "pushed_at": model.pushed_at,  # datetime
            "releases_url": model.releases_url,  # str url
            "role_name": model.role_name,  # str
            "size": model.size,  # int
            "squash_merge_commit_message": model.squash_merge_commit_message,  # str
            "squash_merge_commit_title": model.squash_merge_commit_title,  # str
            "ssh_url": model.ssh_url,  # str url
            "stargazers_count": model.stargazers_count,  # int
            "stargazers_url": model.stargazers_url,  # str url
            "starred_at": model.starred_at,  # str
            "statuses_url": model.statuses_url,  # str url
            "subscribers_count": model.subscribers_count,  # int
            "subscribers_url": model.subscribers_url,  # str url
            "subscription_url": model.subscription_url,  # str url
            "tags_url": model.tags_url,  # str url
            "teams_url": model.teams_url,  # str url
            "topics": model.topics,  # list<str>
            "trees_url": model.trees_url,  # str url
            "updated_at": model.updated_at,  # datetime
            "url": model.url,  # str url
            "use_squash_pr_title_as_default": model.use_squash_pr_title_as_default,  # bool
            "visibility": model.visibility,  # str
            "watchers": model.watchers,  # int
            "watchers_count": model.watchers_count,  # int
            "web_commit_signoff_required": model.web_commit_signoff_required,  # bool
        }

    def get_github_issue(self, model):
        return {
            "provider": self.provider_id,  # str
            "organization": model.repository.organization.login,  # str
            "repository": model.repository.name,  # str
            "external_id": model.id,  # int
            "type": (
                model.raw_data["type"]["name"] if "type" in model.raw_data else None
            ),  # str
            "title": model.title,  # str
            "assignee": (
                self.github_users[model.assignee.login].id if model.assignee else None
            ),  # str
            "assignees": [
                self.github_users[assignee.login].id for assignee in model.assignees
            ],  # list<str>
            "author_association": model.author_association,  # str
            "body": model.body,  # str
            "closed_at": model.closed_at,  # datetime
            "closed_by": model.closed_by,  # str
            "comments": model.comments,  # int
            "comments_url": model.comments_url,  # str url
            "created_at": model.created_at,  # datetime
            "draft": model.draft,  # bool
            "events_url": model.events_url,  # str url
            "html_url": model.html_url,  # str url
            "labels": [label.name for label in model.labels],  # list<str>
            "labels_url": model.labels_url,  # str url
            "locked": model.locked,  # bool
            "milestone": model.milestone.title if model.milestone else None,  # str
            "node_id": model.node_id,  # str
            "number": model.number,  # int
            "repository_url": model.repository_url,  # str url
            "state": model.state,  # str
            "state_reason": model.state_reason,  # str
            "timeline_url": model.timeline_url,  # str url
            "updated_at": model.updated_at,  # datetime
            "url": model.url,  # str url
            "user": self.github_users[model.user.login].id,  # str
        }

    def get_github_issue_comment(self, issue, model):
        return {
            "provider": self.provider_id,  # str
            "issue": issue.id,  # str
            "external_id": model.id,  # int
            "author_association": model.author_association,  # str
            "body": model.body,  # str
            "created_at": model.created_at,  # datetime
            "html_url": model.html_url,  # str url
            "issue_url": model.issue_url,  # str url
            "node_id": model.node_id,  # str
            "updated_at": model.updated_at,  # datetime
            "url": model.url,  # str url
            "user": self.github_users[model.user.login].id,  # str
        }

    def get_github_pull_request(self, model):
        return {
            **self.get_github_issue(model.as_issue()),
            "active_lock_reason": model.active_lock_reason,  # str
            "additions": model.additions,  # int
            "base": model.base.ref,  # str
            "changed_files": model.changed_files,  # int
            "commits": model.commits,  # int
            "commits_url": model.commits_url,  # str url
            "deletions": model.deletions,  # int
            "diff_url": model.diff_url,  # str url
            "head": model.head.ref,  # str
            "issue_url": model.issue_url,  # str url
            "maintainer_can_modify": model.maintainer_can_modify,  # bool
            "merge_commit_sha": model.merge_commit_sha,  # str
            "mergeable": model.mergeable,  # bool
            "mergeable_state": model.mergeable_state,  # str
            "merged": model.merged,  # bool
            "merged_at": model.merged_at,  # datetime
            "merged_by": (
                self.github_users[model.merged_by.login].id if model.merged_by else None
            ),  # str
            "patch_url": model.patch_url,  # str url
            "rebaseable": model.rebaseable,  # bool
            "requested_reviewers": [
                self.github_users[reviewer.login].id
                for reviewer in model.requested_reviewers
            ],  # list<str>
            "review_comment_url": model.review_comment_url,  # str url
            "review_comments": model.review_comments,  # int
            "review_comments_url": model.review_comments_url,  # str url
            "statuses_url": model.statuses_url,  # str url
        }

    def get_github_pull_request_comment(self, pull_request, model):
        return {
            **self.get_github_issue_comment(pull_request, model),
            "commit_id": model.commit_id,  # str
            "diff_hunk": model.diff_hunk,  # str
            "in_reply_to_id": model.in_reply_to_id,  # int
            "line": model.line,  # int
            "original_commit_id": model.original_commit_id,  # str
            "original_line": model.original_line,  # int
            "original_position": model.original_position,  # int
            "original_start_line": model.original_start_line,  # int
            "path": model.path,  # str
            "position": model.position,  # int
            "pull_request_review_id": model.pull_request_review_id,  # int
            "pull_request_url": model.pull_request_url,  # str url
            "side": model.side,  # str
            "start_line": model.start_line,  # int
            "start_side": model.start_side,  # str
            "subject_type": model.subject_type,  # str
        }
