from core.classes import Cog_Extension
import discord
from discord.ext import commands
import json

with open("setting.json", mode="r", encoding="utf-8") as json_file:
    setting = json.load(json_file)


#建立 Main 的 Cog
class Main(Cog_Extension):
    
    #ping
    @commands.command() # @bot.command() 要改為 @commands.commamd()
    async def ping(self, ctx):  
        await ctx.send(f"延遲:{round(self.bot.latency*1000)}ms")

    #stop
    @commands.command()
    async def stop(self, ctx):
        channel_state = self.bot.get_channel(setting["State_channel"])
        await channel_state.send(">> Bot is offline <<") #使用 await 去啟用 send 協成
        await self.bot.logout() #使 bot 登出(關閉迴圈)



#設定 setup 函式
def setup(bot):
    bot.add_cog(Main(bot)) # 將 Main 的 Cog 放入 bot 實體中