
from core.classes import Cog_Extension
import discord
from discord.ext import commands
import json
import random

with open("setting.json", mode="r", encoding="utf-8") as json_file:
    setting = json.load(json_file)

def game_rewrite(key, a):
    with open("gamedata_21.json", mode="r", encoding="utf-8") as json_file:
        game = json.load(json_file)

    game[key]=a #只是修改變數資料  

    with open("gamedata_21.json", mode="w", encoding="utf-8") as json_file:
        game=json.dump(game,json_file)

def game_addwrite(key, a):
    with open("gamedata_21.json", mode="r", encoding="utf-8") as json_file:
        game = json.load(json_file)

    game[key]=game[key] + [a]  #只是修改變數資料  

    with open("gamedata_21.json", mode="w", encoding="utf-8") as json_file:
        game=json.dump(game,json_file)

def load(key):
    with open("gamedata_21.json", mode="r", encoding="utf-8") as json_file:
        game = json.load(json_file)
        return game[key]

def count(key):
    point = load(key)
    x = 0
    for i in range(len(point)):
        x += point[i]
    return x



class Point21(Cog_Extension):
    
    @commands.command() 
    async def 規則(self, ctx):
        with open("21rule.txt", mode="r", encoding="utf-8") as data:
            file = data.read()
        await ctx.send(file)

    @commands.command() 
    async def reset(self, ctx):
        game_rewrite("Pl", [])
        game_rewrite("Bt", [])
        await ctx.send("Game reset done!")
    
    @commands.command() 
    async def start(self, ctx):
        await ctx.send("~白家回合~")
        await ctx.send("~發牌~")
        point = []
        for i in random.choices(range(1,12),k=2):
            point += [i]
        game_rewrite("Pl", point)
        await ctx.send(load("Pl"))

    @commands.command() 
    async def draw(self, ctx):
        card = random.choice(range(1,12))
        game_addwrite("Pl", card)
        await ctx.send(load("Pl"))

    @commands.command() 
    async def account(self, ctx):
        await ctx.send("~白家回合結束~")
        await ctx.send("~莊家回合~")
        await ctx.send("~發牌~")
        point = []
        for i in random.choices(range(1,12),k=2):
            point += [i]
        game_rewrite("Bt", point)
        await ctx.send(load("Bt"))
        if count("Bt") <= 15:
            await ctx.send("莊家補牌")
            card = random.choice(range(1,12))
            game_addwrite("Bt", card)
            await ctx.send(load("Bt"))
        await ctx.send("~莊家回合結束~")
        await ctx.send("--------------")
        await ctx.send("結算")
        pt = 0
        bt = 0
        pt = count("Pl")
        bt = count("Bt")
        b = load("Bt")
        p = load("Pl")
        await ctx.send(f"莊家牌{b}")
        await ctx.send(f"莊家點數總和{bt}")
        await ctx.send(f"白家牌{p}")
        await ctx.send(f"白家點數總和{pt}")
        await ctx.send("--------------")
        
        if bt<=21:
            if pt<=21:
                if bt>pt:
                    await ctx.send("~莊家獲勝~")
                elif bt==pt:
                    await ctx.send("~和局~")
                elif bt<pt:
                    await ctx.send("~莊家爆牌, 白家獲勝~")
            elif pt>21:
                await ctx.send("~白家爆牌, 莊家獲勝~")    
        elif bt>21:
            await ctx.send("~莊家爆牌, 白家獲勝~")

        

#設定 setup 函式
def setup(bot):
    bot.add_cog(Point21(bot)) # 將 Main 的 Cog 放入 bot 實體中