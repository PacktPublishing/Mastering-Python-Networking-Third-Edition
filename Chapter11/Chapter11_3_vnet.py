#!/usr/bin/env python3
#
# Referenced exzmple https://docs.microsoft.com/en-us/azure/virtual-machines/windows/python
#

from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.network import NetworkManagementClient

network_client = get_client_from_auth_file(NetworkManagementClient)

GROUP_NAME = 'Mastering-Python-Networking'
LOCATION = 'eastus'

def create_vnet(network_client):
    vnet_params = {
        'location': LOCATION,
        'address_space': {
            'address_prefixes': ['10.0.0.0/16']
        }
    }
    creation_result = network_client.virtual_networks.create_or_update(
        GROUP_NAME,
        'EAST-US_VNet_1',
        vnet_params
    )
    return creation_result.result()


creation_result = create_vnet(network_client)
print("------------------------------------------------------")
print(creation_result)
input('Press enter to continue...')


def create_subnet(network_client):
    subnet_params = {
        'address_prefix': '10.0.1.0/24'
    }
    creation_result = network_client.subnets.create_or_update(
        GROUP_NAME,
        'EAST-US_VNet_1',
        'EAST-US_VNet_1_Subnet_1',
        subnet_params
    )

    return creation_result.result()


creation_result = create_subnet(network_client)
print("------------------------------------------------------")
print(creation_result)
input('Press enter to continue...')


