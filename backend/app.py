from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import requests

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://avnadmin:AVNS_y5YcZGtAw5mIy0FBNES@pwmanager-pwmanager-1.h.aivencloud.com:25975/defaultdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#hallo
db = SQLAlchemy(app)

server_url = "http://localhost:3000"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["POST"])
def register():
    if request.method == "POST":
        try:
            print(request.get_json())
            response = requests.post(f"{server_url}/login", json=request.get_json())

            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({"error": f"Something went wrong!"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route("/login/<username>/<passwort>", methods=["GET", "OPTIONS"])
def checkLogin(username, passwort):
    if request.method == "OPTIONS":
        return '', 204  # Preflight OK
    
    try:
        response = requests.get(f"{server_url}/login?username={username}&passwort={passwort}")

        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": f"Something went wrong!"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/entry", methods=['GET', 'POST'])
def getAllEntries():
    if request.method == "GET":
        try:
            response = requests.get(f"{server_url}/entry")

            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({"error": f"Something went wrong!"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "POST":
        try:
            print(request.get_json())
            response = requests.post(f"{server_url}/entry", json=request.get_json())

            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({"error": f"Something went wrong!"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@app.route("/entry/<id>", methods=['GET', 'PUT', 'DELETE'])
def getEntry(id):
    if request.method == "GET":
        try:
            response = requests.get(f"{server_url}/entry/{id}")

            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({"error": f"Item with id {id} not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "PUT":
        try:
            data = request.get_json()
            print(f"Received PUT for ID {id}:", data)  # Debugging

            # Forward the data to the actual backend (if using a separate service)
            response = requests.put(f"{server_url}/entry/{id}", json=data)

            if response.status_code in [200, 204]:
                return jsonify({"message": "Entry updated successfully"}), 200
            else:
                return jsonify({"error": "Failed to update entry"}), response.status_code
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "DELETE":
        try:
            response = requests.delete(f"{server_url}/entry/{id}")

            if response.status_code == 200:
                return jsonify(response.json()), 200
            else:
                return jsonify({"error": f"Item with id {id} not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500