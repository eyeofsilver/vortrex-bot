import discord
from discord.ext import commands

from time import time


class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
