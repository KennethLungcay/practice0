from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello WOrld"

@app.route("/<string:name>")
def hello(name):
	return f"Hello,{name}!"