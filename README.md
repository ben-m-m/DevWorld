# DevWorld

DevWorld – AI-Powered GitHub Engineering Analytics Platform

## Overview

DevWorld is an AI-powered engineering analytics platform that transforms any public GitHub profile into an interactive software engineering dashboard.

Instead of simply displaying repository statistics, DevWorld analyzes a developer's GitHub portfolio, visualizes engineering metrics, and leverages Google Gemini AI to generate professional engineering reviews for individual repositories.

The project was developed as part of the African Leadership University (ALU) – Playing Around With APIs summative assessment.

## Problem Statement

GitHub provides repository information but does not help developers understand:

- How healthy their repositories are
- Which projects demonstrate engineering maturity
- Which programming languages dominate their work
- Repository popularity and activity
- Areas that need improvement
- Professional engineering feedback

DevWorld bridges this gap by combining the GitHub REST API, Google Gemini AI, and interactive engineering analytics into a single platform.

## Features

### GitHub User Search

Search any public GitHub username.

The application automatically retrieves:

- Profile information
- Repository list
- Followers
- Following
- Public repositories
- Bio
- Company
- Website
- Join date

using the GitHub REST API.

### Engineering Dashboard

Each GitHub profile generates an engineering dashboard containing:

- Total repositories
- Total stars
- Total forks
- Primary programming language
- Largest repository
- Most starred repository
- Active repositories

These statistics are calculated dynamically from the GitHub API response.

### Repository Explorer

Repositories can be explored using:

- Search by repository name
- Sort repositories
- Filter by programming language

Supported sorting includes:

- Newest updated
- Oldest updated
- Newest created
- Oldest created
- Alphabetical A–Z
- Alphabetical Z–A
- Highest stars
- Lowest stars
- Highest forks
- Lowest forks
- Largest size
- Smallest size

Whenever filters change, both the repository list and all dashboard charts update automatically.

### Interactive Analytics

Selecting a repository immediately updates the dashboard.

The following charts are redrawn using only the selected repository (or filtered repositories):

- Language Distribution
- Repository Stars
- Repository Forks

The charts are built using Chart.js.

### Repository Intelligence

Selecting a repository displays an Engineering Intelligence Panel.

The panel includes:

- Repository description
- Programming language
- Stars
- Forks
- Repository size
- Creation date
- Last update date

Alongside calculated engineering metrics:

#### Maintenance Score

Calculated using:

- Archived status
- Open issues

Higher scores indicate better maintainability.

#### Popularity Score

Calculated using:

- GitHub stars

Higher popularity results in higher scores.

#### Activity Score

Calculated from:

- Repository last updated date

Recently maintained repositories receive higher scores.

#### Overall Engineering Health

The three metrics are combined into a final engineering score.

Possible ratings include:

- Excellent
- Good
- Average
- Needs More Attention

### AI Engineering Review

One of DevWorld's key features is its integration with Google Gemini AI.

Each repository includes an Analyze with AI button.

When selected:

- Repository metadata is collected.
- A structured engineering prompt is generated.
- Gemini AI performs a professional repository review.
- The generated report is rendered on a dedicated analysis page.

The AI evaluates:

- Executive Summary
- Software Architecture
- Project Strengths
- Weaknesses
- Maintainability
- Scalability
- Documentation
- Engineering Recommendations
- Overall Engineering Score

This simulates a professional code review performed by a senior software engineer.

## Technologies Used

### Backend

- Python
- Flask
- Gunicorn

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript (Vanilla)

### APIs

#### GitHub REST API

Used for:

- User profiles
- Repository information
- Repository metadata
- Programming languages
- Repository statistics

#### Google Gemini API

Used to generate AI-powered engineering reviews.

### Visualization

- Chart.js

## Deployment Stack

The application is designed for production deployment using:

- Ubuntu Linux
- Gunicorn
- Nginx
- HAProxy
- Let's Encrypt SSL
- Round Robin Load Balancing

### Architecture

```text
                 Internet
                     │
                     ▼
             mainaben.tech
                     │
                     ▼
                HAProxy (lb-01)
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
     web-01                    web-02
        │                         │
     Nginx                     Nginx
        │                         │
     Gunicorn                 Gunicorn
        │                         │
       Flask                   Flask
```

This setup provides:

- High availability
- Load balancing
- SSL termination
- Fault tolerance
- Scalability

## Project Structure

```text
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

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/DevWorld.git

cd DevWorld
```

### Create a virtual environment

```bash
python3 -m venv .venv
```

### Activate it

#### Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a .env file in the project root.

```env
SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_gemini_api_key

GITHUB_CLIENT_ID=optional

GITHUB_CLIENT_SECRET=optional

FLASK_ENV=development
```

## Running the Application

### Development

```bash
python app.py
```

### Production

```bash
gunicorn app:app
```

### Open

```text
http://localhost:5000
```

## API Requirements

### GitHub API

The application consumes:

- GET /users/{username}
- GET /users/{username}/repos

Documentation:

- https://docs.github.com/en/rest

### Google Gemini API

Requires:

- Gemini API Key
- Google AI Studio account

Documentation:

- https://ai.google.dev/

## Future Improvements

Potential future enhancements include:

- GitHub OAuth authentication
- Repository comparison using AI
- Commit history analysis
- Contributor analytics
- Issue and pull request analytics
- Code quality metrics
- Export AI reports as PDF
- AI chat assistant for repositories
- Repository trend analysis over time
- Personalized engineering recommendations

## Live Demo

### Production URL

https://YOUR-DOMAIN.tech

(Replace with your deployed domain.)

### Video Demonstration

#### Project Walkthrough

https://YOUR-YOUTUBE-VIDEO-LINK

(Replace with your presentation video link.)

## Author

- Benson Maina
- BSc Software Engineering
- African Leadership University

## License

This project was developed for educational purposes as part of the African Leadership University (ALU) coursework and is released under the MIT License.