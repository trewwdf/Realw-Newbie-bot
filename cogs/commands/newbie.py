import pymysql, discord, json, datetime
from discord.ext import commands

with open('config.json', 'r', encoding="utf-8") as f:
    json.data = json.load(f)


host = json.data['database']['host']
basename = json.data['database']['basename']
tablename = json.data['database']['tablename']
username = json.data['database']['username']
password = json.data['database']['passwd']
port = json.data['database']['port']

newbiech = json.data['botsettings']['channel']
newbiero = json.data['botsettings']['role']

connection = pymysql.connect(host=host, user=username, password=password, database=basename, port=int(port), max_allowed_packet=2147483648, autocommit=True)
cur = connection.cursor()

class newbie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.author.bot:
                return None
            else:
                if message.content.startswith("뉴비인증#"):
                    msg = message.content
                    ctx = message.channel
                    q = msg[5:]
                    try:
                        code = int(q)
                    except ValueError:
                        return await ctx.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#3125122**')
                    cur.execute(f'select code from {tablename} where code="{code}"')
                    check = cur.fetchone()
                    cur.execute(f'select * from {tablename} where state="0" and code="{code}"')
                    check1 = cur.fetchone()
                    cur.execute(f'select * from {tablename} where state="1" and code="{code}"')
                    check2 = cur.fetchone()
                    cur.execute(f'select * from {tablename} where state="2" and code="{code}"')
                    check3 = cur.fetchone()
                    if message.channel.id != int(newbiech):
                        pass
                        return
                    elif len(q) == 0:
                        return await ctx.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#3125122**')
                    elif check is None:
                        return await ctx.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#3125122**')
                    else:
                        if check1 is not None:
                            cur.execute(f'update {tablename} set state="1" where code="{code}"')
                            await ctx.send(f'{message.author.mention}, 인증되었습니다. 게임의 "지원받기"에서 E키를 누르세요.')
                            return await message.author.add_roles(discord.utils.get(message.guild.roles, id=int(newbiero)))
                        elif check2 is not None:
                            await ctx.send(f'{message.author.mention}, 인증되었습니다. 게임의 "지원받기"에서 E키를 누르세요.')
                            return await message.author.add_roles(discord.utils.get(message.guild.roles, id=int(newbiero)))
                        elif check3 is not None:
                            return await ctx.send(f'{message.author.mention}, 이미 인증되었습니다.')
                elif message.content.startswith(""):
                    if message.channel.id != int(newbiech):
                        pass
                        return
                    return await message.channel.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#3125122**')
        except Exception as e:
            return await message.channel.send(f'{message.author.mention}, 오류가 발생하였습니다.\n`{e}`')


def setup(bot):
    bot.add_cog(newbie(bot))
