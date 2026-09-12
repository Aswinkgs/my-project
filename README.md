# Automated Cloud Infrastructure & Flask App Deployment

An end-to-end Infrastructure as Code (IaC) and Configuration Management pipeline that automatically provisions AWS EC2 infrastructure using Terraform, configures system dependencies and installs Docker via Ansible, and deploys a containerized Flask web application using Docker Compose. The entire workflow is automated through a Jenkins CI/CD pipeline, triggered on every push to the repository.

## Prerequisites

- **Infrastructure Provisioning**: Terraform (v1.x+)
- **Configuration Management**: Ansible (v2.15+)
- **Container Orchestration**: Docker & Docker Compose
- **Application Framework**: Python 3.12, Flask
- **Cloud Provider**: Amazon Web Services (AWS)
- **CI/CD**: Jenkins

## Local Workstation Requirements

Ensure the following CLI tools are installed on your workstation:

- **AWS CLI**: Configured with valid credentials (`aws configure`)
- **Terraform CLI**: Installed and accessible in your system PATH
- **Ansible**: Installed locally or available via WSL / Python environment
- **SSH Client**: OpenSSH or equivalent terminal client for instance connection
- **Git**: For version control and triggering CI/CD builds

## Repository Structure
```
.
├── app/
│ ├── app.py
│ ├── Dockerfile
│ ├── docker-compose.yaml
│ └── req.txt
├── terraform/
│ ├── ec2.tf
│ ├── provider.tf
│ ├── security.tf
│ └── outputs.tf
├── hosts.ini
├── playbook.yml
├── Jenkinsfile
├── terraform.sh
├── deploy.sh
└── README.md
```
## Architecture Overview
```
GitHub Push
│
▼
Jenkins Pipeline Triggered
│
├── Terraform Apply → Provisions EC2 instance + Security Group
│ (state managed remotely via S3 backend)
│
├── Ansible Playbook → Installs Docker, configures host environment
│
└── Docker Compose → Deploys containerized Flask application
```

## Setup & Deployment

### 1. Configure AWS Credentials
```bash
aws configure
```

### 2. Initialize Terraform
```bash
cd terraform
terraform init
```

### 3. Provision Infrastructure
```bash
terraform apply -auto-approve
```
This creates the EC2 instance and security group, and outputs the instance's public IP.

### 4. Update Ansible Inventory
Update `hosts.ini` with the EC2 instance's public IP output from Terraform.

### 5. Run the Ansible Playbook
```bash
ansible-playbook -i hosts.ini playbook.yml
```
This installs Docker and required dependencies, and deploys the Flask application via Docker Compose.

## CI/CD Pipeline (Jenkins)

The `Jenkinsfile` automates the full deployment workflow:

1. **Checkout** — Pulls the latest code from the repository
2. **Terraform Apply** — Provisions or updates AWS infrastructure using remote state (S3 backend)
3. **Ansible Playbook** — Configures the server and deploys the Flask application

The pipeline is triggered automatically via a GitHub webhook on every push to `main`.


## Notes

- Terraform state is stored remotely in an S3 bucket to ensure consistency between local runs and Jenkins pipeline executions, avoiding state drift or duplicate resource errors.
- AWS credentials and SSH keys used by Jenkins are stored securely using Jenkins Credentials, never hardcoded in the pipeline or repository.