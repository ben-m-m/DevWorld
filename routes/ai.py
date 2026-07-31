from flask import Blueprint, render_template
from services.github import GithubService
from services.ai import AIService

ai_bp = Blueprint("ai", __name__)

github = GithubService()
ai = AIService()


@ai_bp.route("/analyze/<username>/<repo_name>")
def analyze_repository(username, repo_name):
    repositories = github.get_repositories(username)

    repository = next((repo for repo in repositories if repo["name"] == repo_name), None)

    if not repository:
        return "Repository not found", 404

    analysis = ai.analyze_repository(repository)

    return render_template("ai_analysis.html", repository=repository, analysis=analysis)
