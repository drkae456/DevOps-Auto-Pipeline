set -u # or set -o nounset
: "$ACR_NAME"
: "$VERSION"

# Build book catalog image
echo "Building book catalog image..."
docker build -t $ACR_NAME/book-catalog:$VERSION ./book_catalog

# Build inventory management image
echo "Building inventory management image..."
docker build -t $ACR_NAME/inventory-management:$VERSION ./inventory_management

echo "Build complete."