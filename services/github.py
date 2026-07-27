import requests

class GithubService:

    BASE_URL = "https://api.github.com"

    def get_user(self, username):
        """Fetches user information from GitHub API."""
        url = f"{self.BASE_URL}/users/{username}"

        response = requests.get(url, headers={"Accept": "application/vnd.github.v3+json"}, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return None