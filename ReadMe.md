# 🚀 Docker Hub Container Registry Cleanup Automation

![Python](https://img.shields.io/badge/Python-3.12-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-blue)
![Docker Hub](https://img.shields.io/badge/Docker-Hub-2496ED)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# 📖 Project Overview

This project automates the identification and cleanup of outdated Docker images stored in Docker Hub using Python and GitHub Actions.

Instead of manually checking repositories and removing unused images, this solution automatically:

- Connects to Docker Hub using secure credentials
- Retrieves all available image tags
- Applies cleanup policies
- Identifies images eligible for cleanup
- Generates a cleanup report
- Uploads the report as a GitHub Actions artifact

---

# 📌 Problem Statement

As containerized applications grow, Docker repositories accumulate numerous outdated and unused image tags.

This leads to:

- Increased storage usage
- Difficult repository management
- Security risks due to outdated images
- Manual maintenance effort

This project automates repository analysis and cleanup reporting.

---

# 🎯 Objectives

- Automate Docker Hub image analysis
- Reduce manual maintenance
- Apply cleanup policies
- Generate detailed cleanup reports
- Integrate automation using GitHub Actions
- Secure credentials using GitHub Secrets

---

# ✨ Features

✅ Docker Hub Authentication

✅ Automatic Tag Retrieval

✅ Cleanup Policy

✅ Cleanup Report Generation

✅ GitHub Actions Integration

✅ Scheduled Workflow

✅ Manual Workflow Execution

✅ Secure Credential Management

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Cleanup Automation |
| GitHub Actions | CI/CD Pipeline |
| Docker Hub API | Repository Access |
| Requests Library | REST API Communication |
| GitHub Secrets | Secure Credentials |
| Markdown | Documentation |

---

# 📂 Project Structure

```
container-registry-cleanup/
│
├── .github/
│   └── workflows/
│       └── pipeline.yml
│
├── cleanup/
│   ├── cleanup.py
│   └── requirements.txt
│
├── screenshots/
│
├── Dockerfile
│
├── README.md
│
└── .gitignore
```

---

# ⚙ Workflow

```
GitHub Push / Schedule / Manual Run
            │
            ▼
Checkout Repository
            │
            ▼
Setup Python
            │
            ▼
Install Dependencies
            │
            ▼
Run cleanup.py
            │
            ▼
Authenticate Docker Hub
            │
            ▼
Fetch Image Tags
            │
            ▼
Apply Cleanup Policy
            │
            ▼
Generate cleanup.log
            │
            ▼
Upload Report
```

---

# 🔄 Cleanup Process

1. Authenticate to Docker Hub

2. Retrieve all image tags

3. Apply cleanup policy

4. Mark images

5. Generate cleanup report

6. Upload report artifact

---

# 🔐 Security

Docker Hub credentials are **not hardcoded**.

GitHub Secrets are used:

- DOCKER_USERNAME
- DOCKER_PASSWORD

---

# 📸 Project Screenshots

## 1️⃣ Project Folder

![Project Structure](screenshots/project-structure.png)

---

## 2️⃣ GitHub Repository

![Repository](screenshots/github-repository.png)

---

## 3️⃣ GitHub Actions Workflow

![Workflow](screenshots/github-actions-workflow.png)

---

## 4️⃣ Successful Workflow Execution

![Workflow Success](screenshots/workflow-success.png)

---

## 5️⃣ GitHub Secrets

![Secrets](screenshots/github-secrets.png)

---

## 6️⃣ Docker Hub Repository

![Docker Hub](screenshots/dockerhub-repository.png)

---

## 7️⃣ Docker Hub Tags

![Tags](screenshots/dockerhub-tags.png)

---

## 8️⃣ Cleanup Script Output

![Cleanup Output](screenshots/python-output.png)

---

## 9️⃣ Cleanup Log

![Cleanup Log](screenshots/cleanup-log.png)

---

## 🔟 GitHub Actions Artifact

![Artifact](screenshots/artifact.png)

---

## 1️⃣1️⃣ Workflow Logs

![Workflow Logs](screenshots/workflow-logs.png)

---

# 👥 Team Members & Roles

| Team Member | Role |
|-------------|------|
| Member 1 | Project Planning & Requirement Analysis |
| Member 2 | Python Cleanup Script Development |
| Member 3 | GitHub Actions CI/CD Pipeline |
| Member 4 | Docker Hub Integration & Testing |

> Replace the names above with the exact names and roles from your project report.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/aviraljain0/container-registry-cleanup.git
```

Move into the project directory

```bash
cd container-registry-cleanup
```

Install dependencies

```bash
pip install -r cleanup/requirements.txt
```

---

# ▶ Running Locally

Configure environment variables:

```
DOCKER_USERNAME
DOCKER_PASSWORD
```

Run:

```bash
python cleanup/cleanup.py
```

---

# ⚡ GitHub Actions

The workflow can be triggered by:

- Push to `main`
- Manual execution (`workflow_dispatch`)
- Scheduled execution

---

# 📄 Generated Report

The workflow creates:

```
cleanup.log
```

which is uploaded as a GitHub Actions artifact.

---

# 📈 Expected Outcomes

- Automated Docker Hub analysis
- Reduced manual effort
- Improved repository management
- Secure CI/CD implementation
- Automated reporting

---

# 🔮 Future Enhancements

- Configurable retention policies
- Email notifications
- Slack/MS Teams integration
- Multi-repository cleanup
- Dashboard for cleanup analytics
- Administrator approval before deletion

---

# 🏆 Conclusion

This project demonstrates the use of Python, Docker Hub APIs, and GitHub Actions to automate container registry maintenance. By integrating cleanup logic into a CI/CD workflow, the solution reduces manual effort, improves repository organization, and generates actionable cleanup reports while following secure credential management practices.

---

# 🙏 Acknowledgements

- IBM SkillsBuild
- GitHub
- Docker Hub
- Python Community

---

# 📧 Contact

**Repository Owner:** Aviral Jain

GitHub: https://github.com/aviraljain0

---
