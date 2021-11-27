import aiomysql
import config
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='', help_command=None)

def load_extension():
    try:
        for extension in os.listdir("realw_newbie/cogs/"):
            bot.load_extension('realw_newbie.cogs.' + extension)
    except Exception as e:
        print(f"오류가 발생하였습니다.\n\n{e.__class__.__name__}: {e}")
        os.system("pause")

async def connect_mysql():
    connection = await aiomysql.connect(host=config.Database_Connect['host'], user=config.Database_Connect['username'], password=config.Database_Connect['password'], db=config.Database_Connect['basename'], port=config.Database_Connect['port'], autocommit=True)
    cur = await connection.cursor()
    return cur