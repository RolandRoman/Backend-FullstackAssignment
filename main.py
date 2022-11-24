from flask import Flask, render_template,request, jsonify
import pymongo
app= Flask(__name__)
client=pymongo.MongoClient("localhost",27017)
db=client.fishapi

@app.route("/api/v1/registrasi",methods=["POST"])
def regis():
    getdata=request.get_json()
    result=db.pond.find({"name":getdata["name"]})
    if result:
        return "Gak Bisa"
    result=db.pond.insert_one(getdata)
    return "OK"

@app.route("/api/v1/pondinfo/<pondname>",methods=["PUT"])
def update(pondname):
    getdata=request.get_json()
    result=db.pond.update_one( {"name":pondname} , { "$set" : getdata})
    return "OK"

# Code buat update data, data terupdate sesuai dengan parameter pondname
@app.route("/api/v1/pondinfo/<pondname>",methods=["PUT"])
def update(pondname):
    getdata=request.get_json()
    result=db.pond.update_one( {"name":pondname} , { "$set" : getdata})
    return "OK"
