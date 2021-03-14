import discord, ctypes, webbrowser, json, os, time
from discord.ext import commands

with open('config.json', 'r', encoding="utf-8") as f:
    json.data = json.load(f)

bot = commands.Bot(command_prefix='')
bot.remove_command("help")
token = json.data['bot']['token']

cogs = [
    "newbie",
    "error",
    "ready"
]

try:
    if __name__ =='__main__':
        for extension in cogs:
            bot.load_extension('cogs.' + extension)
except Exception as e:
    ctypes.windll.user32.MessageBoxW(0, f"오류가 발생하였습니다.\n\n{e}", "Error", 0)

try:
    bot.run(token)
except discord.LoginFailure as e:
    ctypes.windll.user32.MessageBoxW(0, f"토큰을 제대로 적어주세요!\n\n{e}\n\n확인을 누르시면 토큰을 얻는 방법 웹 브라우저가 열립니다.", "Error", 0)
    webbrowser.open('https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs')
except discord.PrivilegedIntentsRequired as e:
    ctypes.windll.user32.MessageBoxW(0, f"Gateway Intents를 활성화 해주세요!\n\n{e}\n\n확인을 누르시면 활성화 방법 웹 브라우저가 열립니다.", "Error", 0)
    webbrowser.open('https://discordpy.readthedocs.io/en/latest/intents.html')
