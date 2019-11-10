from client import client
import discord
import modules.noofs

@client.message()
async def oof(message: discord.Message):
    if message.content.lower().endswith("oof"):
        try:
            modules.noofs.oofs += 1
            await message.channel.send("rip")
        except:
            pass
