from client import client
import discord


@client.message()
async def oof(message: discord.Message):
	if message.content.lower()("oof"):
		try:
			await message.channel.send("rip")
		except:  # that's fine, we don't care
			pass
