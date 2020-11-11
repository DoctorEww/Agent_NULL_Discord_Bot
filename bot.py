# This file is a bot for some office fun! It will add some spice to the coversations.
# Don't take life to seriously
# Author DoctorEww

import discord

TOKEN = "TODO"
GUILD = "TODO"

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
