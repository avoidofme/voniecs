from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", description="check bot's latency")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong! 🏓 ({round(self.bot.latency * 1000)}ms)")


async def setup(bot: commands.Bot):
    await bot.add_cog(Utils(bot))
