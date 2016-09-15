from flask import Flask, request
import requests

app = Flask(__name__)

GIPHY_API_KEY = "dc6zaTOxFJmzC"
BOT_ID = "d3822257e9df07545ebfdbbecb"
GIPHY_ENDPOINT = "http://api.giphy.com/v1/gifs/translate"
GROUPME_ENDPOINT = "https://api.groupme.com/v3/bots/post"

@app.route("/", methods=["GET", "POST"])
def send_gif():
	if request.method == "POST":
		text = request.get_json()["text"]

		if text.partition(" ")[0].lower() == "giphy":
			query = text.partition(" ")[2]
			query.replace(" ", "+")

			r = requests.get(GIPHY_ENDPOINT, data = {"api_key": GIPHY_API_KEY, "s" : query})
			gif_url = r.json()["data"]["images"]["downsized_large"]["url"]
			response = gif_url if gif_url != None else "Sorry I could not find a gif for that"

			requests.post(GROUPME_ENDPOINT, data = {"bot_id" : BOT_ID, "text" : response})

	return "gif sent"

if __name__ == "__main__":
	app.run()