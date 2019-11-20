from client import client

import discord
import datetime
from time import gmtime, strftime

cmd_name = "rat"

client.basic_help(title=cmd_name, desc="Has rats been spotted in the caf?.")

detailed_help = {
    "Usage": f"{client.default_prefix}{cmd_name}",
    "Arguments": "None",
    "Description": "Any Rats in the caf?",
    # NO Aliases field, this will be added automatically!
}
client.long_help(cmd=cmd_name, mapping=detailed_help)

datetimeFormat = '%Y-%m-%d %H:%M:%S'
date2 = '2019-11-18 12:25:34'
date1 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
diff = datetime.datetime.strptime(date1, datetimeFormat) - datetime.datetime.strptime(date2, datetimeFormat)

@client.command(trigger=cmd_name,
                aliases=[])  # aliases is a list of strs of other triggers for the command
async def rat(command: str, message: discord.Message):
    rats = f"No rats spotted in the caf as of today, if this changes DM Saito, time since last seen {diff}"
    await message.channel.send(rats)
    return
