import requests
import json
import asyncio


class Ballchasing():
    def __init__(self, league, week, team1, team2, channel):
        self.league = league
        self.week = week
        self.team1 = team1
        self.team2 = team2
        self.channel = channel
        self.create_group_url = "https://ballchasing.com/api/groups"
        self.replay_url = "https://ballchasing.com/api/replays/"
        self.group = {"name": f"Week {self.week} {self.league} - {self.team1} vs {self.team2}", "player_identification": "by-id", "team_identification": "by-player-clusters"}
        with open('modules/Uploader/ballchasing-token.txt', 'r') as token: self.bc_token = token.read()

    async def create_group(self):
        try:
            r = requests.post(self.create_group_url, headers = {'Authorization': self.bc_token}, data = json.dumps(self.group))
            self.group_id = r.json()['id']
            self.upload_url = f'https://ballchasing.com/api/v2/upload?group={self.group_id}'
        except:
            return False
    async def upload_file(self, file):
        replay = {'file': open(f"modules/Uploader/replays/{file}", 'rb')}
        r = requests.post(self.upload_url, headers = {'Authorization': self.bc_token}, files = replay)
        if r.status_code == 409:
            await self.channel.send("This replay is already in our system. This means you have already sent it or someone has already uploaded the replay. If this is a mistake, please contact Eth or a member on Management.")
        elif r.status_code == 201:
            # await self.get_file(r.json()['id'])
            pass

    async def get_file(self, id):
        get_replay_url = self.replay_url + id
        r = requests.get(get_replay_url, headers = {'Authorization': self.bc_token, 'Content-Type': 'application/json'}) # get replay

        if r.status_code == 200:
            x = 0
            while r.json()['status'] == 'pending':
                x += 1
                await asyncio.sleep(1)
                r = requests.get(get_replay_url, headers = {'Authorization': self.bc_token, 'Content-Type': 'application/json'})
                if x == 20:
                    await self.channel.send("Could not get the game. If this is an issue, please contact Eth or a member on Management")
                    return
        
        await self.read_file(r.json())
    
    async def read_file(self, data):
        with open('z.json', 'w') as file:
            json.dump(data, file, indent = 4)
        
        blue_team = []
        orange_team = []

        
        

