from client import client
import discord
import key


@client.message()
async def hunter_irl(message: discord.Message):
	if (message.guild.id == 458765854624972811) and ("uwu" in message.content.lower().replace(" ", "")):
		try:
			await message.add_reaction(discord.utils.find(lambda x: x.id == key.uwu_emoji, message.guild.emojis))
		except:  # thats ok, this is only a fun little joke
			pass

@client.message()
async def ntoskrnl_irl(message: discord.Message):
	if (message.guild.id == 458765854624972811) and "<:ntoskrnl_irl:486325601750351882>" in message.content:
		try:
			await message.add_reaction(discord.utils.find(lambda x: x.id == 459861613197918230, message.guild.emojis))
		except:
			pass
