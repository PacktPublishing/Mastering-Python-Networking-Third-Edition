#!/usr/bin/env python3
import requests
import pprint

myheaders={'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'}
orgId = '549236'
url = 'https://dashboard.meraki.com/api/v0/organizations/' + orgId + '/networks'
response = requests.get(url, headers=myheaders, verify=False)
pprint.pprint(response.json())

