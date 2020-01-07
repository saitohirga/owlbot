import log
from client import client
from modules import __common__
from typing import List, Union

import discord

primary_channels: List[int] = [
    458765855115968513,  # general
]

other_channels: List[int] = [
    458778401361100800,  # news
    458766468172218369,  # media
    458766498018754572,  # classes
    458766780471705630,  # clubs
    458766872406523914,  # Campus Events
    458767089633853443,  # Tutoring
    458766836104822795,  # music
    491299425000357908,  # Ask-Owlsey
    533430755817422870,  # Nasty
    605612441417678870,  # Gaming
    642408926419222559,  # GradTickets

]

public_voice_channels: List[int] = [
    458765855115968515,  # General Voice
    458767710516674590,  # Tutoring
    458767831274618880,  # AFK
    458772832449593357,  # Music
    605613190759448617,  # Gaming

]

lock_help = {
    "Usage": f"`{client.default_prefix}lock`\n"
             f"`{client.default_prefix}unlock`",
    "Arguments": "None",
    "Description": "Locks or unlocks the specified channel in case of a raid or general chaos. This command must be "
                   "run in the target channel. Moderator-only channels cannot be locked. "
}

purge_help = {
    "Usage": f"`{client.default_prefix}purge [n]`",
    "Arguments": "`n` - (Optional) Number of messages to delete, capped at 100. (default 25)",
    "Description": "Nukes some number of recent messages in a channel.",
}
client.long_help("lock", lock_help)
client.long_help("unlock", lock_help)
client.long_help("purge", purge_help)

admin_role = None
if client.is_ready():
    admin_role = client.get_guild(458765854624972811).get_role(458767248367157278)


@client.ready
async def set_mod_role(message: discord.Message):
    global admin_role
    try:
        admin_role = admin_role = client.get_guild(458765854624972811).get_role(458767248367157278)
    except AttributeError:
        log.critical(f"WTC mod role not found, oof")
        await message.channel.send("Error not Admin")

        
@client.command(trigger="lock", aliases=["l"])
async def lock(command: str, message: discord.Message):
    if message.guild.id != 458765854624972811:
        if message.guild.id != 452274699641159683:
            # wrong guild
            await message.channel.send("Invalid server")
            return
    else:
        if admin_role not in message.author.roles:
            # user is not a mod
            await __common__.failure(message)
            return

    parts = command.split(" ")
    # parts = ['lock', arg1]

    # Define it so we can use typing without cluttering it up later
    target: Union[discord.TextChannel, discord.VoiceChannel] = None

    if len(parts) == 1:
        if message.author.voice is not None:
            target = message.author.voice.channel
        else:
            target = message.channel
    else:
        target = message.guild.get_channel(parts[1][2:-1])
    if (target.id not in primary_channels + other_channels + public_voice_channels) and \
            (message.guild.id != 452274699641159683):
        await __common__.failure(message)
        return

    # Take away the proper write/speak permission
    if isinstance(target, discord.TextChannel):
        await target.set_permissions(target=target.guild.default_role,
                                     overwrite=discord.PermissionOverwrite(send_messages=False))
        await message.delete()
        return
    if isinstance(target, discord.VoiceChannel):
        await target.set_permissions(target=target.guild.default_role,
                                     overwrite=discord.PermissionOverwrite(speak=False))
        await message.delete()
        return


@client.command(trigger="unlock", aliases=["ul"])
async def unlock(command: str, message: discord.Message):
    if message.guild.id != 458765854624972811:
        if message.guild.id != 452274699641159683:
            # wrong guild
            await message.channel.send("Invalid server")
            return
    else:
        if admin_role not in message.author.roles:
            # user is not a mod
            await __common__.failure(message)
            return

    parts = command.split(" ")
    # parts = ['unlock', arg1]

    # Define it so we can use typing without cluttering it up later
    target: Union[discord.TextChannel, discord.VoiceChannel] = None

    if len(parts) == 1:
        if message.author.voice is not None:
            target = message.author.voice.channel
        else:
            target = message.channel
    else:
        target = message.guild.get_channel(__common__.strip_to_id(parts[1]))
    if (target.id not in primary_channels + other_channels + public_voice_channels) and \
            (message.guild.id != 452274699641159683):
        await __common__.failure(message)
        return

    # Set the proper write/speak permission
    if isinstance(target, discord.TextChannel):
        await target.set_permissions(target=target.guild.default_role,
                                     overwrite=discord.PermissionOverwrite(send_messages=True))
        await message.delete()
        return
    if isinstance(target, discord.VoiceChannel):
        await target.set_permissions(target=target.guild.default_role,
                                     overwrite=discord.PermissionOverwrite(speak=True))
        await message.delete()
        return


@client.command(trigger="purge", aliases=["nuke"])
async def nuke_old_chat(command: str, message: discord.Message):
    if message.guild.id != 458765854624972811:
        if message.guild.id != 452274699641159683:
            # wrong guild
            await message.channel.send("Invalid server")
            return
    else:
        if admin_role not in message.author.roles:
            # user is not a mod
            await __common__.failure(message)
            return

    parts = command.split(" ")
    if len(parts) == 1:
        count = 25
    else:
        count = int(parts[1])

    target_msgs = await message.channel.history(limit=count).flatten()
    assert isinstance(message.channel, discord.TextChannel)
    assert isinstance(message.guild, discord.Guild)
    await message.channel.delete_messages(target_msgs)
    return


@client.command(trigger="modtools")
async def help_mods(command: str, message: discord.Message):
    embed = discord.Embed(title=f"Tools in {client.bot_name} for moderators",
                          description="Specifically with application to the FAU server",
                          colour=0x419bb8)
    embed = embed.add_field(name="Join/Leave Info",
                            value="When a person joins, information about them will be posted such as account name, "
                                  "ID, creation date, and the new member count. When a person leaves, information "
                                  "about them will be posted such as account name, ID, join date, and new member "
                                  "count.") 
    embed = embed.add_field(name="Name Autoban",
                            value="Users who attempt to join with `discord.gg` in their name will be autobanned upon "
                                  "joining. This is as a result of the indexing \"virus\" bots that spread around "
                                  "Discord some time ago.") 
    embed = embed.add_field(name="Ping Spam Autokick",
                            value="Users who spam too many pings will be automatically kicked as an "
                                  "anti-spambot/anti-raid measure. Criteria are either: (A) 30+ pings to a single "
                                  "person within one minute, or (B) 8+ pings to 8 different people within one minute.") 
    embed = embed.add_field(name="Message and File Logger",
                            value="All messages and files that are sent are automatically saved and downloaded "
                                  "locally (up to 7 days for attachments). This can be used to log users that are "
                                  "banned and inspect suspicious attachments.") 
    embed = embed.add_field(name="Channel Locker",
                            value="In case of emergency/chaos, public channels can be locked to calm down chaos. "
                                  "`owl lock` and `owl unlock` can only be run in that target channels, "
                                  "and moderator-only channels cannot be locked/unlocked (attempting to unlock a "
                                  "moderator-only channel would make it publicly accessible).") 
    embed = embed.add_field(name="Message Purge",
                            value="When necessary, recent messages in a channel can be purged with `owl purge [n]`, "
                                  "where `n` is the number of messages to delete including the command itself ("
                                  "default 25). Maximum purge size is 100 messages.") 
    if admin_role in message.author.roles:
        await message.channel.send(embed=embed)
