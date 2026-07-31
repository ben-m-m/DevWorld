from flask import Blueprint, render_template, request, redirect, url_for
from services.github import GithubService
from services.analytics import AnalyticsService

# Define the GitHub blueprint used for user and dashboard routes.
github_bp = Blueprint('github', __name__, template_folder='templates')

github_service = GithubService()
analytics_service = AnalyticsService()

# Search form submits a username and redirects to the profile page.
@github_bp.route("/search", methods=["POST"])
def search():
    username = request.form.get("username")

    return redirect(url_for("github.profile", username=username))

# Render the user profile page using data from the GitHub API.
@github_bp.route("/profile/<username>")
def profile(username):
    user = github_service.get_user(username)

    if not user:
        return render_template("profile.html", user=None, error="User not found.")

    return render_template("profile.html", user=user)

# Build the dashboard page with repository analysis and chart-ready payloads.
@github_bp.route("/dashboard/<username>")
def dashboard(username):
    user = github_service.get_user(username)
    repos = github_service.get_repositories(username)
    analytics = analytics_service.analyze_repositories(repos)

    # Pass structured repository values to the template for chart rendering.
    chart_data = {
        "repository_names": [repo["name"] for repo in repos],
        "repository_stars": [repo["stargazers_count"] for repo in repos],
        "repository_forks": [repo["forks_count"] for repo in repos],
        "repository_sizes": [repo["size"] for repo in repos],
    }

    return render_template("dashboard.html", user=user, repos=repos, analytics=analytics, username=username)