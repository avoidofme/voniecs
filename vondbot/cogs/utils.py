from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping", description="check bot's latency")
    async def ping(self, ctx: commands.Context) -> None:
        """check bot's latency"""
        await ctx.send(f"Pong! 🏓 ({round(self.bot.latency * 1000)}ms)")

    @commands.command(name="say")
    async def say(self, ctx: commands.Context, *, msg: str) -> None:
        await ctx.send(msg)


async def setup(bot: commands.Bot):
    await bot.add_cog(Utils(bot))
