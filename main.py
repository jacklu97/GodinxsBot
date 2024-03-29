from discord.ext import commands, tasks
from discord.ext.commands.context import Context

import os
import asyncio
import discord
from discord import Color

from music_utils import give_link, download_vid, find_music_name, remove_all_files
from asyncio import sleep
from dotenv import load_dotenv

from music_cog import music_cog
from help_cog import help_cog

load_dotenv()

discord_key = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = "/", help_command=None, intents=intents)
# bot = commands.Bot(command_prefix = "/", intents=intents)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user} (ID: {bot.user.id})')
  print('------')


async def main():
  async with bot:
    await bot.remove_cog("help")

    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))

    await bot.start(discord_key)

asyncio.run(main())

# @bot.event
# async def on_ready():
#   try:
#     print("Discord bot successfully connected")
#   except:
#     print("[!] Couldn't connect, an Error ocurred")

# @bot.command()
# async def pause(ctx: Context):
#   if ctx.voice_client and ctx.voice_client.is_playing():
#     ctx.voice_client.pause()
#     await ctx.send("Playback paused.")
#   else:
#     await ctx.send("[-] An error ocurred: You have to be in voice channel to use this command")

# @bot.command()
# async def resume(ctx: Context):
#   if (ctx.voice_client and ctx.voice_client.is_paused()):
#     ctx.voice_client.resume()
#     await ctx.send("Playback resumed.")
#   else:
#     await ctx.send("[-] An error ocurred: You have to be in voice channel to use this command")

# @bot.command()
# async def leave(ctx: Context):
#   if ctx.voice_client:
#     await ctx.guild.voice_client.disconnect()
#     await ctx.send("Left the voice channel")
#     sleep(1)
#     remove_all_files("music")
#   else:
#     await ctx.send("[-] An error ocurred: You have to be in voice channel to use this command")

# @bot.command()
# async def join(ctx: Context):
#   if ctx.author.voice:
#     channel = ctx.message.author.voice.channel
#     try:
#       await channel.connect()
#     except:
#       await ctx.send("[-] An error ocurred: Couldn't connect to the channel")
#   else:
#     await ctx.send("[-] An error ocurred: You have to be in voice channel to use this command")

# @bot.command(name = "play")
# async def play(ctx: Context, *, title: str):
#   download_vid(title)
#   voice_channel = ctx.author.voice.channel

#   if not ctx.voice_client:
#     voice_channel = await voice_channel.connect()

#   try:
#     async with ctx.typing():
#       player = discord.FFmpegPCMAudio(executable="/usr/bin/ffmpeg", source=f"music/{find_music_name()}",)
#       guild = ctx.message.guild
#       voice_client = guild.voice_client

#       voice_client.play(player, after=lambda e: print("Player error %s" % e) if e else None)
#       voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
    
#     await ctx.send(f"Now playing: {find_music_name()}")

#     while ctx.voice_client.is_playing():
#       await sleep(1)
#     # delete_selected_file(find_music_name())
#   except Exception as e:
#     await ctx.send(f"Error: {e}")



# bot.run(discord_key)