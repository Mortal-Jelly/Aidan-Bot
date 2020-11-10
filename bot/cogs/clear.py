import discord
from discord.ext import commands
import time
from time import sleep


class Clear(commands.Cog):

    def __init__(self, client, ):
        self.client = client

    @commands.command(aliases=['clear', 'purge'], help='Deletes the number of message specified')
    @commands.has_permissions(administrator=True)
    async def _clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'{amount} messages were deleted!')
        sleep(2)
        await ctx.channel.purge(limit=1)


def setup(client):
    client.add_cog(Clear(client))
