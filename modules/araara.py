
from client import client
import discord

@client.message()
async def oof(message: discord.Message):
    if message.content.lower().endswith("ara ara"):
        try:
            await message.channel.send("http://giphygifs.s3.amazonaws.com/media/4SSj1rY2T1Eju/giphy.gif")
        except:
            pass
