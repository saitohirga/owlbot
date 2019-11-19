from client import client

import discord


cmd_name = "rat"

client.basic_help(title=cmd_name, desc="Has rats been spotted in the caf?.")

detailed_help = {
	"Usage": f"{client.default_prefix}{cmd_name}",
	"Arguments": "None",
	"Description": "Any Rats in the caf?",
	# NO Aliases field, this will be added automatically!
}
client.long_help(cmd=cmd_name, mapping=detailed_help)


@client.command(trigger=cmd_name,
				aliases=[])  # aliases is a list of strs of other triggers for the command
async def command(command: str, message: discord.Message):
	rat = 'No rats spotted in the caf as of today, if this changes DM Saito'
    await message.channel.send(rat)
	return
