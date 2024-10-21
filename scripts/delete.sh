set -u # or set -o nounset
: "$ACR_NAME"
: "$VERSION"


# Delete the Kubernetes deployment
echo "Deleting Kubernetes deployment..."

envsubst < ./scripts/kubernetes/deployment.yaml | kubectl delete -f -

echo "Deletion complete."