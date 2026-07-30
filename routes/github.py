from flask import Blueprint, render_template, request, redirect, url_for
from services.github import GithubService
from services.analytics import AnalyticsService

github_bp = Blueprint ('github', __name__, template_folder='templates')
github_service = GithubService()
analytics_service = AnalyticsService()

#search route for username in github
@github_bp.route("/search", methods=["POST"])
def search():
    username = request.form.get("username")

    return redirect(url_for("github.profile", username=username))

    
@github_bp.route("/profile/<username>")
def profile(username):
    user = github_service.get_user(username)

    if not user:
        return render_template("profile.html", user=None, error="User not found.")
    
    return render_template("profile.html", user=user)

#
@github_bp.route("/dashboard/<username>")
def dashboard(username):
    user = github_service.get_user(username)
    repos = github_service.get_repositories(username)
    analytics = analytics_service.analyze_repositories(repos)

    chart_data = {
        "repository_names": [repo["name"] for repo in repos],
        "repository_stars": [repo["stargazers_count"] for repo in repos],
        "repository_forks": [repo["forks_count"] for repo in repos],
        "repository_sizes": [repo["size"] for repo in repos],
    }

    return render_template("dashboard.html", user=user, repos=repos, analytics=analytics, username=username)