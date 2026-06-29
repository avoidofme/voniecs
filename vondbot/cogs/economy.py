from discord.ext import commands


class Economy(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="balance")
    async def balance(self, ctx: commands.Context) -> None:
        """check your balance, but not yet"""
        await ctx.send("balance command")

    @commands.command(name="collect")
    async def collect(self, ctx: commands.Context) -> None:
        """collect your income, but not yet"""
        await ctx.send("collect command")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Economy(bot))
