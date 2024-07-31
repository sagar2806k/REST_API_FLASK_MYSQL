from app import app
from model.user_model import user_model
from flask import request
obj = user_model()

#### GET Method #####

@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()

#### POST Method ####

@app.route("/user/addone",methods=["POST"])
def user_addone_controller():
    return obj.user_addone_model(request.form)  

#### PUT(UPDATE) Method ####

@app.route("/user/update",methods=["PUT"])
def user_update_controller():
    return obj.user_update_model(request.form)  

#### DELETE Method ####

@app.route("/user/delete/<ID>",methods=["DELETE"])
def user_delete_controller(ID):
    return obj.user_delete_model(ID)
