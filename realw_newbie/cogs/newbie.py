import aiomysql, discord,
from discord.ext import commands
from realw_newbie.bot import json_data


host = json_data['database']['host']
basename = json_data['database']['basename']
tablename = json_data['database']['tablename']
username = json_data['database']['username']
password = json_data['database']['passwd']
port = json_data['database']['port']

newbiech = json_data['botsettings']['channel']
newbiero = json_data['botsettings']['role']

async def connect_mysql():
    connection = await aiomysql.connect(host=host, user=username, password=password, db=basename, port=int(port), autocommit=True)
    cur = await connection.cursor()
    return cur

class newbie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        ctx = message.channel

        try:
            if message.author.bot:
                return None
            else:
                if ctx.id != int(newbiech):
                    return
                else:
                    if message.content.startswith("뉴비인증#"):
                        cur = await connect_mysql()
                        
                        q = msg[5:]
                        try:
                            code = int(q)
                        except ValueError:
                            return await ctx.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#312512**')
                        

                        await cur.execute(f'select code from {tablename} where code="{code}"')
                        check = await cur.fetchone()

                        await cur.execute(f'select * from {tablename} where state="0" and code="{code}"')
                        check1 = await cur.fetchone()

                        await cur.execute(f'select * from {tablename} where state="1" and code="{code}"')
                        check2 = await cur.fetchone()

                        await cur.execute(f'select * from {tablename} where state="2" and code="{code}"')
                        check3 = await cur.fetchone()

                        if len(q) == 0:
                            return await ctx.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#312512**')
                        elif check is None:
                            return await ctx.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#312512**')
                        elif check is None:
                            return await ctx.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#312512**')
                        else:
                            if check1 is not None:
                                await cur.execute(f'update {tablename} set state="1" where code="{code}"')
                                await ctx.send(f'{message.author.mention}, 인증되었습니다. 게임의 "지원받기"에서 E키를 누르세요.')
                                return await message.author.add_roles(discord.utils.get(message.guild.roles, id=int(newbiero)))
                            elif check2 is not None:
                                await ctx.send(f'{message.author.mention}, 인증되었습니다. 게임의 "지원받기"에서 E키를 누르세요.')
                                return await message.author.add_roles(discord.utils.get(message.guild.roles, id=int(newbiero)))
                            elif check3 is not None:
                                return await ctx.send(f'{message.author.mention}, 이미 인증되어있는 코드입니다.')
                    elif message.content.startswith(""):
                        await ctx.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#312512**')
        except Exception as e:
            return await ctx.send(f'{message.author.mention}, 오류가 발생하였습니다.\n`{e}`')


def setup(bot):
    bot.add_cog(newbie(bot))
