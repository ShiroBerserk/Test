import discord
from discord.ext import commands
import asyncio

import datetime
from google_trans_new import google_translator
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
    translator = google_translator()
    channel = rec.message.channel
    contxt = rec.message.content
    if str(rec) == "🇷🇺":
        lang1 = translator.translate(text = str(contxt), lang_tgt='ru')
        e = discord.Embed(title = "Russian", description = lang1)
        await channel.send(embed = e)

    elif str(rec) == "🇪🇸":
        lang2 = translator.translate(text = str(contxt), lang_tgt='es')
        e = discord.Embed(title = "Spanish", description = lang2)
        await channel.send(embed = e)

    elif str(rec) == "🇺🇸":
        lang3 = translator.translate(text = str(contxt), lang_tgt='en')
        e = discord.Embed(title = "English", description = lang3)
        await channel.send(embed = e)

    elif str(rec) == "🇵🇭":
        lang4 = translator.translate(text = str(contxt), lang_tgt='tl')
        e = discord.Embed(title = "Filipino", description = lang4)
        await channel.send(embed = e)

    elif str(rec) == "🏴󠁧󠁢󠁳󠁣󠁴󠁿":
        lang5 = translator.translate(text = str(contxt), lang_tgt='gd')
        e = discord.Embed(title = "Scottish", description = lang5)
        await channel.send(embed = e)

client.run(token)