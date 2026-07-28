from flask import Flask, render_template, request, redirect, url_for
from services.github import GithubService
from routes.github import github_bp

#initialize Flask app
app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(github_bp)

github = GithubService()

#index route
@app.route('/')
def home():
    #username = "ben-m-m" # Replace with actual username or get from request
    #user = github.get_user(username)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)