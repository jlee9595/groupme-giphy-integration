from flask import Flask, request
import requests
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		request_data = request.get_json()
		if request_data["text"].partition(" ")[0].lower() == "giphy":
			query = request_data["text"].partition(" ")[2]
			query.replace(" ", "+")
			r = requests.get("http://api.giphy.com/v1/gifs/translate", data = {"api_key": "dc6zaTOxFJmzC", "s" : query})
			gif_url = r.json()["data"]["images"]["original"]["url"]
			requests.post("https://api.groupme.com/v3/bots/post", data = {"bot_id" : "d3822257e9df07545ebfdbbecb", "text" : gif_url})
	return "Hello World!"

if __name__ == "__main__":
	app.run()