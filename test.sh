IMAGE_NAME=$(cat uploads/env | grep IMAGE_NAME | cut -d '=' -f 2)
echo "IMAGE_NAME: $IMAGE_NAME"