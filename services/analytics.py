from collections import Counter

"""
Analytics service for processing and analyzing GitHub repository data.
"""

class AnalyticsService:
    
    def analyze_repositories(self, repos):
        """
        Orchestrates all repository analysis logic and returns a summary dictionary.
        """
        if not repos:
            return {
                "total_repositories": 0,
                "total_stars": 0,
                "total_forks": 0,
                "total_open_issues": 0,
                "most_common_language": "N/A",
                "language_breakdown": {},
                "largest_repo": "N/A",
                "largest_size": 0,
                "most_starred_repo": "N/A",
                "highest_star_count": 0,
                "oldest_repository": "N/A",
                "active_repo": 0,
            }

        # Aggregate the basic counts across all repositories.
        total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)
        total_forks = sum(repo.get("forks_count", 0) for repo in repos)
        total_open_issues = sum(repo.get("open_issues_count", 0) for repo in repos)

        summary = {
            "total_repositories": len(repos),
            "total_stars": total_stars,
            "total_forks": total_forks,
            "total_open_issues": total_open_issues
        }

        # Merge specialized analytics into the final summary payload.
        summary.update(self.language_statistics(repos))
        summary.update(self.repository_ranking(repos))
        summary.update(self.activity_statistics(repos))

        return summary

    def language_statistics(self, repos):
        # Count programming languages used across the supplied repositories.
        languages = [repo.get("language") for repo in repos if repo.get("language")]
        language_counter = Counter(languages)

        return {
            "most_common_language": language_counter.most_common(1)[0][0] if language_counter else "N/A",
            "language_breakdown": dict(language_counter)
        }

    def repository_ranking(self, repos):
        # Identify top-ranked repositories by size, popularity, and age.
        if not repos:
            return {}

        largest_repo = max(repos, key=lambda repo: repo.get("size", 0), default=None)
        most_starred = max(repos, key=lambda repo: repo.get("stargazers_count", 0), default=None)
        largest_size_repo = max(repo.get("size", 0) for repo in repos)
        oldest_repo = min(repos, key=lambda repo: repo.get("created_at", ""), default=None)

        return {
            "largest_repository": largest_repo["name"] if largest_repo else "N/A",
            "most_starred": most_starred["name"] if most_starred else "N/A",
            "largest_size": largest_size_repo,
            "oldest_repo": oldest_repo["name"] if oldest_repo else "N/A",
            "highest_star_count": most_starred.get("stargazers_count", 0)
        }

    def activity_statistics(self, repos):
        # Count active and archived repositories to show maintenance posture.
        active_repositories = sum(1 for repo in repos if not repo.get("archived", False))
        archived_repositories = sum(1 for repo in repos if repo.get("archived", False))

        return {
            "active_repositories": active_repositories,
            "archived_repositories": archived_repositories
        }