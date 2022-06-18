# IMAGE_NAME=$(cat uploads/env | grep IMAGE_NAME | cut -d '=' -f 2)
# echo "IMAGE_NAME: $IMAGE_NAME"

SERVICE_URL=$(gcloud run services list | grep testing)
# echo $SERVICE_URL
echo $SERVICE_URL > $(pwd)/service_url.txt  