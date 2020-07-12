import discord
from discord.ext import commands

from utils.cooldown import Cooldown, CooldownError
from utils.checks import is_dev

class Encode(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.cooldown = Cooldown()

    async def cool(self, ctx: commands.Context) -> None:
        if self.cooldown.expired() or is_dev(ctx.author.id):
            self.cooldown.reinit()
            return
        else:
            await ctx.channel.send(f"Global cooldown remaining on encode commands is {round(self.cooldown.getremain())} seconds.")
            raise CooldownError("Global cooldown for encode commands is still active.")

    @commands.group(name="encode")
    async def encode(self, ctx):
        pass

    @encode.command(name="txtint")
    async def txtint(self, ctx, *text):
        await self.cool(ctx)
        text = " ".join(text)
        nums = [ord(char) for char in text]
        await ctx.channel.send(f"{nums}"[:1500])