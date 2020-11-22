import discord
from discord.ext import commands

from translate import translator
import datetime
import os

token = str(os.getenv("token"))
prefix = "/"

client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready():
    print((datetime.datetime.now().strftime("%H:%M:%S")) + "| | " + (client.user.name) + '#' + (client.user.discriminator))

@client.event
async def on_reaction_add(rec, user):
    channel = rec.message.channel
    contxt = rec.message.content

    if str(rec) == "🇷🇺":
        lang = translator(source = 'en', target = 'ru', phrase =contxt)
        e = discord.Embed(title = "Russian", description = lang[0][0][0])
        await channel.send(embed = e)

    elif str(rec) == "🇪🇸":
        lang = translator(source = 'en', target = 'es', phrase =contxt)
        e = discord.Embed(title = "Spanish", description = lang[0][0][0])
        await channel.send(embed = e)

    elif str(rec) == "🇺🇸":
        lang = translator(source = 'en', target = 'en', phrase =contxt)
        e = discord.Embed(title = "English", description = lang[0][0][0])
        await channel.send(embed = e)

    elif str(rec) == "🇵🇭":
        lang = translator(source = 'en', target = 'tl', phrase =contxt)
        e = discord.Embed(title = "Filipino", description = lang[0][0][0])
        await channel.send(embed = e)

    elif str(rec) == "🏴󠁧󠁢󠁳󠁣󠁴󠁿":
        lang = translator(source = 'en', target = 'gd', phrase =contxt)
        e = discord.Embed(title = "Scottish", description = lang[0][0][0])
        await channel.send(embed = e)

client.run(token)