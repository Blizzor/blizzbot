import discord
#import requests
#import json
#import os.path
#import logging
#import datetime
#import os
#import math
#test
import zz_setup

zz_setup.checkfiles()

import zz_init
import zz_functions
#import mysql.connector

from random import randrange
#from os import path
from discord.ext import commands
from discord.utils import get
#from shutil import copyfile



zz_init.logger()

token = zz_init.config().get_token()
IDcategoryvoice = zz_init.config().get_IDcategoryvoice()
IDchannelcommand = zz_init.config().get_IDchannelcommand()
IDchannelverificate = zz_init.config().get_IDchannelverificate()
IDchanneladmin = zz_init.config().get_IDchanneladmin()
IDgrpverificate = zz_init.config().get_IDgrpverificate()
IDgrpYT = zz_init.config().get_IDgrpYT()
IDgrpYTGold = zz_init.config().get_IDgrpYTGold()
IDgrpYTDiamant = zz_init.config().get_IDgrpYTDiamant()

bot = commands.Bot(command_prefix='!', case_insensitive=True, help_command=None)

@bot.event
async def on_ready():
#    print(discord)
    print('Bot wurde gestartet')

@bot.command()
async def test(ctx, arg="null"):
    print(ctx.message.raw_mentions)
#    print(ctx.message)
#    print(arg)
#   embed=discord.Embed()
#    embed = discord.Embed(title="Title", description="Desc", color=0xedbc5d)
#    embed.set_image(url="https://vignette.wikia.nocookie.net/minecraft/images/1/19/Apfel.png/revision/latest/top-crop/width/360/height/450?cb=20160919195300&path-prefix=de")
#    embed.set_thumbnail(url=ctx.message.author.avatar_url)
#    embed.set_author(name="fred",url="https://vignette.wikia.nocookie.net/minecraft/images/1/19/Apfel.png/revision/latest/top-crop/width/360/height/450?cb=20160919195300&path-prefix=de", icon_url="https://vignette.wikia.nocookie.net/minecraft/images/1/19/Apfel.png/revision/latest/top-crop/width/360/height/450?cb=20160919195300&path-prefix=de")
#    embed.set_footer(text="fred",icon_url="https://vignette.wikia.nocookie.net/minecraft/images/1/19/Apfel.png/revision/latest/top-crop/width/360/height/450?cb=20160919195300&path-prefix=de")
#    await ctx.channel.send(embed=embed)
#    print(ctx.message.author.avatar_url)
#    #await ctx.send(arg)
#    #print(ctx)
#    #print(arg)

@bot.command()
async def help(ctx):
    if ctx.message.channel.id == IDchannelcommand:
        await zz_functions.cmndhelp(ctx.message)

@bot.command()
async def mc(ctx, arg=None):
    if ctx.message.channel.id == IDchannelcommand:
        if arg:
            await zz_functions.cmndmc(ctx.message, bot, arg)
        else:
            await zz_functions.cmndmc(ctx.message, bot)

@bot.command()
async def mcname(ctx, arg=None):
    if ctx.message.channel.id == IDchannelcommand:
        if arg:
            await zz_functions.cmndmcname(ctx.message, arg)
        else:
            await zz_functions.cmndmcname(ctx.message)

@bot.command()
async def rank(ctx, arg=None):
    if ctx.message.channel.id == IDchannelcommand:
        if arg:
            await zz_functions.cmndrank(ctx.message, arg)
        else:
            await zz_functions.cmndrank(ctx.message)

@bot.command()
async def ranking(ctx):
    if ctx.message.channel.id == IDchannelcommand:
        await zz_functions.cmndranking(ctx.message)

@bot.command()
async def streamchannel(ctx):
    if ctx.message.channel.id == IDchannelcommand:
        await zz_functions.cmndstreamchannel(ctx.message)

@bot.command()
async def syncwhitelist(ctx):
    if ctx.message.channel.id == IDchanneladmin:
        await zz_functions.syncwhitelist()

@bot.command()
async def zz(ctx):
    if ctx.message.channel.id == IDchannelverificate:
        member = discord.utils.find(lambda m: m.id == IDgrpverificate, ctx.author.roles)
        await ctx.message.delete()
        await ctx.author.create_dm()
        if not member:
            grpverify = ctx.guild.get_role(IDgrpverificate)
            await ctx.author.add_roles(grpverify)
            await ctx.author.dm_channel.send("Du wurdest erfolgreich freigeschalten!")
        else:
            await ctx.author.dm_channel.send("Du bist bereits freigeschalten!")


@bot.command()
async def sd(ctx):
    if ctx.message.channel.id == IDchanneladmin:
        await zz_functions.cmndshutdown(bot)

@bot.command()
async def checkwhitelist(ctx):
    if ctx.message.channel.id == IDchanneladmin:
        await zz_functions.cmndwhitelist(ctx.message)

@bot.command()
async def checkdb(ctx):
    if ctx.message.channel.id == IDchanneladmin:
        await zz_functions.cmndcheckdb(ctx.message,bot)

@bot.command()
async def amazon(ctx):
    await ctx.message.channel.send("https://www.amazon.de/shop/blizzor")

@bot.command()
async def equipment(ctx):
    await ctx.message.channel.send("https://www.amazon.de/shop/blizzor")

@bot.command()
async def youtube(ctx):
    await ctx.message.channel.send("https://www.youtube.com/Blizzor")

@bot.command()
async def twitter(ctx):
    await ctx.message.channel.send("https://www.blizzor.de/twitter")

@bot.command()
async def twitch(ctx):
    await ctx.message.channel.send("https://www.blizzor.de/twitch")

@bot.command()
async def facebook(ctx):
    await ctx.message.channel.send("https://www.blizzor.de/facebook")

@bot.command()
async def instagram(ctx):
    await ctx.message.channel.send("https://www.blizzor.de/instagram")

@bot.command()
async def reloadcommand(ctx, arg):
    # vllt get_command(name)
    #remove_command(arg)
    #add_command(arg)
    #bot.reload_extension(arg)
    pass

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.channel.id == IDchannelverificate and message.content != "!zz":
        await message.delete()


    if message.author != bot.user and message.guild and message.channel.id != IDchannelcommand:
        await zz_functions.getexp(message)
        number = randrange(0,200)
        if(number == 5):
            await message.add_reaction('<:ZZBlizzor:493814042780237824>')


    if message.author != bot.user and not message.guild:
        if message.content == '!zz':
            for i in bot.guilds[0].members:
                if i.id == message.author.id:
                    for j in bot.guilds[0].roles:
                        if j.id == IDgrpverificate:
                            await i.add_roles(j)
                    await message.author.dm_channel.send("Du wurdest erfolgreich freigeschalten!")

@bot.event
async def on_member_join(member):
    Nachricht = """Willkommen auf Blizzor's Community Server.
    Damit du auf dem Server freigeschalten wirst, musst du den Befehl !zz verwenden.
    Bitte gib diesen Befehl im Channel #freischalten oder unter dieser Nachricht ein."""
    await member.create_dm()
    await member.dm_channel.send(content=Nachricht)
    return

@bot.event
async def on_member_update(before,after):
    mydb = zz_init.getdb()
    mycursor = mydb.cursor()

    checksubrole = False
    checkgoldrole = False

    for i in after.roles:               #Pruefe ob Youtube Subscriber
        if i.id == IDgrpYT:
            checksubrole = True
        if i.id == IDgrpYTGold:
            checkgoldrole = True
    if not checkgoldrole and checksubrole:#Wenn kein YT-Gold
        await after.add_roles(after.guild.get_role(IDgrpYTDiamant))
#        for k in bot.guilds[0].roles:
#            if k.id == IDgrpYTDiamant:
#                await after.add_roles(k)
    if not checksubrole:
        for l in after.roles:
            if l.id == IDgrpYTDiamant or l.id == IDgrpYTGold:
                await after.remove_roles(l)

    wlrole = False
    roles = after.roles
    for i in roles:
        if i.id == IDgrpYTDiamant:
            wlrole = True
        sql = "UPDATE mcnames SET isWhitelisted = %s WHERE discord_id = %s"
        val = (wlrole, after.id)

        mycursor.execute(sql, val)
        mydb.commit()

    await zz_functions.syncwhitelist()

    return

@bot.event
async def on_voice_state_update(member, before, after):

    channels = (member.guild.voice_channels)
    for j in channels:
        if j.name == "Stream-Channel": # Wenn Kategory richtig ist
            if not j.members:
                await j.delete()

    channels = (member.guild.voice_channels)

    emptychannels = False
    cpchannel = channels[0]
    for j in channels:
        if j.category.id == IDcategoryvoice: # Wenn Kategory richtig ist
            if not j.members: # Wenn niemand im Channel ist
                if not emptychannels: # Wenn emptychannel False ist
                    emptychannels = True
                else: # Wenn emptychannel True ist
                    await j.delete()
            cpchannel = j
    if not emptychannels:
        await cpchannel.clone(name="Channel")
    return

bot.run(token)
