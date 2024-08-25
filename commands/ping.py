from discord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        '''Pings the server.'''
        latency = round(self.bot.latency * 1000)
        await ctx.send(f':ping_pong: **Pong!** {latency} ms.')

async def setup(bot):
    await bot.add_cog(PingCommand(bot))
