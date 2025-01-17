import discord
import config
import os
from realw_newbie.bot import bot, load_extension

try:
    if token := config.Bot['token']:
        load_extension()
        bot.run(token)
except discord.LoginFailure as e:
    print(f"토큰이 잘못되었습니다.\n\n{e.__class__.__name__}: {e}")
    os.system("pause")
except discord.PrivilegedIntentsRequired as e:
    print(f"Gateway Intents를 활성화 해주세요!\n\n{e.__class__.__name__}: {e}")
    os.system("pause")
