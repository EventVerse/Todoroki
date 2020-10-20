import discord
from discord.ext import commands

client = discord.Client()


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Help.py loaded")

    # command
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title=" ", colour=0xa47dff)
        embed.set_author(name="EventVerse!", icon_url="https://media.discordapp.net/attachments/760140061516890132/764853762383937566/finalEV.gif")
        embed.add_field(name="Ticket", value="`new` | `lock` | `close`", inline=False)
        embed.add_field(name="Návrhy", value="`navrh`", inline=False)
        embed.add_field(name="Developer only", value="`load` | `unload` | `reload`", inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
