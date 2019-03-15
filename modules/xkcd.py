from client import client

import discord


cmd_name = "x"

client.basic_help(title=cmd_name, desc="Pulls up a xkcd.")

detailed_help = {
	"Usage": f"{client.default_prefix}{cmd_name}",
	"Arguments": "None",
	"Description": "Pulls up a xkcd, all you need is a number!",
	# NO Aliases field, this will be added automatically!
}
client.long_help(cmd=cmd_name, mapping=detailed_help)


@client.command(trigger=cmd_name,
				aliases=[])  # aliases is a list of strs of other triggers for the command
async def command(command: str, message: discord.Message):
    wo = ''
    discord.Message.strip = wo
    num = wo.replace("x", "")
    await message.channel.send('http://xkcd.com/' + num )

    return


