
from client import client
import discord

@client.message()
async def oof(message: discord.Message):
    if message.content.lower().endswith("ara ara"):
        try:
            await message.channel.send("https://steamuserimages-a.akamaihd.net/ugc/928174091350767352/781BA205BF32A445ABA7993EF7F16751F2B9E312/")
        except:
            pass
