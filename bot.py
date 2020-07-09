import discord
from discord.ext import commands
from discord.ext.commands import has_any_role
import config
import logging
import os

bot = commands.Bot("!")
logger = logging.getLogger("vortrex.core")

bot.remove_command("help")


@bot.event
async def on_ready():
    logger.info("Launching Vortrex")
    bot.help_command = commands.MinimalHelpCommand()

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
    if not ctx.id == 297045071457681409:
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

try:
    bot.run(config.TOKEN)
except RuntimeError:
    pass
raise ConnectionAbortedError
