from flask import Blueprint, render_template, request, redirect, url_for
from services.github import GithubService
from services.analytics import AnalyticsService

github_bp = Blueprint ('github', __name__, template_folder='templates')
github_service = GithubService()
analytics_service = AnalyticsService()

#
@github_bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    repos = []
    analytics = {}

    if request.method == "POST":
        username = request.form.get("username")
        
        repos = github_service.get_repositories(username)
        analytics = analytics_service.analyze_repositories(repos)
        print(analytics)
        print(f"Fetched {len(repos)} repositories for user {username}.")
    return render_template("dashboard.html", repos=repos, analytics=analytics)