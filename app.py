from flask import Flask 

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/home")
def home():
    return "This is homepage"

from controller import *

     


