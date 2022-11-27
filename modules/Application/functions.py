import json

filename = "player_data.json"

def load_dict():
    with open(filename, "r") as file:
        data = json.load(file)
        return data

def user_exist(user):
    if user in load_dict():
        return True



def create_user(name, trackers, region, user_id):
    # price = price_player(trackers) # NEED TO FIX
    price = False

    data = load_dict()
    with open(filename, 'w') as file:
        data[name] = {"player_information": {"price": price, "trackers": trackers, "region": region, "user_id": user_id}, "player_stats": {"games_played": 0, "wins": 0, "goals": 0, "assists": 0, "saves": 0, "shots": 0, "demos_inflicted": 0, "demos_taken": 0}, "team_data": {"team": False, "is_captain": False}}
        json.dump(data, file, indent = 4)

user_exist("Eth")