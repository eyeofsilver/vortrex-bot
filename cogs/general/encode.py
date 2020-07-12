import discord
from discord.ext import commands

class Encode(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot