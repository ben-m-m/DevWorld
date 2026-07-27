from flask import Blueprint, render_template, request, redirect, url_for
from services.github import GithubService

github_bp = Blueprint ('github', __name__, template_folder='templates')
github_service = GithubService()

#
@github_bp.route("/dashboard", methods=["GET", "POST"])
def repositories():
    repos = []
    if request.method == "POST":
        username = request.form.get("username")
        
        repos = github_service.get_repositories(username)
        print(f"Fetched {len(repos)} repositories for user {username}.")
    return render_template("dashboard.html", repos=repos)