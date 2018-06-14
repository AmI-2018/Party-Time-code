
""" Announce as PartyTimeServer """

import logging
import socket
import sys
from time import sleep
from zeroconf import ServiceInfo, Zeroconf
import netifaces as ni


NETWORK_INTERFACE = 'wlp2s0'

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('zeroconf').setLevel(logging.DEBUG)

def get_network_interface_ip_address(interface='eth0'):
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


    desc = {
        'api':'/api/info',
        'welcome': 'hi!!'}
    local_ip_address = get_network_interface_ip_address(NETWORK_INTERFACE)
    #print(local_ip_address)
    info = ServiceInfo("_http._tcp.local.",
                       "Party Time server._http._tcp.local.",
                       socket.inet_aton(local_ip_address), 80, 0, 0,
                       desc, "ash-2.local.")

    '''
    info = ServiceInfo("_http._tcp.local.",
                       "Party Time server._http._tcp.local.",
                       socket.inet_aton("127.0.0.1"), 80, 0, 0,
                       desc, "ash-2.local.")
    '''
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
