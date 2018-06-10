from flask import Flask, redirect, url_for, render_template, session, request, jsonify, abort, Response
import json
from collections import  defaultdict
from datetime import datetime

import logging
# from server import DBoperator
import DBoperator

app = Flask(__name__)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


# ---------- REST SERVER ----------
@app.route('/api/pos/update', methods=['POST'])
def fetch_json(item):
    """
    Convert the json in a dictionary
    """
    location = request.json
    print("received location")
    print(location)
    #DBoperator.registerUserPosition()
    pass

@app.route('/api/registerroom', methods=['POST'])
def registerRoom():

    room = request.json
    DBoperator.createRoom(roomName=room["roomName"], raspIP=room["raspIP"], hueID=room["hueIP"], beaconID=room["beaconUUID"], beaconMajor=room["beaconM"], beaconMinor=room["beaconm"])
    return jsonify(room)
    #return Response(status=201)


@app.route('/api/info', methods=['GET'])
def info():
    return Response(status=200)

@app.route('/api/users', methods=['GET'])
def retrieveUsers():
    """Return a json file as Dict<"users":[List of all users]>
        es:
        [
        "users":[
                "tizio",
                "caio",
                "sempronio"
                ]
        ]
    """
    rows = DBoperator.getListOfUsers()
    ret = {"users":[i[0] for i in rows]}
    print("called retrieveUsers @ " + str(datetime.now()))
    return jsonify(ret)

@app.route('/api/users/<username>', methods=['DELETE'])
def removeUser(username):
    """Remove a user by given name"""
    ret = DBoperator.removeUser(username)
    print("called removeUser @ " + str(datetime.now()))
    """TODO: implement response code"""


@app.route('/api/users/<username>', methods=['GET'])
def checkuser(username):
    """Find if user is already registered"""
    print("ore: " + str(datetime.now()))

    if DBoperator.userInDB(username):
        print("Returned 202")
        return Response(status=202) # accepted, is in DB
    print("Returned 204")

    return Response(status=204) # no content

@app.route('/api/pos/allbeacons', methods=['GET'])
def retrieveAllBeacon():
    ret = DBoperator.beaconsList()
    if ret == False:
        return Response(status=204)
    d = list(defaultdict())
    for room, uuid, major, minor in ret:
        d.append({"room":room, "uuid":uuid, "major":major, "minor":minor})
        print("ore: " + str(datetime.now()))

    print("list of all beacons:")
    print({"beacons":d})
    return jsonify({"beacons":d})


@app.route('/api/users/<username>', methods=['POST'])
def adduser(username):

    if DBoperator.userInDB(username):
        print("l'utente risulta gia registrato")
        return Response(status=409)

    preferences = request.json
    print("username=" + username)
    print("pref1=" + preferences['pref1'])
    print("pref2=" + preferences['pref2'])
    print("pref3=" + preferences['pref3'])

    DBoperator.createUser(username, preferences['pref1'], preferences['pref2'], preferences['pref3'])
    return jsonify(preferences)
    #return Response(status=201)

@app.route('/api/music/kind', methods=['GET'])
def getKindsOfMusic():
    """Return a List object for every kind of music"""
    kinds = DBoperator.getKindsOfMusic()
    return jsonify(kinds)

@app.route('/api/music/kindAndCount', methods=['GET'])
def getKindsOfMusicAndCount():
    """Return a List object for every kind of music"""
    kinds = DBoperator.getKindsOfMusicAndCount()
    ret = dict(kinds)
    print("ore: " + str(datetime.now()))
    print(ret)
    print(type(ret))

    return jsonify(ret)


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
    # print(retrieveUsers)
    # print(DBoperator.getListOfUsers())
