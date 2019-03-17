from client import client
import discord


@client.message()
async def boonk(message: discord.Message):

	htm_boonk = (':regional_indicator_b: '
				 ':regional_indicator_o: '
				 ':regional_indicator_o: '
				 ':regional_indicator_n: '
				 ':regional_indicator_k: ' 
				
				 ':regional_indicator_g: '
				 ':regional_indicator_a: '
				 ':regional_indicator_n: '
				 ':regional_indicator_g:')

	if message.content.lower().endswith("boonk"):
		try:
			await message.channel.send(htm_boonk)
		except:  # that's fine, we don't care
			pass
