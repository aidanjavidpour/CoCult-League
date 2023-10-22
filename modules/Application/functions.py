import firebase_admin
from firebase_admin import credentials, firestore
import json

cred = credentials.Certificate("database_creds.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

def create_user(name, trackers, discord_id):
    doc_ref = db.collection("users").document(name)
    doc_ref.set({"player_information": {"price": 0, "trackers": trackers, "discord_id": int(discord_id)}, "player_stats": {"games_played": 0, "wins": 0, "goals": 0, "assists": 0, "saves": 0, "shots": 0, "demos_inflicted": 0, "demos_taken": 0}, "team_data": {"team": False, "is_captain": False}})
    return True

def already_registered(id):
    users_ref = db.collection("users")
    docs = users_ref.stream()
    for doc in docs:
        data = doc.to_dict()
        if int(id) == data['player_information']['discord_id']:
            return True
