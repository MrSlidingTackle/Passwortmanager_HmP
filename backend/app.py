from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

server_url = "http://localhost:3000"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/entry/<id>", methods=['GET'])
def getEntry(id):
    try:
        response = requests.get(f"{server_url}/entry/{id}")

        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": f"Item with id {id} not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500