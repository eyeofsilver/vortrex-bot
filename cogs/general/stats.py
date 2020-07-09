from discord.ext import commands
from discord.ext.commands import has_any_role
from time import time
from utils.checks import is_dev
import discord
import json
import os


class Stats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ini_stats()
        self.start = time()
        self.socks = self.read_stats()
        self.event = 0
        self.opcod = {
            10: "Hello",
            11: "HEARTBEAT",
            9: "HI",
            7: "RECONNECT"
        }

    def ini_stats(self):
        if not os.path.exists("data/stats/sock.json"):
            with open("data/stats/sock.json", 'w') as f:
                json.dump({}, f)

    def write_stats(self, data: object):
        with open("data/stats/sock.json", 'w') as f:
            json.dump(data, f)

    def read_stats(self):
        with open("data/stats/sock.json") as f:
            return json.load(f)

    def update_stats(self):
        self.write_stats(self.socks)

    @commands.Cog.listener()
    async def on_socket_response(self, data):
        t = data["t"]
        if not t:
            try:
                t = self.opcod[data["op"]]
            except KeyError:
                pass #Need to implement error logging
        self.socks[t] = self.socks.get(t, 0) + 1
        self.event += 1
        if self.event % 25 == 0:
            self.update_stats()

    @commands.command(name="stats")
    async def stats(self, ctx):
        if not is_dev(ctx.author.id):
            return

        data = f"```json\n{json.dumps(self.socks, indent=2)}```"

        embed = discord.Embed(title="Raw Socket Stats", description=data)
        await ctx.channel.send(embed=embed)