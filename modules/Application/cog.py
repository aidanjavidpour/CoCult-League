import discord
from discord.ext import commands
from modules.Application.application import *

class Application(commands.Cog, name = "Application Cog"):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.persistent_views_added = False

    @commands.has_role("Leadership")
    @commands.command()
    async def he(self, ctx):
        view = ApplicationButton()
        await ctx.send("Click this button to start the application process.", view = view)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.persistent_views_added:
            self.client.add_view(ApplicationButton())
            self.persistent_views_added = True

def setup(client: commands.Bot):
    client.add_cog(Application(client))