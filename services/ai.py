import os
#import google.generativeai as genai
#import google.api_core.exceptions as exceptions
import markdown
from config import Config
import requests



class AIService:
    def analyze_repository(self, repo):
        prompt = f"""
You are a Senior Software Engineer and Recruiter.
Produce an engineering design Review for this Github repository.

Evaluate:

- Codebase maturity
- Project architecture
- Maintainability
- Scalability
- Testability
- Documentation quality
- Security concerns
- Performance concerns
- Hiring readiness
- Business potential

Give scores out of 10.

Finish with:

Overall Engineering Grade:
A+
A
B
C
D

Keep the report professional.

Repository:
{repo["name"]}

Description:
{repo["description"]}

Language:
{repo["language"]}

Stars:
{repo["stargazers_count"]}

Forks:
{repo["forks_count"]}

Watchers:
{repo["watchers_count"]}

Open Issues:
{repo["open_issues_count"]}

Repository Size:
{repo["size"]} KB

Archived:
{repo["archived"]}

Updated:
{repo["updated_at"]}

Write a professional engineering report.

Use these headings:
# Executive Summary
# Architecture
# Strengths
# Weaknesses
# Security Concerns
# Maintainability
# Scalability
# Documentation quality
# Recommendations
# Engineering Score

Return markdown.
"""
        try:
            url = (
                "https://generativelanguage.googleapis.com/"
                "v1beta/models/gemini-3.5-flash:generateContent"
            )

            headers = {
                "Content-Type": "application/json"
            }

            payload = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ]
            }

            response = requests.post(
                url,
                headers=headers,
                params={
                    "key": Config.GEMINI_API_KEY
                },
                json=payload,
                timeout=60
            )

            response.raise_for_status()

            data = response.json()

            text = (
                data["candidates"][0]
                ["content"]
                ["parts"][0]
                ["text"]
            )

            return markdown.markdown(text)

        except Exception as e:

            return f"""
# AI Analysis Temporarily Unavailable

Reason: {e}

Please try again later.
"""
    