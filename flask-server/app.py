# save this as app.py
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
@app.route("/crops")

def crops():
    return "Crops are cool"

def hello():
    return "Hello, World!"  