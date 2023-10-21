import discord
from discord.ext import commands
import requests
import json

class Pricing(commands.Cog, name = "Pricing Cog"):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def price(self, ctx, url = None):
        if url == None:
            await ctx.reply("You must submit a url")
            return
            
        url = url.split("profile")
        url = url[1].replace("/overview", "")
        api_url = f"https://api.tracker.gg/api/v2/rocket-league/standard/profile{url}"

        headers = {"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"}
        r = requests.get(api_url, headers = headers)
        if r.status_code == 403:
            await ctx.send("Api is down, please try again later")
            return
        r = r.json()


    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded Pricing Client")
    

        


def setup(client: commands.Bot):
    client.add_cog(Pricing(client))