from client import client

import discord


cmd_name = "phoneticize"

client.basic_help(title=cmd_name, desc="Turns into a phoneticize word.")

detailed_help = {
	"Usage": f"{client.default_prefix}{cmd_name}",
	"Arguments": "letter",
	"Description": "Turns into a phoneticize word.",
	# NO Aliases field, this will be added automatically!
}
client.long_help(cmd=cmd_name, mapping=detailed_help)


@client.command(trigger=cmd_name,
				aliases=["ph"])  # aliases is a list of strs of other triggers for the command
async def command(command: str, message: discord.Message):
	# Awesome stuff happens here!
	return
