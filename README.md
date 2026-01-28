# Azure Kubernetes Service (AKS) Microservices Architecture Deployment

This project demonstrates deploying a containerized microservices application on **Azure Kubernetes Service (AKS)** using **Docker, Azure Container Registry (ACR), and Terraform**.

The application consists of:

- **Frontend** – Nginx-based web application  
- **Backend** – Node.js REST API  
- **Database** – PostgreSQL  

---

## Architecture Overview

- Azure Kubernetes Service (**AKS**) deployed in **Canada Central**
- Azure Container Registry (**ACR**) for container image storage
- Microservices deployed into a dedicated Kubernetes namespace
- Frontend exposed using a **LoadBalancer** service
- Backend and Database exposed internally using **ClusterIP**

---

## Deployment Guide

### Build Docker Images

- docker build -t mojeed0088.azurecr.io/frontend:v1 ./frontend
- docker build -t mojeed0088.azurecr.io/backend:v1 ./backend

Built & containerized images
   ![containers](docs/container.png)


## Push Images to Azure Container Registry

- docker push mojeed0088.azurecr.io/frontend:v1
- docker push mojeed0088.azurecr.io/backend:v1

Images in ACR
![containers](docs/repository-image.png)

![containers](docs/azurecr-repository.png)


## Deploy to Kubernetes

- Apply the Kubernetes manifests in order:
- kubectl apply -f k8s-manifests/database
- kubectl apply -f k8s-manifests/backend
- kubectl apply -f k8s-manifests/frontend

AKS Nodes and Pods
![containers](docs/kubectl-get-node-screenshot.png)


## Service Access

- Frontend: Exposed via LoadBalancer (External IP)
- Backend: Internal ClusterIP service
- Database: Internal ClusterIP service

Service IPs
![containers](docs/IPs-image.png)


## Application Access

Browser image
![containers](docs/browser-image.png)


## Key Skills Demonstrated

- Azure Kubernetes Service (AKS)
- Azure Container Registry (ACR)
- Docker & Containerization
- Kubernetes (Deployments, Services, Namespaces)
- Infrastructure as Code with Terraform
- Microservices Architecture
- Cloud Networking & Load Balancing


## Repository Structure

 ```                   
azure-aks-microservices/
│
├── frontend/ # Frontend application source code
├── backend/ # Backend (Node.js API) source code
├── database/ # Database configuration files
│
├── terraform/ # Infrastructure as Code (AKS, ACR, networking)
├── k8s-manifests/ # Kubernetes deployment & service manifests
│
├── docs/ # Project screenshots and evidence
│
├── README.md
└── .gitignore


Author

Mojeed Tijani 
Azure Cloud Engineer  

Certifications
• AZ-104 – Microsoft Azure Administrator  
• KCNA – Kubernetes and Cloud Native Associate  
• FinOps Certified Engineer

