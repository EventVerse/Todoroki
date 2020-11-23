import discord
from discord.ext import commands

client = discord.Client()


class Tester(commands.Cog):

    def __init__(self, client):
        self.client = client

    # cog sa uspesne nacital
    @commands.Cog.listener()
    async def on_ready(self):
        print("NABOR_TESTER | ✅")

    # kod prikazu
    @commands.command()
    async def tester(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title=f"Tvůj nábor byl vytvořený!", color=0xb500c2)
        await ctx.send(embed=embed, delete_after=3.0)

        guild = ctx.message.guild
        Role1 = guild.get_role(760145600288260135)
        Role2 = guild.get_role(760141416701362206)
        Role3 = guild.get_role(760145658040156180)
        User = ctx.author
        Bots = guild.get_role(760143211657953319)

        channel = await guild.create_text_channel("tester-" +ctx.author.name)
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

        embed = discord.Embed(title=f"**Vítej v tvém náboru, {ctx.author.name}**", color=0xb500c2)
        embed.add_field(name="Odpověz na následující otázky:",
                        value="1. Proč chceš být Tester Eventů?\n2.Bude mít dostatek času na testování?\n(Test eventů bude tak 1 - 5 krát za týden)")
        embed.set_footer(text="Nábor může uzavřít pouze člen AT!", icon_url=self.client.user.avatar_url)

        await channel.send(embed=embed)

def setup(client):
    client.add_cog(Tester(client))
