#!/bin/bash

# Get project image name
# IMAGE_NAME=$(cat uploads/env | grep IMAGE_NAME | cut -d '=' -f 3)

# Create a Docker repository in Artifact Registry
gcloud artifacts repositories \
     create project-images \
     --repository-format=docker \
     --location=us-central1 \
     --description="Docker repository"  

# Get project ID
export PROJECT=$(gcloud info --format='value(config.project)')

cd uploads/mongo-docker/
docker build -t testing .

IMAGE_NAME="testing"

# Build the Docker image
gcloud builds submit --tag \
     us-central1-docker.pkg.dev/$PROJECT/project-images/$IMAGE_NAME:latest

# Run image on CR
gcloud run deploy $IMAGE_NAME --port=5003 --image us-central1-docker.pkg.dev/$PROJECT/project-images/$IMAGE_NAME:latest