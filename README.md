CI/CD Pipeline: GitHub Actions, Docker, and Local Deployment

This repository demonstrates a complete Continuous Integration (CI) and Continuous Delivery (CD) pipeline. The pipeline is fully automated using GitHub Actions to build, test, and containerize a simple Python Flask application, then push the resulting image to Docker Hub.

This setup provides a highly repeatable and version-controlled deployment process without relying on external cloud providers (AWS, Azure, GCP).

Pipeline Overview

The workflow executes the following steps automatically on every push to the main branch:

Test (CI): Run unit tests (pytest) against the application code.

Build (CI): Build a production-ready Docker image based on the Dockerfile.

Push (CI/CD): Tag the image with the commit SHA and :latest and push both tags to Docker Hub.

Deploy (CD): The image is now ready for deployment anywhere Docker is installed (local machine, Minikube, or a remote server).

Technology Stack

Tool

Purpose

Python/Flask

The simple web application used as the build target.

Dockerfile

Defines the steps to package the Python app into a light-weight container image.

GitHub Actions

The automation engine for the CI/CD pipeline (testing, building, pushing).

Docker Hub

The public/private registry used to store and manage the built Docker images.

Docker Compose

Used locally to pull the image and run the container with correct port mapping.

Prerequisites

To replicate or manage this pipeline, you need:

A GitHub Account with this repository cloned.

A Docker Hub Account.

GitHub Repository Secrets: The following secrets must be configured in your GitHub repository (Settings > Secrets and variables > Actions):

DOCKER_USERNAME

DOCKER_PASSWORD (This should be a Personal Access Token, not your main password, for security).

Docker Desktop installed locally (for the final deployment step).

Repository Structure

File/Folder

Description

app.py

The main Flask application (runs on port 5000).

test_app.py

Unit tests for the application, run by pytest.

Dockerfile

Defines the container image build process.

requirements.txt

Python dependencies (Flask, gunicorn, pytest).

docker-compose.yml

Local deployment file to run the final Docker image.

.gitignore

Ensures development files (e.g., virtual environments) are ignored.

.github/workflows/main.yml

The full GitHub Actions CI/CD pipeline definition.

Local Deployment Guide (Continuous Delivery)

Once the GitHub Actions workflow successfully pushes the new image to Docker Hub, you can pull and run it locally:
<img width="1920" height="974" alt="Image" src="https://github.com/user-attachments/assets/e6d3ffa4-8b90-4581-ba38-76efc1a02fc1" />

DOckerHub Image CI Result
<img width="1845" height="977" alt="Image" src="https://github.com/user-attachments/assets/7e212074-96d0-4e9e-ab1c-0484867efb88" />

Update docker-compose.yml:
Before running, ensure you have replaced your-dockerhub-username in the docker-compose.yml file with your actual Docker Hub username.

# Example snippet from docker-compose.yml
image: **your-dockerhub-username**/cicd-flask-app:latest 


Deploy the Container:
In your project root directory, execute the Docker Compose command:

docker compose up -d
<img width="745" height="449" alt="Image" src="https://github.com/user-attachments/assets/8c31ccc2-d97d-4523-92c4-709361893aa5" />

Access the Application:
Open your web browser and navigate to:

http://localhost:8080
<img width="1920" height="984" alt="Image" src="https://github.com/user-attachments/assets/ae3843bd-4753-4b84-9d9c-d34360da3e79" />

The application is now running as a container, pulling the latest image built by your automated pipeline.

Management Commands

To manage the running container:

To stop the application: docker compose stop

To stop and remove the container: docker compose down

To view application logs: docker compose logs -f`
