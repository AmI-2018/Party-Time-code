import ssdpDiscover as ssdp

"""
!!!!!!IMPORTANT the app need to verify the room names before......
#TODO is needed to set associate the roomname stored in the bridge with the one given by the user......
"""
# probably best choise for the project: https://github.com/quentinsf/qhue

if __name__ == '__main__':
    #bridge = ssdp.discover("Philips HUE")
    server = ssdp.discover("PartyTimeServer")
    #print(bridge)
    print("server: " + str(server))
class hueOperator(object):
    """use this class to control and set hue lights and color"""
    def __init__(self):
        super(hueOperator, self).__init__()
        bridge = ssdp.discover("Philips HUE")


    def setColor(self, roomName="", colorID=-1):
        """
        this function will set the color by id to a given room (by its name):

        1->red
        2->blue
        3->yellow
        4->green
        5->? #TODO add more colorID
        """
        code_payload={"bri": 254,
                      "hue": colorID,
                      "on": true}
        """
        bri = 254 is the maximum brightness
        """
post_reply = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers).json()
