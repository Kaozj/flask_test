from flask import Flask

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")
def hello_world():
	return "hello world"

@app.route("/test/<param>")
def search(param):
	return param

@app.route("/name/<name>")
def index(name):
	if name.lower == "mike":
		return "hello,{}".format(name)
	else:
		return "not found", 404

if __name__ == "__main__":
	app.run()

