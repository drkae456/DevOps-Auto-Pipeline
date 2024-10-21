output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}

output "resource_group_location" {
  value = azurerm_resource_group.rg.location
}

output "acr_name" {
  value = azurerm_container_registry.acr.name
}

output "acr_login_server" {
  value = azurerm_container_registry.acr.login_server
}

output "acr_admin_username" {
  value = azurerm_container_registry.acr.admin_username
}

output "aks_cluster_name" {
  value = azurerm_kubernetes_cluster.aks.name
}

output "aks_cluster_fqdn" {
  value = azurerm_kubernetes_cluster.aks.fqdn
}

output "aks_node_resource_group" {
  value = azurerm_kubernetes_cluster.aks.node_resource_group
}

output "reminder_message" {
  value = <<EOT

Resource creation complete!

Resources created:
- Resource Group: ${azurerm_resource_group.rg.name} (Location: ${azurerm_resource_group.rg.location})
- Azure Container Registry: ${azurerm_container_registry.acr.name} (Login server: ${azurerm_container_registry.acr.login_server})
- AKS Cluster: ${azurerm_kubernetes_cluster.aks.name} (FQDN: ${azurerm_kubernetes_cluster.aks.fqdn})
  - Node Resource Group: ${azurerm_kubernetes_cluster.aks.node_resource_group}

IMPORTANT REMINDER:
Before proceeding with deployment, please ensure you set the following variables in your GitHub repository secrets or deployment environment:

1. ACR_NAME: ${azurerm_container_registry.acr.login_server}
2. ACR_UN: ${azurerm_container_registry.acr.admin_username}
3. ACR_PW: (ACR PASSWORD)
4. KUBE_CONFIG: (Base64 encoded kubeconfig for the AKS cluster)
5. DATABASE_URL: (Your database connection string)

To get the kubeconfig for your AKS cluster, run:
az aks get-credentials --resource-group ${azurerm_resource_group.rg.name} --name ${azurerm_kubernetes_cluster.aks.name}

Then encode it to base64:
cat ~/.kube/config | base64 | tr -d '\n'

Set these values in your GitHub repository secrets before running your deployment workflow.

EOT
}