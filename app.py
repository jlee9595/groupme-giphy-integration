from flask import Flask, request
import requests
app = Flask(__name__)

@app.route("/")
def hello():
	requests.post("https://api.groupme.com/v3/bots/post", data = {"bot_id" : "d3822257e9df07545ebfdbbecb", "text" : "https://media.giphy.com/media/14k2L68sg1rVZu/giphy.gif"})
	return "Hello World!"

if __name__ == "__main__":
	app.run()