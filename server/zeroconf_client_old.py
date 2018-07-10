#!/usr/bin/env python3

""" Example of resolving a service with a known name """

import logging
import sys
import socket

from zeroconf import Zeroconf

TYPE = '_http._tcp.local.'
NAME = 'PartyTimeServer'

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG)
#     if len(sys.argv) > 1:
#         assert sys.argv[1:] == ['--debug']
#         logging.getLogger('zeroconf').setLevel(logging.DEBUG)
#
#     zeroconf = Zeroconf()
#
#     try:
#         # print(zeroconf.get_service_info(TYPE,""))
#         print(zeroconf.get_service_info(TYPE, NAME + '.' + TYPE))
#         res = zeroconf.get_service_info(TYPE, NAME + '.' + TYPE)
#         print(socket.inet_ntoa(res.address))
#         serverAddress = socket.inet_ntoa(res.address)
#     finally:
#         zeroconf.close()

def findClient(clientID):
    zeroconf = Zeroconf()
    try:
        print("entrato")
        lis = zeroconf.listener()

        print(zeroconf.listener)
        print(zeroconf.get_service_info(type_="_http._tcp.local.", name="PartyTimeServer._http._tcp.local."))
        # print(zeroconf.get_service_info(TYPE, clientID + '.' + TYPE))
        #res = zeroconf.get_service_info(TYPE, clientID + '.' + TYPE)
        #print(socket.inet_ntoa(res.address))
        #serverAddress = socket.inet_ntoa(res.address)
        #return serverAddress
    finally:
        zeroconf.close()

if __name__ == '__main__':
    findClient("PTserver")
