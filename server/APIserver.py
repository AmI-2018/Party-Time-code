from flask import Flask, redirect, url_for, render_template, session, request, jsonify, abort, Response
import json
import logging
from server import DBoperator

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
    DBoperator.registerUser()


@app.route('/info', methods=['GET'])
def info():
    return "funziona"

@app.route('/api/users', methods=['GET'])
def retrieveUsers():
    pass

@app.route('/api/users/<username>', methods=['POST'])
def adduser(username):
    if DBoperator.userInDB(username):
        return Response(status=409)

    preferences = request.json
    print("pref1=" + preferences['pref1'])
    print("pref2=" + preferences['pref2'])
    print("pref3=" + preferences['pref3'])

    DBoperator.createUser(username, preferences['pref1'], preferences['pref2'], preferences['pref3'])
    return Response(status=201)

@app.route('/api/music/kind', methods=['GET'])
def getKindsOfMusic():
    kinds = DBoperator.getKindsOfMusic()
    print(kinds)
    return jsonify(kinds)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
