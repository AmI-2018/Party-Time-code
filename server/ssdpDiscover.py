
import socket
import http.client
import io

class SSDPResponse(object):
    class _FakeSocket(io.BytesIO):
        def makefile(self, *args, **kw):
            return self
    def __init__(self, response):
        r = http.client.HTTPResponse(self._FakeSocket(response))
        r.begin()
        self.location = r.getheader("location")
        self.usn = r.getheader("usn")
        self.st = r.getheader("st")
        self.cache = r.getheader("cache-control").split("=")[1]
    def __repr__(self):
        return "<SSDPResponse({location}, {st}, {usn})>".format(**self.__dict__)

def discover(service, timeout=5, retries=1, mx=3):
    group = ("239.255.255.250", 1900)
    message = "\r\n".join([
        'M-SEARCH * HTTP/1.1',
        'HOST: {0}:{1}',
        'MAN: "ssdp:discover"',
        'ST: {st}','MX: {mx}','',''])
    socket.setdefaulttimeout(timeout)
    responses = {}
    for _ in range(retries):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
        message_bytes = message.format(*group, st=service, mx=mx).encode('utf-8')
        sock.sendto(message_bytes, group)
        while True:
            try:
                response = SSDPResponse(sock.recv(1024))
                responses[response.location] = response
            except socket.timeout:
                break
    return list(responses.values())
