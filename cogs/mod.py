import discord
from discord.ext import commands
from modules import zz_functions
from modules import zz_init

class MembersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def resetuser(self, ctx, arg=None):
        if ctx.message.channel.id == zz_init.config.main['IDchanneladmin']:
            if arg:
                await zz_functions.resetuser(ctx.message, arg)

    @commands.command()
    @commands.guild_only()
    async def customdbcommand(self, ctx, arg=None):
        text = ctx.message.content
        text = text.replace("!customdbcommand ", "")
        if ctx.message.channel.id == zz_init.config.main['IDchanneladmin']:
            if arg:
                #print(text)
                await zz_functions.customdbcommand(ctx.message, text)


    @commands.command()
    @commands.guild_only()
    async def resetrank(self, ctx, arg=None):
        if ctx.message.channel.id == zz_init.config.main['IDchanneladmin']:
            if arg:
                await zz_functions.resetrank(ctx.message, arg)

    @commands.command()
    @commands.guild_only()
    async def addblacklist(self, ctx, arg=None):
        if ctx.message.channel.id == zz_init.config.main['IDchanneladmin']:
            if arg:
                await zz_functions.addblacklistword(ctx.message, arg)
            else:
                await ctx.channel.send("Bitte versuchen Sie den Befehl erneut mit einem Argument!")

    @commands.command()
    @commands.guild_only()
    async def removeblacklist(self, ctx, arg=None):
        if ctx.message.channel.id == zz_init.config.main['IDchanneladmin']:
            if arg:
                await zz_functions.removeblacklistword(ctx.message, arg)
            else:
                await ctx.channel.send("Bitte versuchen Sie den Befehl erneut mit einem Argument!")

    @commands.command()
    @commands.guild_only()
    async def blacklist(self, ctx):
        if ctx.message.channel.id == zz_init.config.main['IDchanneladmin']:
            await ctx.message.channel.send(await zz_functions.blacklist())

    @commands.command()
    @commands.guild_only()
    async def syncwhitelist(self, ctx):
        if ctx.message.channel.id == zz_init.config.main['IDchanneladmin']:
            await zz_functions.syncwhitelist()

    @commands.command()
    @commands.guild_only()
    async def sd(self, ctx):
        if ctx.message.channel.id == zz_init.config.main['IDchanneladmin']:
            await zz_functions.cmndshutdown(self.bot)

    @commands.command()
    @commands.guild_only()
    async def checkwhitelist(self, ctx):
        if ctx.message.channel.id == zz_init.config.main['IDchanneladmin']:
            await zz_functions.cmndwhitelist(ctx.message)

    @commands.command()
    @commands.guild_only()
    async def say(self, ctx, arg=None):
        if ctx.message.channel.id == zz_init.config.main['IDchanneladmin']:
            channel = self.bot.get_channel(zz_init.config.main['IDchannelstandard'])
            await channel.send(arg)
#    @commands.command()
#    @commands.guild_only()
#    async def checkdb(self, ctx):
#        if ctx.message.channel.id == IDchanneladmin:
#            await zz_functions.cmndcheckdb(ctx.message,commands.Bot)

def setup(bot):
    bot.add_cog(MembersCog(bot))
