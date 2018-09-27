from client import client
import discord
import datetime


cmd_name = "t"
timern = datetime.datetime.now()
client.basic_help(title=cmd_name, desc="Time right now!")

detailed_help = {
	"Usage": f"{client.default_prefix}{cmd_name}",
	"Arguments": "None",
	"Description": "This is what the command does!",
	# NO Aliases field, this will be added automatically!
}
client.long_help(cmd=cmd_name, mapping=detailed_help)


@client.command(trigger=cmd_name,
				aliases=[])  # aliases is a list of strs of other triggers for the command
async def time(command: str, message: discord.Message):
	await message.channel.send(f"Just for you to know the date and time is " + str(timern))
	return



