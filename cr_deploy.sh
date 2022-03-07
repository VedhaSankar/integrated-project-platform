#!/bin/bash

# Get project image name
IMAGE_NAME=$(cat .env | grep IMAGE_NAME | cut -d '=' -f 3)

# Create a Docker repository in Artifact Registry
gcloud artifacts repositories \
     create project-images \
     --repository-format=docker \
     --location=us-central1 \
     --description="Docker repository"  

# Get project ID
export PROJECT=$(gcloud info --format='value(config.project)')

# Build the Docker image
gcloud builds submit --tag \
     us-central1-docker.pkg.dev/$PROJECT/project-images/mongo-docker:latest

# Run image on CR
gcloud run deploy mongo-docker --image us-central1-docker.pkg.dev/$PROJECT/my-docker-repo/mongo-docker:latest