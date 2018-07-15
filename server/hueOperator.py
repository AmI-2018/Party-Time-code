import ssdpDiscover as ssdp
import DBoperator as db
import huerest

"""
!!!!!!IMPORTANT the app need to verify the room names before......
#TODO is needed to set associate the roomname stored in the bridge with the one given by the user......
"""
# probably best choice for the project: https://github.com/quentinsf/qhue

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

        1->red 0
        2->blue 46920
        3->yellow 12750
        4->green 25500
        5->? #TODO add more colorID
        """
        music = db.getCurrentPlayingKind()
        kinds = db.getKindsOfMusic()
        color = {"red":0,"blue":46920,"yellow":12750,"green":25500}
        for i in range (0,3):
            color [i] = kinds[i]
            print(color)
            if music == kinds[i]:
                colorID = color[kinds[i]] #if blue

        code_payload={"bri": 200,
                      "hue": colorID,
                      "on": true}
        """
        bri = 254 is the maximum brightness
        """
post_reply = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers).json()

base_url = 'http://192.168.0.201'

"""
for emulator:
base_url = 'http://localhost:8000'
"""
#username for emulator:
username = 'newdeveloper'
#username must be generated from  https://www.developers.meethue.com/documentation/getting-started
lights_url = base_url + '/api/' + username + '/lights/'
all_the_lights = rest.send(url=lights_url)
kinds = db.getKindsOfMusic()
if type(all_the_lights) is dict:
    # iterate over the Hue lights
    for light in all_the_lights:
        url_to_call = lights_url + light + '/state'
        body = '{ "on" : true, "hue" : colorID }'
        rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
        else:
            print('Error:', all_the_lights[0]['error'])