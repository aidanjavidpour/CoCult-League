async def in_channel(ctx):
    if ctx.author.voice == None:
        await ctx.reply("Please join a voice channel before playing music.", ephemeral = True)
        return False
    
    if ctx.voice_client == None:
        await ctx.author.voice.channel.connect()
    return True