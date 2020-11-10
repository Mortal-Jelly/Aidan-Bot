import discord
from discord.ext import commands


class Join(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server!!')


def setup(client):
    client.add_cog(Join(client))
