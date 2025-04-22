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

@app.route("/login", methods=["GET","POST"])
def register():
    if request.method == "POST":
        try:
            data = request.get_json()
            query_stmt = f"INSERT INTO user (user, passwort, isAdmin) VALUES ('{data["username"]}', '{data["passwort"]}', '0')"
            db.session.execute(text(query_stmt))
            db.session.commit()
            # print(request.get_json())
            # response = requests.post(f"{server_url}/login", json=request.get_json())

            if query_stmt:
                return {"message": "done"}, 200
            else:
                return jsonify({"error": f"Something went wrong!"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    if request.method == "GET":
        try:
            query_stmt = f"SELECT * FROM user"
            result = db.session.execute(text(query_stmt))
            users = result.fetchall()

            user_list = [dict(row._mapping) for row in users]

            # response = requests.get(f"{server_url}/login?username={username}&passwort={passwort}")

            if users:
                return jsonify(user_list), 200
            else:
                return jsonify({"error": f"Something went wrong!"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route("/login/<username>/<passwort>", methods=["GET", "OPTIONS"])
def checkLogin(username, passwort):
    if request.method == "OPTIONS":
        return '', 204  # Preflight OK
    
    try:
        query_stmt = f"SELECT * FROM user WHERE user='{username}' AND passwort='{passwort}'"
        print("haha1")
        result = db.session.execute(text(query_stmt))
        print("haha2")
        user = result.fetchall()
        print("haha3")

        # response = requests.get(f"{server_url}/login?username={username}&passwort={passwort}")

        if user:
            return {'id': user[0][0], 'user': user[0][1], 'passwort': user[0][2], 'isAdmin': user[0][3]}, 200
        else:
            return jsonify({"error": f"Something went wrong!"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/entry", methods=['GET', 'POST'])
def getAllEntries():
    if request.method == "GET":
        try:
            query_stmt = f"SELECT * FROM entry"
            result = db.session.execute(text(query_stmt))
            entries = result.fetchall()
            #response = requests.get(f"{server_url}/entry")

            if entries:
                entrylist = []
                for entry in entries:
                    item = {'id':entry[0], 'name':entry[1], 'username':entry[2], 'url':entry[3], 'passwort':entry[4], 'farbe':entry[5], 'created':entry[6], 'ownerId':entry[7]}
                    entrylist.append(item)
                
                return jsonify(entrylist), 200
            else:
                return jsonify({"error": f"Something went wrong!"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "POST":
        try:
            entry = request.get_json()
            query_stmt = f"INSERT INTO entry (name, username, url, passwort, farbe, created, ownerId) VALUES ('{entry["name"]}', '{entry["username"]}', '{entry["url"]}', '{entry["passwort"]}', '{entry["farbe"]}', '{entry["created"]}', {entry["ownerId"]})"
            db.session.execute(text(query_stmt))
            db.session.commit()
            #response = requests.post(f"{server_url}/entry", json=request.get_json())

            if query_stmt:
                return {"message":"Entry created"}, 200
            else:
                return jsonify({"error": f"Something went wrong!"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@app.route("/entry/<id>", methods=['GET', 'PUT', 'DELETE'])
def getEntry(id):
    if request.method == "GET":
        try:
            query_stmt = f"SELECT * FROM entry WHERE id='{id}'"
            result = db.session.execute(text(query_stmt))
            entry = result.fetchall()
            #response = requests.get(f"{server_url}/entry/{id}")

            if entry:
                return {'id':entry[0][0], 'name':entry[0][1], 'username':entry[0][2], 'url':entry[0][3], 'passwort':entry[0][4], 'farbe':entry[0][5], 'created':entry[0][6], 'ownerId':entry[0][7]}, 200
            else:
                return jsonify({"error": f"Item with id {id} not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "PUT":
        try:
            data = request.get_json()
            query_stmt = f"UPDATE entry SET name='{data["name"]}', username='{data["username"]}', url='{data["url"]}', passwort='{data["passwort"]}', farbe='{data["farbe"]}', created='{data["created"]}' WHERE id='{id}'"
            db.session.execute(text(query_stmt))
            db.session.commit()

            # Forward the data to the actual backend (if using a separate service)
            #response = requests.put(f"{server_url}/entry/{id}", json=data)

            if query_stmt:
                return {"message":"done"}, 200
            else:
                return jsonify({"error": "Failed to update entry"}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "DELETE":
        try:
            query_stmt = f"DELETE FROM entry WHERE id='{id}'"
            db.session.execute(text(query_stmt))
            db.session.commit()
            #response = requests.delete(f"{server_url}/entry/{id}")

            if id:
                return "Entry deleted", 200
            else:
                return jsonify({"error": f"Item with id {id} not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500