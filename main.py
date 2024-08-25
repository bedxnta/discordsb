import discord
from discord.ext import commands
import os
import asyncio

TOKEN = "YOUR TOKEN HERE"

bot = commands.Bot(command_prefix=';', self_bot=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_command_error(ctx, error):
    """Handles errors and sends a custom message for unknown commands."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'**Unknown command: **`{ctx.message.content[1:]}`')
    else:
        print(f'Error: {error}')

async def load_extensions():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py') and filename != '__init__.py':
            try:
                await bot.load_extension(f'commands.{filename[:-3]}')
                print(f'Loaded {filename}')
            except Exception as e:
                print(f'Failed to load {filename}: {e}')

async def main():
    await load_extensions()
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
