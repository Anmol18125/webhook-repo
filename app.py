from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from db import events_collection
from models import parse_event

app = Flask(__name__)
CORS(app)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    event = parse_event(data)
    if event:
        events_collection.insert_one(event)
    return jsonify({"status": "received"}), 200

@app.route("/events", methods=["GET"])
def get_events():
    data = list(events_collection.find({}, {"_id": 0}))
    return jsonify(data)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
