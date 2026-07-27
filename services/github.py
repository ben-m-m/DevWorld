import requests

class GithubService:

    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.session = requests.Session()

        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json"})

    def get_user(self, username):
        """Fetches user information from GitHub API."""
        url = f"{self.BASE_URL}/users/{username}"

        response = self.session.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    

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
