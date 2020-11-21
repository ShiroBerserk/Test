import discord
from discord.ext import commands
import asyncio

import datetime
from googletrans import Translator
import json
import requests
import os


token = str(os.getenv("token"))
prefix = "/"


client = commands.Bot(command_prefix = prefix)


@client.event
async def on_ready():
    print((datetime.datetime.now().strftime("%H:%M:%S")) + "| | " + (client.user.name) + '#' + (client.user.discriminator))


@client.event
async def on_reaction_add(rec,user):
    translator = Translator()
    await asyncio.sleep(5.5)
    channel = rec.message.channel
    contxt = rec.message.content
    if str(rec) == "🇷🇺":
        lang1 = translator.translate(text = str(contxt), dest='ru')
        e = discord.Embed(title = "Russian", description = lang1.text)
        await channel.send(embed = e)

    elif str(rec) == "🇪🇸":
        lang2 = translator.translate(text = str(contxt), dest='es')
        e = discord.Embed(title = "Spanish", description = lang2.text)
        await channel.send(embed = e)

    elif str(rec) == "🇺🇸":
        lang3 = translator.translate(text = str(contxt), dest='en')
        e = discord.Embed(title = "English", description = lang3.text)
        await channel.send(embed = e)

    elif str(rec) == "🇵🇭":
        lang4 = translator.translate(text = str(contxt), dest='tl')
        e = discord.Embed(title = "Filipino", description = lang4.text)
        await channel.send(embed = e)

    elif str(rec) == "🏴󠁧󠁢󠁳󠁣󠁴󠁿":
        lang5 = translator.translate(text = str(contxt), dest='gd')
        e = discord.Embed(title = "Scottish", description = lang5.text)
        await channel.send(embed = e)

client.run(token)