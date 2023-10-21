import discord
from discord.ext import commands

class Application(commands.Cog, name = "Events Cog"):
    def __init__(self, client: commands.Bot):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def nuke(self, ctx):
        await ctx.reply("https://media4.giphy.com/media/oe33xf3B50fsc/giphy.gif")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_channel = self.client.get_channel(1045949597824061460)
        await welcome_channel.send(f"Welcome {member.mention} to ARL!")


def setup(client: commands.Bot):
    client.add_cog(Application(client))