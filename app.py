from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://prashantkumar7124:a4NEd6sCRMCfRx7L@clusterdemo.tccscoh.mongodb.net/?retryWrites=true&w=majority&appName=ClusterDemo"
client = MongoClient(MONGO_URI)

# Select database and collection
db = client.webhookdb
events_collection = db.events

@app.route('/events', methods=['GET'])
def get_events():
    events = list(events_collection.find({}, {'_id': 0}))  # exclude MongoDB _id field
    return jsonify(events), 200

@app.route('/webhook/receiver', methods=['POST'])
def webhook_receiver():
    event = request.get_json()
    if not event:
        return jsonify({"error": "Invalid payload"}), 400

    events_collection.insert_one(event)
    return jsonify({"status": "Event received"}), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

