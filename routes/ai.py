from flask import Blueprint, render_template
from services.github import GithubService
from services.ai import AIService

# Blueprint for AI analysis endpoints.
ai_bp = Blueprint("ai", __name__)

github = GithubService()
ai = AIService()

# Analyze a specific repository for a user and render the AI review page.
@ai_bp.route("/analyze/<username>/<repo_name>")
def analyze_repository(username, repo_name):
    repositories = github.get_repositories(username)

    # Locate the requested repository in the user's list.
    repository = next((repo for repo in repositories if repo["name"] == repo_name), None)

    if not repository:
        return "Repository not found", 404

    # Request the AI-generated engineering review for the repository.
    analysis = ai.analyze_repository(repository)

    return render_template("ai_analysis.html", repository=repository, analysis=analysis)
