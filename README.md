# Azure Kubernetes Service (AKS) Microservices Architecture Deployment

This project demonstrates deploying a containerized microservices application on **Azure Kubernetes Service (AKS)** using **Docker, Azure Container Registry (ACR), and Terraform**.

The application consists of:

- **Frontend** – HTML/CSS web application  
- **Backend** – Python REST API  
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
   ![image showing built docker images](docs/docker-images.png)


## Push Images to Azure Container Registry

- docker push mojeed0088.azurecr.io/frontend:v1
- docker push mojeed0088.azurecr.io/backend:v1

Images in ACR
![containers](docs/repository-image.png)


![containers](docs/azurecr-repository.png)


## Provisioned Azure Kubernetes Services (AKS) with Terraform

- terraform plan
![image showing terraform-plan](docs/terraform-plan-image.png)

- terraform apply
![image showing infrasructures provision after terraform apply](docs/resources-in-azure.png)


## Deploy to Kubernetes

- Apply the Kubernetes manifests in order:
- kubectl apply -f k8s/database/
- kubectl apply -f k8s/backend/
- kubectl apply -f k8s/frontend/


## AKS Nodes and Pods After deployment

kubectl get nodes 
![containers](docs/kubectl-get-node-screenshot.png)

kubectl get pods
![Image showing all pos are running after deployment](docs/pods-running-screenshot.png)


## Service Access

- Frontend: Exposed via LoadBalancer (External IP)
- Backend: Internal ClusterIP service
- Database: Internal ClusterIP service

Service IPs
![image showing the external ip address](docs/IPs-address.png)


## Application Access

Browser image
![testing the frontend external ip on browser](docs/frontendapp-running-aks.png)


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
    azure-aks-microservices
    ├── README.md
    ├── backend
    │   ├── Dockerfile
    │   ├── app.py
    │   └── requirements.txt
    ├── docs
    │   ├── azurecr-repository.png
    │   ├── docker-images.png
    │   ├── frontendapp-running-aks.png
    │   ├── kubectl-get-node-screenshot.png
    │   ├── pods-running-screenshot.png
    │   ├── repository-image.png
    │   ├── resources-in-azure.png
    │   └── terraform-plan-image.png
    ├── frontend
    │   ├── Dockerfile
    │   ├── health.html
    │   └── index.html
    ├── k8s
    │   ├── backend
    │   │   ├── backend-deployment.yaml
    │   │   └── backend-service.yaml
    │   ├── database
    │   │   ├── postgres-deployment.yaml
    │   │   ├── postgres-pvc.yaml
    │   │   ├── postgres-secret.example.yaml
    │   │   ├── postgres-secret.yaml
    │   │   └── postgres-service.yaml
    │   ├── frontend
    │   │   ├── deployment.yaml
    │   │   └── service.yaml
    │   └── namespaces.yaml
    └── terraform
        ├── acr.tf
        ├── main.tf
        ├── outputs.tf
        ├── provider.tf
        ├── terraform.tfstate
        ├── terraform.tfstate.backup
        ├── terraform.tfvars
        └── variables.tf


Author

Mojeed Tijani

Azure Cloud Engineer  

Certifications

• AZ-104 – Microsoft Azure Administrator  
• KCNA – Kubernetes and Cloud Native Associate  
• FinOps Certified Engineer

