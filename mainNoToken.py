# coding=utf-8
"""A silly bot for silly friends."""
import discord

# sets the client
client = discord.Client()


@client.event
async def on_ready():
    """On login print information about the bot."""
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_guild_join(guild):
    """On joining a discord server(guild) send a welcome message."""
    print("guild join")
    for channel in guild.text_channels:
        if channel and channel.permissions_for(guild.me).send_messages:
            await channel.send("Hey Mom!")
            break


# noinspection PyBroadExceptions
@client.event
async def on_message(message):
    """Send a message every time a message is received in the special channel"""
    if message.author.bot:
        pass
    elif message.channel.id == 649017651158319116 and message.author.id == 381524241381720064:
        await message.channel.send('thanks mom')


# start the bot using the token(placeholder used here)
client.run("token")
# “https://discordapp.com/oauth2/authorize?client_id=659060357087887390&scope=bot”
