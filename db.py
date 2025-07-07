import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv("MONGO_URI")

client = MongoClient(uri)
db = client["github_events"]
events_collection = db["events"]
