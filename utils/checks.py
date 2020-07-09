import discord
from discord.ext import commands
import config

def is_dev(uid: int):
    if uid in config.DEVS:
        return True
    return False