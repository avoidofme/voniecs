import discord
from discord.ext import commands


class Von(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(
            intents=intents, command_prefix=["v ", "v"], status=discord.Status.idle
        )

    async def setup_hook(self) -> None:
        await self.load_extension("cogs.utils")
        await self.load_extension("cogs.fun")
