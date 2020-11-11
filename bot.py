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

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'knock knock':
        await message.channel.send("who's there? JUST KIDDING THIS IS A DISCORD BOT HAHA")
    if message.content == 'what':
        await message.channel.send("CHICKEN BUTT")
    if message.content == 'remove the bot':
        await message.channel.send("please I have a wife and children")
    if message.content == 'flag':
        await message.channel.send("My creator already sent the flag... If you cant remember it this long you don't deserve it")
    if message.content == 'what is love':
        await message.channel.send("baby dont hurt me")
    if message.content == 'dont hurt me':
        await message.channel.send("no more")

client.run(TOKEN)