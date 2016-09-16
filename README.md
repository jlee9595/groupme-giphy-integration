# groupme-giphy-integration
Integration of Giphy into GroupMe via a chatbot

![Screenshot](https://cloud.githubusercontent.com/assets/14844924/18571199/97ae8232-7b7e-11e6-9996-60a0a3638d6f.png)

This project adds Giphy functionality to GroupMe similar to the integrations provided in other messaging apps like Slack and HipChat. This is achieved by adding a [bot](https://dev.groupme.com/tutorials/bots) to your group and linking it to a server that queries Giphy's search API.

##Prerequisites:
- Python 2.5+
- A Heroku account (there is a free option that will suffice for this application) for hosting
- A GroupMe account (and a group to put the integration in)

##To use:
1. Log into GroupMe on your computer and fill out [this form](https://dev.groupme.com/bots/new) to create your bot, leaving the callback url blank for now. Note the bot-id given after you submit the form, you will need this later.
2. Install the [Heroku Command Line Interface](https://devcenter.heroku.com/articles/heroku-command-line#download-and-install)
3. `heroku login`
4. `git clone https://github.com/jlee9595/groupme-giphy-integration.git`
5. `cd groupme-giphy-integration`
6. Edit app.py and change BOT_ID to your bot's id and commit the change
7. `heroku create` ** Note the url ending in herokuapp.com in the output, you will need this later
8. `git push heroku master`
9. Go to your bot list [here](https://dev.groupme.com/bots), edit your bot and put the url from earlier (ending in herokuapp.com) as the callback URL.
