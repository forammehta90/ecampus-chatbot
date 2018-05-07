
# eCampus ChatBot

The purpose of this application is to create a chatbot that will answer to any ecampus
website visitor to ask questions/doubts about any ecampus supported tool.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Technology Stack

```
Python3
Virtualenv
MongoDb
Slack Client
Chatlio client
```

### Steps

1. Download all the files from github.

2. Create a Slack Channel and add a "bot application" to the channel.

3. Store the "SLACK_BOT_TOKEN" and "bot_id" in the profile and export.

4. Create a Chatlio account and add the Slack Bot to the chatlio account.

5. Install MongoDB on local and restore the dump. Command is mentioned below.

6. Run ecampusbot.py This will run the server.

```
python ecampusbot.py
```
5 . Once the server is up and running, double click on webpage_chatlio.html. This will open the chatbot and ask questions to the bot.


## MongoDB dump restore

Run mongorestore from the system command line, not the mongo shell.

```
mongorestore
```
