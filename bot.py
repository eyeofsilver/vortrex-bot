import discord
from discord.ext import commands
from discord.ext.commands import has_any_role
import config
import logging
import os
from utils.checks import is_dev

bot = commands.Bot(command_prefix=["%%", "v!"])
logger = logging.getLogger("vortrex.core")
logger.setLevel(logging.DEBUG)

bot.remove_command("help")

if not os.path.exists("data/"):
    os.makedirs("data/stats")
    os.makedirs("data/persist")
    os.makedirs("data/temp")

@bot.event
async def on_ready():
    logger.info("Launching Vortrex")

    for cog in os.listdir("cogs/"):
        if not cog.endswith(".py"):
            continue
        cog = cog[:-3]
        logger.debug(f"Loading {cog}")
        try:
            bot.load_extension("cogs." + cog)
        except:
            logger.error(f"Failed to load cog {cog}", exc_info=True)

@bot.command(name="reload")
async def reload(ctx):
    if not ctx.author.id in config.DEVS:
        return

    logger.info("Reloading Vortrex")

    for cog in os.listdir("cogs/"):
        if not cog.endswith(".py"):
            continue
        cog = cog[:-3]
        logger.debug(f"Reloading {cog}")
        try:
            bot.reload_extension("cogs." + cog)
        except:
            logger.error(f"Failed to reload cog {cog}", exc_info=True)

@bot.command(name="restart")
async def restart(ctx):
    if not ctx.author.id in config.DEVS:
        return

    await bot.logout()

try:
    bot.run(config.TOKEN)
except RuntimeError:
    pass
raise ConnectionAbortedError
