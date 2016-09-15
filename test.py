from flask import Flask, request
import requests
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
	r = requests.get("http://api.giphy.com/v1/gifs/translate", data = {"api_key": "dc6zaTOxFJmzC", "s" : "south+park"})
	return r.json()["data"]["images"]["original"]["url"]

if __name__ == "__main__":
	app.run()