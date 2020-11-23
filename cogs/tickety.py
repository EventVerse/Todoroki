import discord
from discord.ext import commands

client = discord.Client()


class Tickety(commands.Cog):

    def __init__(self, client):
        self.client = client

    # cog sa uspesne nacital
    @commands.Cog.listener()
    async def on_ready(self):
        print("Tickety | ✅")

    # kod prikazu
    @commands.command()
    async def ticket(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title=f"Tvůj ticket byl vytvořený!", color=0xa47dff)
        await ctx.send(embed=embed, delete_after=3.0)

        guild = ctx.message.guild
        Role1 = guild.get_role(760145600288260135)
        Role2 = guild.get_role(760141416701362206)
        Role3 = guild.get_role(760145658040156180)
        User = ctx.author
        Bots = guild.get_role(760143211657953319)

        channel = await guild.create_text_channel("ticket-" +ctx.author.name, topic="#close_id")
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

        embed = discord.Embed(title=f"**Vítej v tvém ticketu, {ctx.author.name}**", color=0xa47dff)
        embed.add_field(name="Jak postupovat?",
                        value="Teď už máš ticket vytvořený, přichází ta těžší část.  Popiš nám tvůj problém. Zachvilku se ti někdo z AT bude věnovat!")
        embed.set_footer(text="Ticket může uzavřít pouze člen AT!", icon_url=self.client.user.avatar_url)

        await channel.send(embed=embed)

def setup(client):
    client.add_cog(Tickety(client))
