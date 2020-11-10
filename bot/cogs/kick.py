import discord
from discord.ext import commands


class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'<@{member.id}> was kicked for {reason}')


def setup(client):
    client.add_cog(Kick(client))
