import discord
import config
import sys, os
from discord.ext import commands
from realw_newbie.bot import connect_mysql

Table_name = config.Database['table_name']

class newbie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.author.bot:
                return None
            else:
                if message.channel.id != config.Settings['Channel']:
                    return
                else:
                    if message.content.startswith("뉴비인증#"):
                        cur = await connect_mysql()
                        
                        code_value = message.content[5:]
                        
                        try:
                            code = int(code_value)
                        except ValueError:
                            return await message.channel.send(config.Message['NotFound_Code'].format(message.author.mention, "예시: **뉴비인증#312512**"))
                        
                        await cur.execute(f'select code from {Table_name} where code = {code}',)
                        check = await cur.fetchone()

                        if len(code_value) == 0:
                            return await message.channel.send(config.Message['NotFound_Code'].format(message.author.mention, "예시: **뉴비인증#312512**"))
                        elif check is None:
                            return await message.channel.send(config.Message['NotFound_Code'].format(message.author.mention, "예시: **뉴비인증#312512**"))
                        else:
                            await cur.execute(f'select * from {Table_name} where state = "0" and code = {code}',)
                            check1 = await cur.fetchone()

                            await cur.execute(f'select * from {Table_name} where state = "1" and code = {code}',)
                            check2 = await cur.fetchone()

                            await cur.execute(f'select * from {Table_name} where state = "2" and code = {code}',)
                            check3 = await cur.fetchone()

                            if check1 is not None:
                                await cur.execute(f'update ? set state = "1" where code = {code}',)
                                await message.channel.send(config.Message['Success_Code'].format(message.author.mention))
                                return await message.author.add_roles(discord.utils.get(message.guild.roles, id=config.Settings['Role']))
                            elif check2 is not None:
                                await message.channel.send(config.Message['Success_Code'].format(message.author.mention))
                                return await message.author.add_roles(discord.utils.get(message.guild.roles, id=config.Settings['Role']))
                            elif check3 is not None:
                                return await message.channel.send(config.Message['Already_Code'].format(message.author.mention))
                    elif message.content.startswith(""):
                        await message.channel.send(config.Message['NotFound_Code'].format(message.author.mention, "예시: **뉴비인증#312512**"))
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno, exc_obj)
            return await message.channel.send(f'{message.author.mention}, 오류가 발생하였습니다.\n`{e.__class__.__name__}: {e}`')


def setup(bot):
    bot.add_cog(newbie(bot))
