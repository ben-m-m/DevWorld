import requests

# Service wrapper for all GitHub REST API interactions.
class GithubService:

    # GitHub API base endpoint.
    BASE_URL = "https://api.github.com"

    # Initialize a reusable requests session with the GitHub API header.
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json"})

    # Fetch a single GitHub user's profile metadata.
    def get_user(self, username):
        """Fetches user information from GitHub API."""
        url = f"{self.BASE_URL}/users/{username}"

        response = self.session.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    

    # Fetch all public repositories for a given GitHub username.
    def get_repositories(self, username):
        """Fetches user's repositories from GitHub API."""
        url = f"{self.BASE_URL}/users/{username}/repos"

        params = {
            "sort": "updated",
            "per_page": 100
        }

        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching repositories for user {username}: {e}")
            return []
