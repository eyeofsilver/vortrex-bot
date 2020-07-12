from discord.ext import commands

from .general import general, stats, encode

def setup(bot: commands.Bot):
    bot.add_cog(general.General(bot))
    bot.add_cog(stats.Stats(bot))
    bot.add_cog(encode.Encode(bot))