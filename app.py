from flask import Flask, render_template, request, redirect, url_for
from services.github import GithubService
from routes.github import github_bp
from routes.ai import ai_bp

# Create the Flask application instance.
app = Flask(__name__)

# Load application settings from the configuration class.
app.config.from_object('config.Config')

# Register the feature blueprints for GitHub and AI routes.
app.register_blueprint(github_bp)
app.register_blueprint(ai_bp)

# Initialize the GitHub service so the app can fetch profile and repo data.
github = GithubService()

# Home page route: renders the landing page.
@app.route('/')
def home():
    

    return render_template('index.html')


# Run the Flask development server when this file is executed directly.
if __name__ == '__main__':
    app.run(debug=True)