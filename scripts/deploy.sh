set -o # or set -o nounset
: "$ACR_NAME"
: "$VERSION"
# Apply the Kubernetes deployment

echo "Applying Kubernetes deployment..."
envsubst < ./scripts/kubernetes/deployment.yaml | kubectl apply -f -

echo "Deployment complete."