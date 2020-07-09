from discord.ext import commands

from .general import general

def setup(bot: commands.Bot):
    bot.add_cog(general.General(bot))