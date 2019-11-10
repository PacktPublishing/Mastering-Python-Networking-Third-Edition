#!/usr/bin/env python3
import requests
import json
import pytest

# Getting NX-OSv Version with NXAPI
url='http://172.16.1.21/ins'
switchuser='cisco'
switchpassword='cisco'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show version",
      "version": 1.2
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
nxos_version = response['result']['body']['sys_ver_str']

def test_transaction():
     assert nxos_version != False

