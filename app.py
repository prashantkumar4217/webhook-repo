from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://prashantkumar7124:a4NEd6sCRMCfRx7L@clusterdemo.tccscoh.mongodb.net/?retryWrites=true&w=majority&appName=ClusterDemo"
client = MongoClient(MONGO_URI)

# Select database and collection
db = client.webhookdb
events_collection = db.events


@app.route('/webhook/receiver', methods=['POST'])
def webhook_receiver():
    """
    Receives GitHub webhook events. Stores only merged pull requests.
    """
    event = request.get_json()

    if not event:
        return jsonify({"error": "Invalid JSON payload"}), 400

    event_type = request.headers.get("X-GitHub-Event")
    if event_type == "pull_request":
        action = event.get("action")
        pr = event.get("pull_request", {})
        
        if action == "closed" and pr.get("merged"):
            merged_event = {
                "event_type": "pull_request_merged",
                "repo": event.get("repository", {}).get("full_name"),
                "title": pr.get("title"),
                "author": pr.get("user", {}).get("login"),
                "merged_by": pr.get("merged_by", {}).get("login"),
                "merged_at": pr.get("merged_at"),
                "url": pr.get("html_url"),
                "timestamp": datetime.utcnow().isoformat()
            }

            events_collection.insert_one(merged_event)
            return jsonify({"status": "Merged PR stored"}), 200

    return jsonify({"status": "Ignored (not a merged PR)"}), 200


@app.route('/events', methods=['GET'])
def get_events():
    """
    Returns all stored merged PR events.
    """
    events = list(events_collection.find({}, {'_id': 0}))
    return jsonify(events), 200


@app.route('/')
def index():
    """
    Renders the homepage with event listing.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

