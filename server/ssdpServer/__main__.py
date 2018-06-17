from lib.ssdp import SSDPServer
from lib.upnp_http_server import UPNPHTTPServer

import uuid
import netifaces as ni
from time import sleep
import logging

NETWORK_INTERFACE = 'wlp2s0'

#logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)

def setup_debugging():
    """
    Load PyCharm's egg and start a remote debug session.
    :return: None
    """
    import sys
    sys.path.append('/root/pycharm-debug-py3k.egg')
    import pydevd
    pydevd.settrace('192.168.4.47', port=5422, stdoutToServer=True, stderrToServer=True, suspend=False)


#setup_debugging()


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

    device_uuid = uuid.uuid4()
    local_ip_address = get_network_interface_ip_address(NETWORK_INTERFACE)

    http_server = UPNPHTTPServer(8088,
                                 friendly_name="PartyTimeServer",
                                 manufacturer="AMI-PartyTime",
                                 manufacturer_url='https://ami-2018.github.io/Party-Time/index.html',
                                 model_description='PartyTime Server',
                                 model_name="PartyTimeServer",
                                 )
    http_server.start()

    ssdp = SSDPServer()
    ssdp.register
    ssdp.register('local',
                  'uuid:{}::upnp:rootdevice'.format(device_uuid),
                  'upnp:rootdevice',
                  'http://{}:8088/partyTime.xml'.format(local_ip_address))
    ssdp.run()
