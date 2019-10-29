#!/usr/bin/env python3
#
# Referenced example https://docs.microsoft.com/en-us/azure/virtual-machines/windows/python
#
from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.network import NetworkManagementClient

network_client = get_client_from_auth_file(NetworkManagementClient)

GROUP_NAME = 'Mastering-Python-Networking'
LOCATION = 'westus2'

def create_subnet(network_client):
    subnet_params = {
        'address_prefix': '192.168.0.128/25'
    }
    creation_result = network_client.subnets.create_or_update(
        GROUP_NAME,
        'WEST-US-2_VNet_1',
        'WEST-US-2_VNet_1_Subnet_2',
        subnet_params
    )

    return creation_result.result()

creation_result = create_subnet(network_client)
print(creation_result)


