import discord
import webbrowser
import ctypes
from realw_newbie.bot import bot, token, load_extension

try:
    load_extension()
    bot.run(token)
except discord.LoginFailure as e:
    ctypes.windll.user32.MessageBoxW(0, f"토큰을 제대로 적어주세요!\n\n{e}\n\n확인을 누르시면 토큰 발급 방법 웹 브라우저가 열립니다.", "Error", 0)
    webbrowser.open('https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs')
    quit()
except discord.PrivilegedIntentsRequired as e:
    ctypes.windll.user32.MessageBoxW(0, f"Gateway Intents를 활성화 해주세요!\n\n{e}\n\n확인을 누르시면 활성화 방법 웹 브라우저가 열립니다.", "Error", 0)
    webbrowser.open('https://discordpy.readthedocs.io/en/latest/intents.html')
    quit()
