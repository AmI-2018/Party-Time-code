#!/usr/bin/env python3

""" Example of announcing a service (in this case, a fake HTTP server) """

import logging
import socket
import sys
from time import sleep
import netifaces as ni
from zeroconf import ServiceInfo, Zeroconf

NETWORK_INTERFACE='wlp2s0'

def get_network_interface_ip_address(interface='wlp2s0'):
    """
    Get the first IP address of a network interface.
    :param interface: The name of the interface.
    :return: The IP address.
    """
    while True:
        if NETWORK_INTERFACE not in ni.interfaces():
            logger.error('Could not find interface %s.' % (interface,))
            exit(1)
        interface = ni.ifaddresses(interface)
        if (2 not in interface) or (len(interface[2]) == 0):
            logger.warning('Could not find IP of interface %s. Sleeping.' % (interface,))
            sleep(60)
            continue
        return interface[2][0]['addr']


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    if len(sys.argv) > 1:
        assert sys.argv[1:] == ['--debug']
        logging.getLogger('zeroconf').setLevel(logging.DEBUG)

    local_ip_address = get_network_interface_ip_address(NETWORK_INTERFACE)
    desc = {
        'api':'/api/info',
        'welcome': 'hi!!'
        }
    '''
                       type_="_http._tcp.local.",
                       name="PartyTimeServer._http._tcp.local.",
                       address=socket.inet_aton(str(local_ip_address)),
                       port=80,
                       weight=0,
                       priority=0,
                       properties=desc,
                       server=str(local_ip_address)
    '''
    info = ServiceInfo(type_="_http._tcp.local.",
                       name="PartyTimeServer._http._tcp.local.",
                       address=socket.inet_aton(str(local_ip_address)),
                       port=80,
                       weight=0,
                       priority=0,
                       properties=desc,
                       server="partytimeserver.local."
                       )

    zeroconf = Zeroconf()
    print("Registration of a service, press Ctrl-C to exit...")
    zeroconf.register_service(info)
    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Unregistering...")
        zeroconf.unregister_service(info)
zeroconf.close()
