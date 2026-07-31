import os
from dotenv import load_dotenv

# Load environment variables from the local .env file when available.
load_dotenv()

class Config:

    # Flask application security configuration.
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "default_secret_key"
    )

    FLASK_ENV = os.getenv(
        "FLASK_ENV",
        "development"
    )

    # GitHub API / OAuth credentials for app-based integrations.
    GITHUB_CLIENT_ID = os.getenv(
        "GITHUB_CLIENT_ID"
    )

    GITHUB_CLIENT_SECRET = os.getenv(
        "GITHUB_CLIENT_SECRET"
    )

    # Groq AI service key used for repository analysis.
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # Cache duration for commonly fetched data in seconds.
    CACHE_TIMEOUT = int(
        os.getenv(
            "CACHE_TIMEOUT",
            300
        )
    )
