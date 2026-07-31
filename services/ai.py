import os
import google.generativeai as genai
import markdown


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.5-flash")

class AIService:
    def analyze_repository(self, repo):
        prompt = f"""
You are a Senior Software Engineer and Recruiter.
Review this Github repository.

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

# Maintainability

# Scalability

# Documentation

# Recommendations

# Engineering Score

Return markdown.
"""
        response = model.generate_content(prompt)
        return markdown.markdown(response.text)
    