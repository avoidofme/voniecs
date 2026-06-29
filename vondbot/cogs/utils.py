from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ping", description="check bot's latency")
    async def ping(self, ctx: commands.Context) -> None:
        """check bot's latency"""
        await ctx.send(f"Pong! 🏓 ({round(self.bot.latency * 1000)}ms)")

    @commands.command(name="say")
    async def say(self, ctx: commands.Context, *, msg: str) -> None:
        """say what you say"""
        await ctx.send(msg)

    @commands.command(name="avatar")
    async def avatar(self, ctx: commands.Context) -> None:
        """get your avatar"""
        avatar_url = ctx.author.display_avatar.with_size(1024).url
        await ctx.send(avatar_url)

    @commands.command(name="profile")
    async def profile(self, ctx: commands.Context) -> None:
        await ctx.send("profile command")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Utils(bot))
