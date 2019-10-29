from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.network import NetworkManagementClient

client = get_client_from_auth_file(NetworkManagementClient)
print("Network Management Client API Version: " + client.DEFAULT_API_VERSION)

