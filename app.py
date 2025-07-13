from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# Connect to MongoDB using environment variable
client = MongoClient(os.getenv("MONGO_URI"))
db = client.github_events
collection = db.events

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')

    if event_type == "push":
        author = data['pusher']['name']
        to_branch = data['ref'].split('/')[-1]
        timestamp = datetime.utcnow().isoformat()
        collection.insert_one({
            "type": "push",
            "author": author,
            "to_branch": to_branch,
            "timestamp": timestamp
        })

    elif event_type == "pull_request":
        action = data['action']
        author = data['pull_request']['user']['login']
        from_branch = data['pull_request']['head']['ref']
        to_branch = data['pull_request']['base']['ref']
        timestamp = datetime.utcnow().isoformat()

        if action == "opened":
            collection.insert_one({
                "type": "pull_request",
                "author": author,
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            })
        elif action == "closed" and data['pull_request']['merged']:
            collection.insert_one({
                "type": "merge",
                "author": author,
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            })

    return '', 204

@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find().sort("_id", -1).limit(10))
    for e in events:
        e['_id'] = str(e['_id'])  # Convert ObjectId to string
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
