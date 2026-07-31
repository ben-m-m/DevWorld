import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    # Flask
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "default_secret_key"
    )

    FLASK_ENV = os.getenv(
        "FLASK_ENV",
        "development"
    )

    # GitHub API / OAuth
    GITHUB_CLIENT_ID = os.getenv(
        "GITHUB_CLIENT_ID"
    )

    GITHUB_CLIENT_SECRET = os.getenv(
        "GITHUB_CLIENT_SECRET"
    )

    # Groq AI
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # Cache
    CACHE_TIMEOUT = int(
        os.getenv(
            "CACHE_TIMEOUT",
            300
        )
    )
