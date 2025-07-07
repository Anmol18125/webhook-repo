from pymongo import MongoClient

# Securely connect to MongoDB Atlas
uri = "mongodb+srv://rai836848:qB17eMHxEoYdwGQ6@cluster0.icecvve.mongodb.net/github_events?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["github_events"]
events_collection = db["events"]
