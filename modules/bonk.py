from client import client
import discord


@client.message()
async def bonk(message: discord.Message):

	htm_bonk = (':regional_indicator_b: '
				':regional_indicator_o: '
				':regional_indicator_n: '
				':regional_indicator_k:')

	if message.content.lower().endswith("bonk"):
		try:
			await message.channel.send(htm_bonk)
		except:  # that's fine, we don't care
			pass
