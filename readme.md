# FastAPI CRUD Application with Kubernetes Deployment

## Overview

This project demonstrates a FastAPI CRUD (Create, Read, Update, Delete) application deployed on a Kubernetes cluster using Azure Kubernetes Service (AKS). The application is containerized using Docker, and continuous integration and deployment (CI/CD) are managed through GitHub Actions.

## API Description

The FastAPI application provides endpoints to create, read, update, and delete items. Each item has an ID, name, and price.

### Endpoints

- **Create an Item**
  - **URL:** `/items/`
  - **Method:** `POST`
  - **Request Body:**
    ```json
    {
      "id": 1,
      "name": "Item 1",
      "price": 10.5
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "Item 1",
      "price": 10.5
    }
    ```

- **Retrieve All Items**
  - **URL:** `/items/`
  - **Method:** `GET`
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "name": "Item 1",
        "price": 10.5
      }
    ]
    ```

- **Retrieve a Specific Item**
  - **URL:** `/items/{item_id}`
  - **Method:** `GET`
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "Item 1",
      "price": 10.5
    }
    ```

- **Update an Item**
  - **URL:** `/items/{item_id}`
  - **Method:** `PUT`
  - **Request Body:**
    ```json
    {
      "id": 1,
      "name": "Updated Item",
      "price": 20.0
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "Updated Item",
      "price": 20.0
    }
    ```

- **Delete an Item**
  - **URL:** `/items/{item_id}`
  - **Method:** `DELETE`
  - **Response:**
    ```json
    {
      "detail": "Item deleted"
    }
    ```

## Setup and Deployment

### Prerequisites

- Docker
- Kubernetes CLI (`kubectl`)
- Azure CLI (`az`)
- Terraform

### Steps

1. **Clone the Repository**

   ```sh
   git clone <repository-url>
   cd <repository-name>
```
2. **Build and Push Docker Image**

   ```sh
   docker buildx build --platform linux/amd64 -t <dockerhub-username>/fastapi-crud:latest --push .
   ```

3. **Configure Terraform**

   Initialize and apply Terraform configurations:

   ```sh
   terraform init
   terraform plan
   terraform apply -auto-approve
   ```

4. **Deploy to Kubernetes**

   Apply Kubernetes configurations:

   ```sh
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```

### GitHub Actions Configuration

Add the following secrets to your GitHub repository under **Settings** > **Secrets** and variables > **Actions**:

- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password
- `AZURE_CREDENTIALS`: Your Azure credentials in JSON format
- `AZURE_RESOURCE_GROUP`: The resource group name for your AKS cluster
- `AKS_CLUSTER_NAME`: The name of your AKS cluster

### GitHub Actions Workflow

The CI/CD pipeline is defined in `.github/workflows/main.yml`. It performs the following steps:

- Checks out the code
- Sets up Python and installs dependencies
- Logs in to Docker Hub
- Builds and pushes the Docker image
- Logs in to Azure
- Initializes and applies Terraform configurations
- Configures `kubectl`
- Deploys the application to AKS
- Waits for the Load Balancer IP
- Tests the FastAPI endpoints

### Testing the Endpoints

Use the following commands to test the FastAPI endpoints from the internet:

1. **Create an Item**

   ```sh
   curl -X POST http://<external-ip>/items/ -H "Content-Type: application/json" -d '{"id": 1, "name": "Item 1", "price": 10.5}'
   ```

2. **Retrieve All Items**

   ```sh
   curl http://<external-ip>/items/
   ```

3. **Retrieve a Specific Item**

   ```sh
   curl http://<external-ip>/items/1
   ```

4. **Update an Item**

   ```sh
   curl -X PUT http://<external-ip>/items/1 -H "Content-Type: application/json" -d '{"id": 1, "name": "Updated Item", "price": 20.0}'
   ```

5. **Delete an Item**

   ```sh
   curl -X DELETE http://<external-ip>/items/1
   ```

### Local Testing

To test the application locally, follow these steps:

1. **Run FastAPI Locally**

   ```sh
   uvicorn app.main:app --reload
   ```

2. **Test Local Endpoints**

   - **Create an Item:**

     ```sh
     curl -X POST http://127.0.0.1:8000/items/ -H "Content-Type: application/json" -d '{"id": 1, "name": "Item 1", "price": 10.5}'
     ```

   - **Retrieve All Items:**

     ```sh
     curl http://127.0.0.1:8000/items/
     ```

   - **Retrieve a Specific Item:**

     ```sh
     curl http://127.0.0.1:8000/items/1
     ```

   - **Update an Item:**

     ```sh
     curl -X PUT http://127.0.0.1:8000/items/1 -H "Content-Type: application/json" -d '{"id": 1, "name": "Updated Item", "price": 20.0}'
     ```

   - **Delete an Item:**

     ```sh
     curl -X DELETE http://127.0.0.1:8000/items/1
     ```

## Conclusion

This setup demonstrates a complete CI/CD pipeline for deploying a FastAPI application to an AKS cluster using Docker and Terraform, with end-to-end automation managed by GitHub Actions. You can use the provided steps and commands to replicate and verify the deployment and functionality of the application.
```
