#!/usr/bin/python3.8
import discord

from modules import zz_setup
from modules import zz_init
from modules import zz_functions

from random import randrange

from discord.ext import commands
from discord.utils import get



zz_init.logger()

token = zz_init.config().get_token()
IDcategoryvoice = zz_init.config().get_IDcategoryvoice()
IDchannelcommand = zz_init.config().get_IDchannelcommand()
IDchannelverificate = zz_init.config().get_IDchannelverificate()
IDchanneladmin = zz_init.config().get_IDchanneladmin()
IDchannellogs = zz_init.config().get_IDchannellogs()
IDgrpverificate = zz_init.config().get_IDgrpverificate()
IDgrpYT = zz_init.config().get_IDgrpYT()
IDgrpYTGold = zz_init.config().get_IDgrpYTGold()
IDgrpYTDiamant = zz_init.config().get_IDgrpYTDiamant()
ArrayIDgrpsubserver = zz_init.config().get_ArrayIDgrpsubserver()

bot = commands.Bot(command_prefix='!', case_insensitive=True, help_command=None)

initial_extensions = ['cogs.user',
                      'cogs.mod']

if __name__ == '__main__': #Wenn Datei als Hauptdatei aufgerufen wird
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print('Bot wurde gestartet')
#
#@bot.command()
#async def test(ctx, arg="null"):
#    print(ctx.message.raw_mentions)
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
async def mc(ctx, arg=None):
    if ctx.message.channel.id == IDchannelcommand:
        if arg:
            await zz_functions.cmndmc(ctx.message, bot, arg)
        else:
            await zz_functions.cmndmc(ctx.message, bot)

@bot.command()
async def checkdb(ctx):
    if ctx.message.channel.id == IDchanneladmin:
        await zz_functions.cmndcheckdb(ctx.message,bot)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.channel.id == IDchannelverificate and message.content != "!zz":
        await message.delete()


    if message.author != bot.user and message.guild and message.channel.id != IDchannelcommand:
        await zz_functions.getexp(message)
        number = randrange(0,1000)
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

    #checksubrole = False
    #checkgoldrole = False

    #if await zz_functions.checkrole(after.roles, IDgrpYT):
    #    checksubrole = True

    #if await zz_functions.checkrole(after.roles, IDgrpYTDiamant):
    #    checkgoldrole = True

    #if not checkgoldrole and checksubrole:#Wenn kein YT-Gold
    #    await after.add_roles(after.guild.get_role(IDgrpYTDiamant))

    #if not checksubrole:
    #    for l in after.roles:
    #        if l.id == IDgrpYTDiamant or l.id == IDgrpYTGold:
    #            await after.remove_roles(l)

    #wlrole = False
    #roles = after.roles
    #for i in roles:
    wlrole = False
    for i in ArrayIDgrpsubserver:
        if await zz_functions.checkrole(after.roles, i):
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
