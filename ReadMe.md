# Container Registry with Automated Image Cleanup

## IBM Internship Project

A DevOps automation project that demonstrates how container images can be managed efficiently using Docker, GitHub Actions, and Python automation.

The project automatically scans a Docker Hub repository, identifies old or unnecessary image tags based on predefined cleanup policies, generates a cleanup report, and integrates the complete process into a CI/CD pipeline.

---

## Project Objective

Container registries often store multiple Docker images created during development, testing, and deployment. Over time, these images consume unnecessary storage and become difficult to manage.

The objective of this project is to automate the image management process by:

- Scanning Docker Hub repositories
- Identifying old and unused image tags
- Applying cleanup policies
- Generating cleanup reports
- Automating the complete workflow using GitHub Actions

---

## Technology Stack

- Docker
- Docker Hub
- Python 3.11
- Git
- GitHub
- GitHub Actions
- YAML
- Requests Library

---

## Project Structure

```
container-registry-cleanup
│
├── .github
│   └── workflows
│       └── pipeline.yml
│
├── app
│   ├── app.py
│   └── requirements.txt
│
├── cleanup
│   ├── cleanup.py
│   └── requirements.txt
│
├── Dockerfile
├── README.md
└── .gitignore
```

---

## Workflow

The CI/CD pipeline follows the steps below:

```
Developer Pushes Code
        │
        ▼
GitHub Actions Triggered
        │
        ▼
Checkout Repository
        │
        ▼
Setup Python Environment
        │
        ▼
Install Dependencies
        │
        ▼
Login to Docker Hub
        │
        ▼
Pull Docker Image
        │
        ▼
Run Docker Container
        │
        ▼
Execute Cleanup Script
        │
        ▼
Generate cleanup.log
        │
        ▼
Upload Cleanup Report
```

---

## Features

- Automated Docker Hub integration
- Container image verification
- Python-based cleanup automation
- Cleanup report generation
- GitHub Actions CI/CD pipeline
- Automatic artifact upload
- Secure Docker Hub authentication using GitHub Secrets

---

## Docker Repository

Docker Hub Repository:

```
ibm1container1cleanup1team/container-registry-cleanup
```

---

## GitHub Actions

The workflow automatically executes whenever code is pushed to the **main** branch.

Pipeline includes:

- Checkout Repository
- Setup Python
- Install Dependencies
- Docker Hub Login
- Pull Docker Image
- Run Docker Container
- Execute Cleanup Script
- Upload Cleanup Report

---

## Team Members

| Team Member | Role |
|-------------|------|
| Narayan Vyas | Docker & Container Registry Engineer |
| Shashank Rawat | Python Automation Developer |
| Aviral Jain | CI/CD Engineer |
| Loveneet Rulhan | Testing Engineer |
| Sourabh Saini | Monitoring Engineer |

---

## My Contribution

As the **CI/CD Engineer**, my responsibilities included:

- Configuring GitHub Actions workflow
- Integrating Docker Hub authentication
- Pulling Docker images automatically
- Running Docker containers
- Executing the Python cleanup script
- Uploading cleanup logs as GitHub Artifacts
- Automating the complete workflow on every push

---

## Output

The workflow generates:

- Docker Image Verification
- Cleanup Log (`cleanup.log`)
- GitHub Actions Build Report
- Cleanup Report Artifact

---

## Future Enhancements

- Automatic deletion of obsolete Docker images
- Email notifications after cleanup
- Slack or Microsoft Teams integration
- Dashboard for cleanup statistics
- Support for multiple container registries

---

## Conclusion

This project demonstrates the implementation of a DevOps-based automated container registry management system. It combines Docker, Python automation, and GitHub Actions to streamline container image management, reduce manual effort, and improve operational efficiency.

---

## License

This project was developed as part of the IBM Internship Program for educational and learning purposes.
