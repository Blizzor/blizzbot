#!/usr/bin/python3.8
import discord

from modules import zz_setup
from modules import zz_init
from modules import zz_functions

from random import randrange

from discord.ext import commands
from discord.utils import get

import re

intents = discord.Intents()
intents.messages = True
intents.reactions = True
intents.members = True
intents.voice_states = True
intents.emojis = True
intents.guilds = True

zz_init.logger()

#test
bot = commands.Bot(command_prefix='!', case_insensitive=True, help_command=None, intents=intents)

initial_extensions = ['cogs.user',
                      'cogs.mod']

if __name__ == '__main__': #Wenn Datei als Hauptdatei aufgerufen wird
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print('Bot wurde gestartet')
    return

@bot.command(aliases=["minecraft"])
async def mc(ctx, arg=None):
    if ctx.message.channel.id == zz_init.config.main['IDchannelcommand']:
        if arg:
            await zz_functions.cmndmc(ctx.message, bot, arg)
        else:
            await zz_functions.cmndmc(ctx.message, bot)

@bot.command(aliases=["checkdatabase"])
async def checkdb(ctx):
    if ctx.message.channel.id == zz_init.config.main['IDchanneladmin']:
        await zz_functions.cmndcheckdb(ctx.message,bot)

@bot.command()
async def anfrage(ctx):
    if ctx.message.channel.id == zz_init.config.main['IDchannelcommand']:
        Nachricht = await zz_functions.question(ctx.message,bot)

        channels = (ctx.author.guild.text_channels)
        for j in channels:
            if j.name == "anfragen": # Wenn Kategory richtig ist
                await j.send(Nachricht)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    filter = True

    messageNoWhitespace = re.sub(' *', '', message.content)
    if re.fullmatch(r".*https?:.*\.[a-zA-Z]{2,3}.*", messageNoWhitespace, re.I) and message.guild:
        if await zz_functions.checkrole(message.author.roles, zz_init.config.main['IDgrpverificate']):
            for i in zz_init.config.main['ArraynoFilter']:
                if await zz_functions.checkrole(message.author.roles, i):
                    filter = False
            if filter:
                await message.delete()

    if message.guild and message.author != bot.user and message.channel.id != zz_init.config.main['IDchanneladmin']:
        if await zz_functions.checkwords(message):
            await message.delete()
            await message.author.create_dm()
            await message.author.dm_channel.send("Ihre Nachricht mit dem Inhalt **" + message.content + "** wurde entfernt. Melden Sie sich bei Fragen an einen Moderator.")

    if message.channel.id == zz_init.config.main['IDchannelverificate'] and message.content != "!zz":
        await message.delete()

    if message.author != bot.user and message.guild and message.channel.id != zz_init.config.main['IDchannelcommand'] and message.channel.category_id != zz_init.config.main['IDcategorytext']:
        await zz_functions.getexp(message)
        number = randrange(0,1000)
        if(number == 5):
            await message.add_reaction('<:ZZBlizzor:493814042780237824>')


#    if message.author != bot.user and not message.guild:
#        if message.content == '!zz':
#            for i in bot.guilds[0].members:
#                if i.id == message.author.id:
#                    for j in bot.guilds[0].roles:
#                        if j.id == IDgrpverificate:
#                            await i.add_roles(j)
#                    await message.author.dm_channel.send("Du wurdest erfolgreich freigeschalten!")
#                    await zz_functions.gotverified(message.author, bot.get_channel(IDchannelstandard), bot)

@bot.event
async def on_raw_reaction_add(payload):

    if payload.channel_id == zz_init.config.main['IDchannelverificate']:
        if payload.emoji.id == 704707230137581658: #testserverid: 596435950469513216  #serverid: 704707230137581658
            for i in bot.guilds[0].roles:
                if i.id == zz_init.config.main['IDgrpverificate'] or i.id == zz_init.config.main['IDgrpnotify']:
                    if i.id == zz_init.config.main['IDgrpverificate']:
                        await payload.member.add_roles(i)
                        await zz_functions.gotverified(payload.member, bot.get_channel(zz_init.config.main['IDchannelstandard']), bot)
                    else:
                        await payload.member.add_roles(i)

    if(payload.member != bot.user):
        if payload.channel_id == zz_init.config.main['IDchannelcommand']:
            if payload.emoji.id == 780172418781675531: # Links
                await zz_functions.switchrank(payload, bot)
        if payload.channel_id == zz_init.config.main['IDchannelcommand']:
            if payload.emoji.id == 780171887619473458: # Rechts
                await zz_functions.switchrank(payload, bot)


@bot.event
async def on_member_join(member):
    Nachricht = """Willkommen auf Blizzor's Community Server.
    Damit du auf dem Server freigeschalten wirst, musst du den Befehl !zz verwenden.
    Bitte gib diesen Befehl im Channel #freischalten ein."""
    await member.create_dm()
    await member.dm_channel.send(content=Nachricht)
    #await zz_functions.newjoin(member)
    #embed = discord.Embed(title="Willkommen!", color=0xedbc5d)
    #embed.set_thumbnail(url=member.avatar_url)
    #embed.add_field(name="Name", value=member.name, inline=False)
    #embed.add_field(name="freigeschalten?", value="Nein", inline=False)
    #channel = bot.get_channel(IDchannelstandard)
    #await channel.send(embed=embed)
    return

@bot.event
async def on_member_remove(member):
    mydb = zz_init.mydb
    mycursor = mydb.cursor()
    sql = "DELETE FROM mcnames WHERE discord_id = " + str(member.id)

    mycursor.execute(sql)
    mydb.commit()

    sql = "DELETE FROM ranking WHERE discord_id = " + str(member.id)

    mycursor.execute(sql)
    mydb.commit()

    return

@bot.event
async def on_member_update(before,after):

    if(before.roles != after.roles):

        mydb = zz_init.mydb
        mycursor = mydb.cursor()

        wlroleyoutube = False
        wlroletwitch = False
        for i in zz_init.config.main['ArrayIDgrpsubyoutube']:
            if await zz_functions.checkrole(after.roles, i):
                wlroleyoutube = True
        for i in zz_init.config.main['ArrayIDgrpsubtwitch']:
            if await zz_functions.checkrole(after.roles, i):
                wlroletwitch = True
        sql = "UPDATE mcnames SET isWhitelistedYoutube = %s WHERE discord_id = %s"
        val = (wlroleyoutube, after.id)

        mycursor.execute(sql, val)
        mydb.commit()

        sql = "UPDATE mcnames SET isWhitelistedTwitch = %s WHERE discord_id = %s"
        val = (wlroletwitch, after.id)

        mycursor.execute(sql, val)
        mydb.commit()

        await zz_functions.syncwhitelist()

    return

@bot.event
async def on_voice_state_update(member, before, after):
    #print(before.channel)
    #print(after.channel)
    if(before.channel != after.channel): #Wenn Änderung durch Channelwechsel stattfindet
        tcategory = None
        for n in member.guild.categories:
            if n.id == zz_init.config.main['IDcategorytext']:
                tcategory = n

        channels = (member.guild.voice_channels)
        for j in channels:
            if j.name == "Stream-Channel": # Wenn Kategory richtig ist
                if not j.members:
                    await j.delete()

        channels = (member.guild.voice_channels)

        emptychannels = False
        cpchannel = channels[0]
        for j in channels:
            if j.category.id == zz_init.config.main['IDcategoryvoice']: # Wenn Kategory richtig ist
                if not j.members: # Wenn niemand im Channel ist
                    if not emptychannels: # Wenn emptychannel False ist
                        emptychannels = True
                    else: # Wenn emptychannel True ist
                        await j.delete()
                cpchannel = j
        if not emptychannels:
            await cpchannel.clone(name="Channel")

        tchannels = (member.guild.text_channels)
        #temprole2 = None
        #Entfernt Textchannel für Voicechannel
        if(before.channel != None): # Wenn Benutzer Channel verlässt
            #Entferne Nutzer aus Role
            for k in channels: # Prüfe Sprachchannel
                if k.category.id == zz_init.config.main['IDcategoryvoice'] and k.id == before.channel.id: # Wenn Kategory richtig ist
                    if not k.members: # Wenn niemand im Channel ist
                        #Entferne Berechtigung
                        for l in tchannels:
                            if(l.topic != None and l.category.id == zz_init.config.main['IDcategorytext']):
                                if str(k.id) == l.topic:
                                    await l.delete() # Entferne Textchannel
                    else:
                        #Entferne Channel
                        for l3 in tchannels:
                            if(l3.topic != None and l3.category.id == zz_init.config.main['IDcategorytext']):
                                if str(k.id) == l3.topic:
                                    await l3.set_permissions(member, read_messages=None)


        if(after.channel != None and after.channel.category_id == zz_init.config.main['IDcategoryvoice'] and after.channel.name != "Stream-Channel"): # Wenn Channel betreten wird

            channelexists = False
            for m in tchannels:
                if(m.topic == str(after.channel.id)):
                    channelexists = True
            if(not channelexists): # Wenn der Textchannel nicht existiert
                overwrites = {
                member.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                member.guild.get_role(zz_init.config.main['IDgrpMod']): discord.PermissionOverwrite(read_messages=True)
                }
                await member.guild.create_text_channel('Channel', overwrites=overwrites, category = tcategory, topic = after.channel.id)
            tchannels = (member.guild.text_channels)
            for l2 in tchannels:
                if(l2.topic != None and l2.category.id == zz_init.config.main['IDcategorytext']):
                    if str(after.channel.id) == l2.topic:
                        await l2.set_permissions(member, read_messages=True)

    return

@bot.event
async def on_message_delete(message):
    if(message):

        channel = discord.utils.get(message.guild.text_channels, id=zz_init.config.main['IDchannellogs'])

        embed = discord.Embed(title="Gelöschte Nachricht", color=0xedbc5d)
        if(message.author.avatar_url):
            embed.set_thumbnail(url=message.author.avatar_url)
        if(message.author.name):
            embed.add_field(name="Name", value=message.author.name, inline=True)
        else:
            embed.add_field(name="Name", value="Name unbekannt", inline=True)
        if(message.channel.name):
            embed.add_field(name="Channel", value=message.channel.name, inline=True)
        else:
            embed.add_field(name="Channel", value="Channel unbekannt???", inline=True)
        if(message.content):
            embed.add_field(name="Inhalt", value=message.content, inline=False)
        else:
            embed.add_field(name="Inhalt", value="Inhalt nicht auslesbar", inline=False)

        await channel.send(embed=embed)

    return

#@bot.event
#async def on_error(event):
#    channel = discord.utils.get(bot.guild.channels, id='IDchannellogs')
#    channel.send(event)
bot.run(zz_init.config.main['token'])
