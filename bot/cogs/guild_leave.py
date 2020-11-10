import discord
from discord.ext import commands


class GuildLeave(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, ctx, guild):
        await ctx.send(f'Aidan bot left {guild}')


def setup(client):
    client.add_cog(GuildLeave(client))
