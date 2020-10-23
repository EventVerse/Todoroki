import discord
from discord.ext import commands

client = discord.Client()


class Napady(commands.Cog):

    def __init__(self, client):
        self.client = client

    # cog sa uspesne nacital
    @commands.Cog.listener()
    async def on_ready(self):
        print("Nápady | ✅")

    # kod prikazu
    @commands.command()
    async def napad(self, ctx, *, link, amount=1):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title=f"Tvůj nápad byl zaznamenaný!", color=0xa47dff)
        await ctx.send(embed=embed, delete_after=5.0)

        channel = client.get_channel(760140761437438002)
        yes = "<:yes:767754158358659092>"
        no = "<:no:767754183444398101>"

        embed = discord.Embed(title="**Nápady**", color=0xa47dff, timestamp=ctx.message.created_at)
        embed.add_field(name="Hlasování o nápadu", value=link, inline=False)
        embed.set_footer(text=f"{self.client.user.name}", icon_url=self.client.user.avatar_url)

        msg = await channel.send(embed=embed)
        await msg.add_reaction(yes)
        await msg.add_reaction(no)


def setup(client):
    client.add_cog(Napady(client))
