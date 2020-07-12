import discord
from discord.ext import commands

class Invite(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot