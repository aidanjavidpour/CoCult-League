import discord
from discord.ext import commands
from youtube_dl.postprocessor import ffmpeg
import urllib
import urllib.request
import re
from youtube_dl import YoutubeDL
import asyncio
from discord.utils import get
import pafy
from discord import Option
from modules.Music.functions import *


is_playing = False
queue = []

class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(0)


class Song():
    def __init__(self, info):
        self.url = info['formats'][0]['url']
        self.song = info['title']
        self.length = info['duration'] + 3

class Music(commands.Cog, name = "Music Bot"):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.queue = Queue()

    @commands.slash_command(guild_ids = [1045897045287907339], description = 'Plays a song!')
    async def play(self, ctx, search: Option(str, "Choose a name the player will be known as.", required = True)):
        if not await in_channel(ctx):
            return
        
        search = search.replace(" ", "+")
        html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={search}")
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        video = f"https://www.youtube.com/watch?v={video_ids[0]}"

        YDL_OPTIONS = {'format': 'bestaudio'}
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(video, download = False)
            self.queue.enqueue(Song(info))



    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded Music client")

def setup(client: commands.Bot):
    client.add_cog(Music(client))