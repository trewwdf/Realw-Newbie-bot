import pymysql, discord, json, datetime
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

class newbie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.author.bot:
                return None
            else:
                connection = pymysql.connect(host=host, user=username, password=password, database=basename, port=int(port), max_allowed_packet=2147483648, autocommit=True)
                cur = connection.cursor()

                if message.content.startswith("뉴비인증#"):
                    msg = message.content
                    ctx = message.channel
                    q = msg[5:]
                    try:
                        code = int(q)
                    except ValueError:
                        cur.close()
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
                        return cur.close()
                    elif len(q) == 0:
                        await ctx.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#3125122**')
                        return cur.close()
                    elif check is None:
                        await ctx.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#3125122**')
                        return cur.close()
                    elif check is None:
                        await ctx.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#3125122**')
                        return cur.close()
                    else:
                        if check1 is not None:
                            cur.execute(f'update {tablename} set state="1" where code="{code}"')
                            connection.commit()
                            await ctx.send(f'{message.author.mention}, 인증되었습니다. 게임의 "지원받기"에서 E키를 누르세요.')
                            await message.author.add_roles(discord.utils.get(message.guild.roles, id=int(newbiero)))
                            return cur.close()
                        elif check2 is not None:
                            await ctx.send(f'{message.author.mention}, 인증되었습니다. 게임의 "지원받기"에서 E키를 누르세요.')
                            await message.author.add_roles(discord.utils.get(message.guild.roles, id=int(newbiero)))
                            return cur.close()
                        elif check3 is not None:
                            await ctx.send(f'{message.author.mention}, 이미 인증되어있는 코드입니다.')
                            return cur.close()
                elif message.content.startswith(""):
                    if message.channel.id != int(newbiech):
                        return
                    await message.channel.send(f'{message.author.mention}, 올바르지 않은 입력. 예시처럼 띄어쓰기 없이 정확히 입력해주세요. 예시: **뉴비인증#3125122**')
                    return cur.close()
        except Exception as e:
            return await message.channel.send(f'{message.author.mention}, 오류가 발생하였습니다.\n`{e}`')


def setup(bot):
    bot.add_cog(newbie(bot))
