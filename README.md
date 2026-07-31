# DevWorld – AI-Powered GitHub Engineering Analytics Platform

## Overview

DevWorld is an AI-powered GitHub engineering analytics platform that transforms public GitHub profiles into interactive software engineering dashboards.

Unlike traditional GitHub profile viewers that only display repository statistics, DevWorld analyzes developer activity, visualizes engineering metrics, and generates AI-powered engineering reviews for individual repositories.

The platform helps developers answer:

- What have I built?
- Which technologies define my work?
- How healthy are my repositories?
- Which projects demonstrate engineering maturity?
- How can I improve my engineering portfolio?

DevWorld combines the GitHub REST API, Groq AI API, and interactive data visualization to provide meaningful engineering insights.

This project was developed as part of the African Leadership University (ALU) **Playing Around With APIs** summative assessment.

---

## Problem Statement

GitHub provides valuable repository information but does not directly help developers understand:

- The quality and maturity of their projects
- Repository maintainability
- Engineering strengths and weaknesses
- Technology trends across their work
- Portfolio readiness for recruiters

Developers often have many repositories but lack a structured way to evaluate their growth and engineering impact.

DevWorld bridges this gap by combining GitHub data analysis, interactive dashboards, and AI-generated engineering reviews into a single platform.

---

## Features

## GitHub User Search

Users can search any public GitHub username.

DevWorld retrieves:

- Profile information
- Repository information
- Followers
- Following
- Public repositories
- Bio
- Company
- Website
- Account creation date

Data is collected using the GitHub REST API.

---

## Engineering Analytics Dashboard

Each GitHub profile generates an engineering analytics dashboard containing:

- Total repositories
- Total stars
- Total forks
- Primary programming language
- Largest repository
- Most starred repository
- Most active repositories
- Language distribution

Analytics are calculated dynamically from GitHub repository data.

---

## Repository Explorer

Repositories can be explored using interactive controls:

## Search

Search repositories by name.

## Filtering

Filter repositories by programming language.

## Sorting

Supported sorting options:

- Recently updated
- Least recently updated
- Recently created
- Oldest created
- Alphabetical A–Z
- Alphabetical Z–A
- Highest stars
- Lowest stars
- Highest forks
- Lowest forks
- Largest repository size
- Smallest repository size

Whenever filtering or sorting changes, the repository data and visualizations update dynamically.

---

## Interactive Data Visualization

DevWorld presents repository analytics using interactive charts powered by Chart.js.

Visualizations include:

- Programming language distribution
- Repository stars
- Repository forks
- Repository sizes

Selecting repositories updates dashboard analytics dynamically.

---

## Repository Engineering Intelligence

Each repository includes an engineering intelligence analysis panel.

The panel displays:

## Repository Information

- Description
- Programming language
- Stars
- Forks
- Repository size
- Creation date
- Last update date

## Engineering Metrics

### Maintenance Score

Calculated using:

- Repository archived status
- Open issues
- Repository activity

### Popularity Score

Calculated using:

- GitHub stars

### Activity Score

Calculated using:

- Repository update frequency

### Overall Engineering Health

Combines multiple engineering indicators into a final repository health assessment:

- Excellent
- Good
- Average
- Needs More Attention

---

## AI Engineering Review

One of DevWorld's main features is AI-powered repository analysis using the **Groq API**.

Each repository provides an:

**Analyze Repository With AI**

feature.

The system:

1. Collects repository metadata.
2. Builds an engineering review prompt.
3. Sends repository information to Groq AI.
4. Generates a professional engineering assessment.
5. Displays the report in a dedicated analysis page.

The AI evaluates:

- Executive Summary
- Software Architecture
- Project Strengths
- Weaknesses
- Security Concerns
- Maintainability
- Scalability
- Documentation Quality
- Engineering Recommendations
- Overall Engineering Score

The AI review simulates feedback from a senior software engineer and technical recruiter.

---

## Error Handling

DevWorld includes error handling for:

- Invalid GitHub usernames
- GitHub API failures
- AI API downtime
- Invalid API responses
- Network failures

If AI analysis is unavailable, repository analytics remain accessible.

---

## Technologies Used

## Backend

- Python
- Flask
- Gunicorn

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- Vanilla JavaScript

## APIs

### GitHub REST API

Used for:

- User profiles
- Repository data
- Repository statistics
- Languages
- Metadata

### Groq API

Used for:

- AI-powered repository engineering reviews
- Technical analysis generation

## Visualization

- Chart.js

---

## Deployment Architecture

DevWorld is deployed using a production web stack:

- Ubuntu Linux
- Nginx
- Gunicorn
- HAProxy
- Let's Encrypt SSL
- Systemd services

Architecture:

```
                 Internet
                     |
                     |
                HAProxy
                 lb-01
                     |
        ┌────────────┴────────────┐
        |                         |
        ▼                         ▼
     web-01                    web-02
        |                         |
     Nginx                     Nginx
        |                         |
   Gunicorn                 Gunicorn
        |                         |
      Flask                   Flask
        |
        |
 GitHub API + Groq API
```

The deployment provides:

- Load balancing
- High availability
- SSL termination
- Fault tolerance
- Horizontal scalability

---

## Project Structure

```
DevWorld/
│
├── app.py
├── config.py
├── requirements.txt
│
├── routes/
│   ├── github.py
│   └── ai.py
│
├── services/
│   ├── analytics.py
│   ├── github.py
│   └── ai.py
│
├── static/
│   ├── css/
│   │    └── style.css
│   │
│   └── js/
│        ├── charts.js
│        ├── filters.js
│        ├── intelligence.js
│        └── repository.js
│
└── templates/
    ├── base.html
    ├── dashboard.html
    ├── profile.html
    ├── ai_analysis.html
    └── index.html
```

---

## Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/DevWorld.git

cd DevWorld
```

---

## Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate:

Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your_secret_key

GITHUB_TOKEN=your_github_token

GROQ_API_KEY=your_groq_api_key

GITHUB_CLIENT_ID=optional

GITHUB_CLIENT_SECRET=optional

FLASK_ENV=development
```

Never commit `.env` files to GitHub.

---

## Running the Application

## Development

```bash
python app.py
```

Application:

```
http://localhost:5000
```

---

## Production

Run using Gunicorn:

```bash
gunicorn app:app
```

---

## API Attribution

## GitHub REST API

GitHub provides repository and user information.

Documentation:

https://docs.github.com/en/rest


## Groq API

Groq provides AI inference capabilities used for repository engineering analysis.

Documentation:

https://console.groq.com/docs


---

## Future Improvements

Future enhancements include:

- GitHub OAuth authentication
- Repository comparison
- Commit history analytics
- Pull request analysis
- Contributor analytics
- Code quality scoring
- Export AI reports as PDF
- AI repository chat assistant
- Historical developer growth tracking
- Personalized engineering recommendations

---

## Live Demo

Production URL:

```
https://www.mainaben.tech
```

---

## Demo Video

Project walkthrough:

```
https://youtu.be/foLgG44j2dU
```

---

## Author

**Benson Maina**

BSc Software Engineering  
African Leadership University

---

## License

This project was developed for educational purposes as part of African Leadership University coursework and is released under the MIT License.