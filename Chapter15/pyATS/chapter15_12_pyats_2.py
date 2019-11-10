#!/usr/bin/env python
# 
# from https://devnet-pubhub-site.s3.amazonaws.com/media/pyats/docs/getting_started/index.html
#

from pyats import aetest
import re

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology(self,
                       testbed,
                       iosv1_name = 'iosv-1',
                       nxosv1_name = 'nxosv-1'):
        ios1 = testbed.devices[iosv1_name]
        nxos1 = testbed.devices[nxosv1_name]

        # add them to testscript parameters
        self.parent.parameters.update(ios1 = ios1, nxos1 = nxos1)

        # get corresponding links
        links = ios1.find_links(nxos1)

        assert len(links) >= 1, 'require one link between ios1 and nxos1'


    @aetest.subsection
    def establish_connections(self, steps, ios1):
        with steps.start('Connecting to %s' % ios1.name):
            ios1.connect()


@aetest.loop(device = ('ios1',))
class PingTestcase(aetest.Testcase):

    @aetest.test.loop(destination = ('10.0.0.5', '10.0.0.6'))
    def ping(self, device, destination):
        try:
            result = self.parameters[device].ping(destination)

        except Exception as e:
            self.failed('Ping {} from device {} failed with error: {}'.format(
                                destination,
                                device,
                                str(e),
                            ),
                        goto = ['exit'])
        else:
            match = re.search(r'Success rate is (?P<rate>\d+) percent', result)
            success_rate = match.group('rate')


class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, steps, ios1):
        with steps.start('Disconnecting from %s' % ios1.name):
            ios1.disconnect()


if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',
                        type = loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))

