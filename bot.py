# import these :)
import discord
from discord.ext import commands

# Add prefix (needed) and a description! (optional)
bot = commands.Bot(command_prefix="{PREFIX}", description="{DESCRIPTION}")

# When the bot is ready...
@bot.event()
async def on_ready(ctx):
  print('Ready!')
 
# Here is how you do a responder command!
@bot.command()
async def ping(ctx)
  await ctx.channel.send('Pong!')
  
bot.run('TOKEN')
