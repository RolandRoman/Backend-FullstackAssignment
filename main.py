from flask import Flask, request, jsonify
import pymongo
app = Flask(__name__)
client = pymongo.MongoClient("localhost", 27017)
db = client.fishapi

@app.route("/api/v1/registrasi", methods=["POST"])
def register():
    getdata = request.get_json()
    result = db.pond.find({"name": getdata["name"]})
    if result:
        return "Name already exists."
    result = db.pond.insert_one(getdata)
    return "OK"

@app.route("/api/v1/pondinfo", methods=["GET"])
def ponds_info():
    datas = db.pond.find({}, {"_id": 0})
    return jsonify([data for data in datas])

# Code buat update data, data terupdate sesuai dengan parameter pondname
@app.route("/api/v1/pondinfo/<pondname>", methods=["PUT"])
def update(pondname):
    getdata = request.get_json()
    result = db.pond.update_one({"name": pondname}, {"$set": getdata})
    return "OK"

@app.route("/api/v1/pondinfo/<name>", methods=["GET"])
def pond_info(name):
    datas = db.pond.find({"name": name}, {"_id": 0})
    return jsonify([data for data in datas])
