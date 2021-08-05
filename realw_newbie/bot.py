import discord, ctypes, json
from discord.ext import commands

f = open('config.json', 'r', encoding="utf-8")
json_data = json.load(f)

bot = commands.Bot(command_prefix='', help_command=None)
token = json_data['bot']['token']

cogs = [
    "newbie",
    "events"
]

def load_extension():
    try:
        for extension in cogs:
            bot.load_extension('realw_newbie.cogs.' + extension)
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, f"오류가 발생하였습니다.\n\n{e}", "Error", 0)
        quit()
