from flask import Flask, jsonify, abort, request, Response, render_template
import server.DBoperator as DB

app = Flask(__name__)

# ---------- REST SERVER ----------
@app.route('/api/pos/update', methods=['POST'])
def fetch_json(item):
    """
    Convert the json in a dictionary
    """
    DB.registerUser()

if __name__ == '__main__':
    app.run()