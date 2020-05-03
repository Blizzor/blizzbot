import discord
from discord.ext import commands
from modules import zz_functions
from modules import zz_init

IDchanneladmin = zz_init.config().get_IDchanneladmin()
IDchannelcommand = zz_init.config().get_IDchannelcommand()

class MembersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def resetrank(self, ctx, arg=None):
        if ctx.message.channel.id == IDchannelcommand:
            if arg:
                await zz_functions.resetrank(ctx.message, arg)

    @commands.command()
    @commands.guild_only()
    async def syncwhitelist(self, ctx):
        if ctx.message.channel.id == IDchanneladmin:
            await zz_functions.syncwhitelist()

    @commands.command()
    @commands.guild_only()
    async def sd(self, ctx):
        if ctx.message.channel.id == IDchanneladmin:
            await zz_functions.cmndshutdown(bot)

    @commands.command()
    @commands.guild_only()
    async def checkwhitelist(self, ctx):
        if ctx.message.channel.id == IDchanneladmin:
            await zz_functions.cmndwhitelist(ctx.message)

#    @commands.command()
#    @commands.guild_only()
#    async def checkdb(self, ctx):
#        if ctx.message.channel.id == IDchanneladmin:
#            await zz_functions.cmndcheckdb(ctx.message,commands.Bot)

def setup(bot):
    bot.add_cog(MembersCog(bot))
