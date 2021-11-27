import asyncio
from discord.ext import commands
from realw_newbie.bot import on_off_loop

class ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        user = await self.bot.fetch_user(user_id=720112607268307004)
        print(self.bot.user)
        print(self.bot.user.id)
        print(f'Newbie BOT has Ready.\nMade By {user}')

        await asyncio.create_task(on_off_loop())
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass

def setup(bot):
    bot.add_cog(ready(bot))
