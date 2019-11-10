#!/usr/bin/env python3
#
# derived from https://devnet-pubhub-site.s3.amazonaws.com/media/pyats/docs/getting_started/index.html
#
from pyats.topology import loader

# load testbed
testbed = loader.load('chapter15_pyats_testbed_1.yml')

# access the device
testbed.devices
ios_1 = testbed.devices['iosv-1']

# establish connectivity
ios_1.connect()

# issue command
print(ios_1.execute('show version'))

# disconnect
ios_1.disconnect()


