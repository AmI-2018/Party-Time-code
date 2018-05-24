
from pyestimote.client import EstimoteAPI

"""
Get the beacon for party time by scanning tags
"""
"""
installed packages:
pip install -e https://github.com/michal-michalak/python-estimote
pip install estimote.py

"""

"""
class BEACONcontroller(object):
    def __init__(self, app_id, app_token):
        self.app_id=app_id
        self.app_token=app_token
"""

APP_ID= 'ami---partytime-76u'
APP_TOKEN='98c3dde0c582475f703dab411c3dd435'

class PartyBeacons(object):
    def __init__(self, app_id, app_token):
        self.app_id=app_id
        self.app_token = app_token
        party_beacon = []
        beacon = EstimoteAPI(APP_ID, APP_TOKEN)
        devices = beacon.get_devices().json()
        for device in devices:
            tag = beacon.get_device(device['identifier']).json()['shadow']['tags']
            #print('tag: ', end='')
            #print(tag)
            if len(tag) > 0:
                if tag[0] == 'party-time':
                    #print("arrivato?")
                    #print(device)
                    party_beacon.append(device)
            # if beacon.get_device(device['identifier']).json()['shadow']['tags']=='party-time':
            #    print(beacon.get_device(device['identifier']))
        #for my in party_beacon:
        #    print(my)
        self.party_beacon=party_beacon



    def getDetailsOfBeacons(self):
        return self.party_beacon

"""
def init():
    party_beacon=[]
    beacon=EstimoteAPI(APP_ID, APP_TOKEN)
    devices = beacon.get_devices().json()
    for device in devices:
        tag=beacon.get_device(device['identifier']).json()['shadow']['tags']
        #print('tag: ', end='')
        #print(tag)
        if len(tag)>0:
            if tag[0]=='party-time':
                party_beacon.append(device)
        #if beacon.get_device(device['identifier']).json()['shadow']['tags']=='party-time':
        #    print(beacon.get_device(device['identifier']))
    print(party_beacon)
"""
if __name__ == '__main__':
    mybeacons = PartyBeacons(APP_ID, APP_TOKEN)
    for beacon in mybeacons.getDetailsOfBeacons():
        print(beacon)
    #print(mybeacons.getDetailsOfBeacons())
