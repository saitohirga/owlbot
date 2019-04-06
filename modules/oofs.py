from client import client

import discord
import Main

cmd_name = "oofs"

client.basic_help(title=cmd_name, desc="How many oofs have there been?")

detailed_help = {
	"Usage": f"{client.default_prefix}{cmd_name}",
	"Arguments": "None",
	"Description": "How many oofs have there been??",
	# NO Aliases field, this will be added automatically!
}
client.long_help(cmd=cmd_name, mapping=detailed_help)


@client.command(trigger=cmd_name,
				aliases=[])  # aliases is a list of strs of other triggers for the command
async def command(command: str, message: discord.Message):
	await message.channel.send(Main.oofs)

	return
