set -u # or set -o nounset
: "$ACR_NAME"
: "$VERSION"
: "$ACR_UN"
: "$ACR_PW"


# Log in to Azure Container Registry
echo "Logging in to Azure Container Registry..."
docker login $ACR_NAME --username $ACR_UN --password $ACR_PW

# Push book catalog image
echo "Pushing book catalog image..."
docker push $ACR_NAME/book-catalog:$VERSION

# Push inventory management image
echo "Pushing inventory management image..."
docker push $ACR_NAME/inventory-management:$VERSION

echo "Push complete."