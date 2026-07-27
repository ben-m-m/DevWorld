from flask import Flask, render_template, request, redirect, url_for
from services.github import GithubService
from routes.github import github_bp

app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(github_bp)

github = GithubService()

@app.route('/')
def index():
    username = "ben-m-m"
    user = github.get_user(username)

    return render_template('index.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)