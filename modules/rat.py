from client import client

import discord
import datetime


cmd_name = "rat"

client.basic_help(title=cmd_name, desc="Has rats been spotted in the caf?.")

detailed_help = {
    "Usage": f"{client.default_prefix}{cmd_name}",
    "Arguments": "None",
    "Description": "Any Rats in the caf?",
    # NO Aliases field, this will be added automatically!
}
client.long_help(cmd=cmd_name, mapping=detailed_help)

datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
date1 = '2016-04-16 10:01:28.585'
date2 = '2016-03-10 09:56:28.067'
diff = datetime.datetime.strptime(date1, datetimeFormat) \
       - datetime.datetime.strptime(date2, datetimeFormat)

print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)

@client.command(trigger=cmd_name,
                aliases=[])  # aliases is a list of strs of other triggers for the command
async def rat(command: str, message: discord.Message):
    rats = f"No rats spotted in the caf as of today, if this changes DM Saito, time since last seen {diff}"
    await message.channel.send(rats)
    return
