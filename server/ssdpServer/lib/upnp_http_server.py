from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

PORT_NUMBER = 8080


class UPNPHTTPServerHandler(BaseHTTPRequestHandler):
    """
    A HTTP handler that serves the UPnP XML files.
    """

    # Handler for the GET requests
    def do_GET(self):


        if self.path == '/partyTime.xml':
            self.send_response(200)
            self.send_header('Content-type', 'application/xml')
            self.end_headers()
            self.wfile.write(self.get_server_xml().encode())
            return
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("Not found.")
            return

    def get_server_xml(self):
        """
        Get the main device descriptor xml file.
        """

        xml = """<root>
    <specVersion>
        <major>1</major>
        <minor>0</minor>
    </specVersion>
    <device>
        <friendlyName>{friendly_name}</friendlyName>
        <manufacturer>{manufacturer}</manufacturer>
        <modelDescription>{model_description}</modelDescription>
        <modelName>{model_name}</modelName>
        <serviceList>
            <service>
                <URLBase>http://xxx.yyy.zzz.aaaa:5000</URLBase>
                <serviceType>urn:boucherie.example.com:service:Jambon:1</serviceType>
               <controlURL>/partytime</controlURL>
                <eventSubURL/>
                <SCPDURL>/partytime.xml</SCPDURL>
            </service>
        </serviceList>
    </device>
</root>"""
        return xml.format(friendly_name=self.server.friendly_name,
                          manufacturer=self.server.manufacturer,
                          manufacturer_url=self.server.manufacturer_url,
                          model_description=self.server.model_description,
                          model_name=self.server.model_name)



class UPNPHTTPServerBase(HTTPServer):
    """
    A simple HTTP server that knows the information about a UPnP device.
    """
    def __init__(self, server_address, request_handler_class):
        HTTPServer.__init__(self, server_address, request_handler_class)
        self.port = None
        self.friendly_name = None
        self.manufacturer = None
        self.manufacturer_url = None
        self.model_description = None
        self.model_name = None


class UPNPHTTPServer(threading.Thread):
    """
    A thread that runs UPNPHTTPServerBase.
    """

    def __init__(self, port, friendly_name, manufacturer, manufacturer_url, model_description, model_name):
        threading.Thread.__init__(self, daemon=True)
        self.server = UPNPHTTPServerBase(('', port), UPNPHTTPServerHandler)
        self.server.port = port
        self.server.friendly_name = friendly_name
        self.server.manufacturer = manufacturer
        self.server.manufacturer_url = manufacturer_url
        self.server.model_description = model_description
        self.server.model_name = model_name

    def run(self):
        self.server.serve_forever()
