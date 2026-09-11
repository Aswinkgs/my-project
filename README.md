Automated Cloud Infrastructure & Flask App Deployment
--------------------------------------------------
An end-to-end Infrastructure as Code (IaC) and Configuration Management pipeline that automatically provisions AWS EC2 infrastructure using Terraform, configures system dependencies and installs Docker via Ansible, and deploys a containerized Flask web application using Docker Compose.

Prerequisites
-----------------
Infrastructure Provisioning: Terraform (v1.x+)
Configuration Management: Ansible (v2.15+)
Container Orchestration: Docker & Docker Compose
Application Framework: Python 3.12, Flask
Cloud Provider: Amazon Web Services (AWS)

Repository Structure
---------------------

Configuration Management: Ansible (v2.15+)

Container Orchestration: Docker & Docker Compose

Application Framework: Python 3.12, Flask

Cloud Provider: Amazon Web Services (AWS)

Repository Structure
-------------------
```text
.
├── app/
│   ├── app.py
│   ├── Dockerfile
│   ├── docker-compose.yaml
│   └── req.txt
├── terraform/
│   ├── ec2.tf
│   ├── provider.tf
│   ├── security.tf
│   └── outputs.tf
├── hosts.ini
├── playbook.yml
├── terraform.sh
├── deploy.sh
└── README.md
```
                           
>>>>>>> refs/remotes/origin/main
