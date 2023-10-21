import firebase_admin
from firebase_admin import credentials, firestore
import json

cred = credentials.Certificate("database_creds.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()


with open('player_data.json') as json_file:
    data = json.load(json_file)
    doc_ref = db.collection("users").document("Eth")
    doc_ref.set(data)