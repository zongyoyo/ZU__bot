import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open("setting.json", mode="r", encoding="utf-8") as json_file:
    setting = json.load(json_file)

class React(Cog_Extension):

    #picture_jpg
    @commands.command()
    async def pic_fish(self, ctx):
        #發送 jpg 圖片
        #運用 discord.File 來宣告圖片檔
        pic_jpg = discord.File(setting["fish.jpg"])
        await ctx.send(file= pic_jpg) #利用 send 發送 file(pic_jpg)

    #picture_png
    @commands.command()
    async def pic_teacher(self, ctx):
        #發送 png 圖片
        #運用 discord.File 來宣告圖片檔
        pic_png = discord.File(setting["teacher.png"])
        await ctx.send(file= pic_png) #利用 send 發送 file(pic_png)

    #picture_gif
    @commands.command()
    async def pic_bird(self, ctx):
        #發送 png 圖片
        #運用 discord.File 來宣告圖片檔
        pic_gif = discord.File(setting["bird.gif"])
        await ctx.send(file= pic_gif) #利用 send 發送 file(pic_gif)

    #picture_random
    @commands.command()
    async def 鯊鯊(self, ctx):
        #利用 choice() 隨機選取圖片
        random_pic = discord.File(random.choice(setting["sharks"]))
        await ctx.send(file= random_pic) #利用 send 發送 file(pic_gif)



#設定 setup 函式
def setup(bot):
    bot.add_cog(React(bot)) # 將 Main 的 Cog 放入 bot 實體中