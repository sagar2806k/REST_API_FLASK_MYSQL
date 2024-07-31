from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask App!"

@app.route("/Home")
def home():
    return "You are at the Home Page!"
from controller import *
# import controller.controller as controller
# import controller.product_controller as product_controller