from discord.ext import commands
import requests
import random


class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="choose")
    async def choose(self, ctx: commands.Context, *, msg: str):
        choice = random.choice(msg.split("|")).strip()
        await ctx.send(f"i choose: {choice}")

    @commands.command(name="catfact")
    async def catfact(sefl, ctx: commands.Context):
        res = requests.get("https://catfact.ninja/fact")
        data = res.json()
        await ctx.send(f"""# cat fact:
                        \r```
                        \r{data["fact"]}
                        \r```""")


async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))
