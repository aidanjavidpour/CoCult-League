# import firebase_admin
# from firebase_admin import credentials, firestore
# import json

# cred = credentials.Certificate("database_creds.json")
# app = firebase_admin.initialize_app(cred)
# db = firestore.client()


# users_ref = db.collection("users")
# docs = users_ref.stream()
# for doc in docs:
#     data = doc.to_dict()
#     print(data['player_information']['discord_id'])
#     break