from collections import Counter

"""
Analytics service for processing and analyzing GitHub repos data.
"""

class AnalyticsService:
    @staticmethod
    def analyze_repositories(repos):
        """
        Analyzes the given list of repositories and returns a summary.
        
        Args:
            repos (list): List of repository dictionaries.
            """
        if not repos:
            return {
                "total_repositories": 0,
                "total_stars": 0,
                "total_forks": 0,
                "total_open_issues": 0,
                "most_common_language": "N/A",
                "largest_repo": "N/A",
                "active_repo": 0
            }

        total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)
        total_forks = sum(repo.get("forks_count", 0) for repo in repos)
        total_open_issues = sum(repo.get("open_issues_count", 0) for repo in repos)

        #most common language used
        languages = [repo.get("language") for repo in repos if repo.get("language")]

        language_counter = Counter(languages)
        most_common_language = language_counter.most_common(1)[0][0] if language_counter else "N/A"

        #largest repo by size
        largest_repo = max(repos, key=lambda repo: repo.get("size", 0), default=None)
        largest_repo_name = largest_repo.get("name") if largest_repo else "N/A"

        #active repo by recent updates
        active_repositories = sum(1 for repo in repos if repo.get("archived"))
        active_repo_name = active_repositories.get("name") if active_repositories else "N/A"

        most_starred = max(repos, key=lambda repo: repo.get("stargazers_count", 0), default=None)
        most_starred_name = most_starred.get("name") if most_starred else "N/A"

        largest_size_repo = max(repo.get("size", 0) for repo in repos)
        largest_size_repo_name = next((repo.get("name") for repo in repos if repo.get("size", 0) == largest_size_repo), "N/A")  

        oldest_repo = min(repos, key=lambda repo: repo.get("created_at", ""), default=None)
        oldest_repo_name = oldest_repo.get("name") if oldest_repo else "N/A"

        return {
            "total_repositories": len(repos),
            "total_stars": total_stars,
            "total_forks": total_forks,
            "total_open_issues": total_open_issues,
            "most_used_language": most_common_language,
            "largest_repository": largest_repo_name,
            "active_repositories": active_repositories,
            "most_starred_repo": most_starred_name,
            "oldest_repo": oldest_repo_name,
            "largest_size_repo": largest_size_repo_name
        }
