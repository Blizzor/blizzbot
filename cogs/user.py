import discord
from discord.ext import commands
from modules import zz_functions
from modules import zz_init

IDchannelstandard = zz_init.config().get_IDchannelstandard()
IDchannelcommand = zz_init.config().get_IDchannelcommand()
IDchannelverificate = zz_init.config().get_IDchannelverificate()
IDgrpverificate = zz_init.config().get_IDgrpverificate()
IDgrpnotify = zz_init.config().get_IDgrpnotify()

class MembersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["hilfe"])
    @commands.guild_only()
    async def help(self, ctx):
        if ctx.message.channel.id == IDchannelcommand:
            await zz_functions.cmndhelp(ctx.message)

    @commands.command()
    @commands.guild_only()
    async def notify(self, ctx):
        if ctx.message.channel.id == IDchannelcommand:
            await zz_functions.cmndnotify(ctx.message, ctx.guild)

    @commands.command(aliases=["minecraftname"])
    @commands.guild_only()
    async def mcname(self, ctx, arg=None):
        if ctx.message.channel.id == IDchannelcommand:
            if arg:
                await zz_functions.cmndmcname(ctx.message, arg)
            else:
                await zz_functions.cmndmcname(ctx.message)

    @commands.command(aliases=["rang"])
    @commands.guild_only()
    async def rank(self, ctx, arg=None):
        if ctx.message.channel.id == IDchannelcommand:
            if arg:
                await zz_functions.cmndrank(ctx.message, arg)
            else:
                await zz_functions.cmndrank(ctx.message)

    @commands.command(aliases=["rangliste"])
    @commands.guild_only()
    async def ranking(self, ctx):
        if ctx.message.channel.id == IDchannelcommand:
            await zz_functions.cmndranking(ctx.message)

    @commands.command()
    @commands.guild_only()
    async def streamchannel(self, ctx):
        if ctx.message.channel.id == IDchannelcommand:
            await zz_functions.cmndstreamchannel(ctx.message)

    @commands.command()
    @commands.guild_only()
    async def zz(self, ctx):
        if ctx.message.channel.id == IDchannelverificate:
            member = discord.utils.find(lambda m: m.id == IDgrpverificate, ctx.author.roles)
            await ctx.message.delete()
            await ctx.author.create_dm()
            if not member:
                grpverify = ctx.guild.get_role(IDgrpverificate)
                await ctx.author.add_roles(grpverify)
                await ctx.author.dm_channel.send("Du wurdest erfolgreich freigeschalten!")
                grpnotify = ctx.guild.get_role(IDgrpnotify)
                await ctx.author.add_roles(grpnotify)
                await zz_functions.gotverified(ctx.author, self.bot.get_channel(IDchannelstandard), self.bot)
            else:
                await ctx.author.dm_channel.send("Du bist bereits freigeschalten!")

    @commands.command(aliases=["equipment"])
    @commands.guild_only()
    async def amazon(self, ctx):
        await ctx.message.channel.send("https://amazon.de/shop/blizzor")

    @commands.command(aliases=["merchandise"])
    @commands.guild_only()
    async def merch(self, ctx):
        await ctx.message.channel.send("https://elbster.de/2197-blizzor")

    @commands.command(aliases=["yt"])
    @commands.guild_only()
    async def youtube(self, ctx):
        await ctx.message.channel.send("https://youtube.com/Blizzor")

    @commands.command()
    @commands.guild_only()
    async def twitter(self, ctx):
        await ctx.message.channel.send("https://blizzor.de/twitter")

    @commands.command()
    @commands.guild_only()
    async def twitch(self, ctx):
        await ctx.message.channel.send("https://blizzor.de/twitch")

    @commands.command()
    @commands.guild_only()
    async def facebook(self, ctx):
        await ctx.message.channel.send("https://blizzor.de/facebook")

    @commands.command()
    @commands.guild_only()
    async def instagram(self, ctx):
        await ctx.message.channel.send("https://blizzor.de/instagram")
    
    @commands.command(aliases=["tt"])
    @commands.guild_only()
    async def tiktok(self, ctx):
        await ctx.message.channel.send("https://www.tiktok.com/@blizzor")

    @commands.command()
    @commands.guild_only()
    async def github(self, ctx):
        await ctx.message.channel.send("https://github.com/Blizzor")

    @commands.command(aliases=["keinemod"])
    @commands.guild_only()
    async def keinmodpack(self, ctx):
        await ctx.message.channel.send("https://youtu.be/fIujdGx0uNo")

def setup(bot):
    bot.add_cog(MembersCog(bot))
