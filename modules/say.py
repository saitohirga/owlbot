from client import client
import discord

cmd_name = "talk"


@client.command(trigger=cmd_name,
                aliases=["say"])  # aliases is a list of strs of other triggers for the command
async def command(command: str, msg: discord.Message):
    a1 = command.split(" ", 2)
    ch_idstr = a1[1]
    text = a1[2]

    daddyid = int(ch_idstr)

    channel = client.get_channel(daddyid)

    if channel is not None:  # and msg.author.id(195582200270290944):
        await channel.send(text)
    else:
        raise TypeError("Invalid or non-existant channel ID (Not a text channel? Vars are", daddyid, text)
