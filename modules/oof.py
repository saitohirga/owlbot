from client import client
import discord
import Main


@client.message()
async def oof(message: discord.Message):
    if message.content.lower().endswith("oof"):
        try:
            Main.oofs += 1
            await message.channel.send("rip")
        except:
            pass
