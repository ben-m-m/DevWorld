import os
import google.genai as genai
from google.genai.errors import APIError
import markdown
from config import Config


client = genai.Client( api_key=Config.GEMINI_API_KEY )

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
            response = client.models.generate_content(model="gemini-3.5-flash", contents=prompt)
            return markdown.markdown(response.text)
        except APIError as e:
            return f"""
# AI Analysis Temporarily Unavailable

Reason: {e}

Please try again in a few moments.
"""
    