from client import client
import discord
oofs = 0

@client.message()
async def oof(message: discord.Message):
    if message.content.lower().endswith("oof"):
        try:
            oof.oofs += 1
            await message.channel.send("rip")
        except:
            pass
