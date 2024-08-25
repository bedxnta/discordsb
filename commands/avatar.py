import discord
from discord.ext import commands

class AvatarCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, user: discord.User = None):
        '''Displays user's avatar.'''
        if user is None:
            user = ctx.author
        avatar_url = user.display_avatar.url
        await ctx.send(f'{avatar_url}')

async def setup(bot):
    await bot.add_cog(AvatarCommand(bot))
