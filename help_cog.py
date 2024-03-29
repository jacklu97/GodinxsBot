import discord
from discord.ext import commands

class help_cog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

    self.help_message = """
```
General commands:
/help - displays all the available commands
/p <keywords> - finds the song on youtube and plays it in your current channel. Will resume the reproduction if paused
/q - displays the current music queue
/skip - skips the current song played
/clear - stops the music and clears the queue
/leave - disconnects the bot from the voice channel
/pause - pauses the current song being played or resumes if already paused
/resume - resumes playing the current song
```
"""
    self.text_channel_text = []

  @commands.Cog.listener()
  async def on_guild_join(self):
    for guild in self.bot.guilds:
      for channel in guild.text_channels:
        self.text_channel_text.append(channel)
    
    await self.send_to_all(self.help_message)

  async def send_to_all(self, msg):
    for text_channel in self.text_channel_text:
      await text_channel.send(msg)

  @commands.command(name="help", help="Displays all the available commands")
  async def help(self, ctx: commands.context.Context):
    await ctx.send(self.help_message)