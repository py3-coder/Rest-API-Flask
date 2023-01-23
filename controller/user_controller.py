from app import app
from model.user_model import user_model
from flask import request

obj = user_model()

@app.route("/user/getall",methods=['GET'])
def getall_controller():
    return obj.user_getall_model()

@app.route("/user/add",methods=["POST"])
def addone_controller():
    return obj.user_addone_model(request.form)


@app.route("/user/addmultiple", methods=["POST"])
def add_multiple_users():
    return obj.add_multiple_users_model(request.json)


 
