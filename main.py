import random
import requests
import youtube_dl
import discord
import json
import os
import dotenv

from discord.ext import commands
from dotenv import load_dotenv


client = discord.Client()
client = commands.Bot(command_prefix="!")
client.remove_command("help")
load_dotenv()
TOKEN = os.getenv('TOKEN')



@client.event  # zaciatok
async def on_ready():
    print("-------------------------")
    print("Bot Name: " + client.user.name)
    print(client.user.id)
    print("API Version: " + discord.__version__)
    print(client.latency * 1000)
    print("-------------------------")

    # guild_members = len(set(client.get_all_members()))
    # await client.change_presence(activity=discord.Game(name='with {} users!'.format(guild_members)))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="EventVerse"))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="<:9830_no:748426943766069308> **You don't have enough permissions to execute this command!**",
            color=0xe21830)
        await ctx.send(embed=embed)
    else:
      raise error

    if isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(
            title="<:9830_no:748426943766069308> **Bot doesn't have enough permission to execute this command!**",
            color=0xe21830)
        await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title=f'Loaded `{extension}`!', color=0xe21830)
    await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(title=f'Unloaded `{extension}`!', color=0xe21830)
    await ctx.send(embed=embed)


@client.command(
    name='reload', description="Reload all/one of the bots cogs!"
)
@commands.is_owner()
async def reload(ctx, cog=None):
    if not cog:
        # No cog, means we reload all cogs
        async with ctx.typing():
            embed = discord.Embed(
                title="Reloading all cogs!",
                color=0xe21830,
                timestamp=ctx.message.created_at
            )
            for ext in os.listdir("./cogs/"):
                if ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        client.unload_extension(f"cogs.{ext[:-3]}")
                        client.load_extension(f"cogs.{ext[:-3]}")
                        embed.add_field(
                            name=f"Reloaded: `{ext}`", value='\uFEFF', inline=False)
                    except Exception as e:
                        embed.add_field(
                            name=f"Failed to reload: `{ext}`", value=e, inline=False)
                    await asyncio.sleep(0.5)
            await ctx.send(embed=embed)
    else:
        # reload the specific cog
        async with ctx.typing():
            embed = discord.Embed(
                title="Reloading all cogs!",
                color=0xe21830,
                timestamp=ctx.message.created_at
            )
            ext = f"{cog.lower()}.py"
            if not os.path.exists(f"./cogs/{ext}"):
                # if the file does not exist
                embed.add_field(
                    name=f"Failed to reload: `{ext}`",
                    value="This cog does not exist.",
                    inline=False
                )

            elif ext.endswith(".py") and not ext.startswith("_"):
                try:
                    client.unload_extension(f"cogs.{ext[:-3]}")
                    client.load_extension(f"cogs.{ext[:-3]}")
                    embed.add_field(
                        name=f"Reloaded: `{ext}`", value='\uFEFF', inline=False)
                except Exception:
                    desired_trace = traceback.format_exc()
                    embed.add_field(
                        name=f"Failed to reload: `{ext}`", value=desired_trace, inline=False)
            await ctx.send(embed=embed)


for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
async def navrh(ctx, *, link, amount=1):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title=f"Tvoj návrh bol zaznamenaný!", color=0xa47dff)
    await ctx.send(embed=embed, delete_after=5.0)

    channel = client.get_channel(760140761437438002)
    yes = "<:yes:767754158358659092>"
    no = "<:no:767754183444398101>"

    embed = discord.Embed(title="**Návrhy**", color=0xa47dff, timestamp=ctx.message.created_at)
    embed.add_field(name="Hlasovanie o návrhu", value=link, inline=False)
    embed.set_footer(text=f"{client.user.name}", icon_url=client.user.avatar_url)

    msg = await channel.send(embed=embed)
    await msg.add_reaction(yes)
    await msg.add_reaction(no)

@client.command()
async def new(ctx, amount=1):
  await ctx.channel.purge(limit=amount)
  embed = discord.Embed(title=f"Tvoj ticket bol vytvorený!", color=0xa47dff)
  await ctx.send(embed=embed, delete_after=3.0)
  

  guild = ctx.message.guild
  Role1 = guild.get_role(760145600288260135)
  Role2 = guild.get_role(760141416701362206)
  Role3 = guild.get_role(760145658040156180)
  User = ctx.author
  Bots = guild.get_role(760143211657953319)

  channel = await guild.create_text_channel("ticket")
  overwrites = {
    guild.default_role: discord.PermissionOverwrite(
      read_messages=False,
      send_messages=False,
    ),
    Role1: discord.PermissionOverwrite(
      read_messages=True,
      send_messages=True,
    ),
    Bots: discord.PermissionOverwrite(
      read_messages=True,
      send_messages=True,
    ),
    Role2: discord.PermissionOverwrite(
      read_messages=True,
      send_messages=True,
    ),
    Role3: discord.PermissionOverwrite(
      read_messages=True,
      send_messages=True,
    ),
    User: discord.PermissionOverwrite(
      read_messages=True,
      send_messages=True,
    )
  }

  
  await channel.edit(overwrites=overwrites)


  embed = discord.Embed(title=f"**Vitaj v tvojom tickete, {ctx.author.name}**", color=0xa47dff)
  embed.add_field(name="Ako postupovať?", value="Teraz, keď už máš vytvorený ticket, prichádza tá ťažšia časť.  Popíš nám tvoj problém. O malú chvílu sa ti bude niekto z AT venovať!")
  embed.set_footer(text="Ticket môže zavrieť iba člen AT!", icon_url=client.user.avatar_url)

  await channel.send(embed=embed)


client.run(TOKEN)
