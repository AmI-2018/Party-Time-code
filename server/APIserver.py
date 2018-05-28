app = Flask(__name__)

import logging

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
    DB.registerUser()

@app.route('/api/user/<username>', methods=['POST'])
def adduser(username):
    if DB.userInDB(username):
        return "user already in DB"

    preferences=request.json
    print("pref1=" + preferences['pref1'])
    print("pref2=" + preferences['pref2'])
    print("pref3=" + preferences['pref3'])






if __name__ == '__main__':
    app.run()