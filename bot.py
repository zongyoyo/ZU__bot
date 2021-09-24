import discord
from discord.ext import commands
import json
import random


with open("setting.json", mode="r", encoding="utf-8") as json_file:
    setting = json.load(json_file)
with open("command_list.txt", mode="r", encoding="utf-8") as txt_file:
    cmd_list = txt_file.read()
#print(setting_data)
#開啟特定事件的訂閱內容 (配合 discord 1.5 版更新)
intents = discord.Intents.all()
#intents.members = True #啟用 members 事件訂閱

#建立 bot 實體並放到 Bot 變數中
bot = commands.Bot(command_prefix = "!", intents = intents)
# prefix = str 當每次要呼叫此機器人時都須輸入該 str




# asayn 協成範本
# asayn def funcname(parameter_list):
#   "function event"


#建立 bot 觸發性事件 

#啟動
@bot.event
async def on_ready():
    print(">> Bot is online <<")
    channel_state = bot.get_channel(setting["State_channel"]) #取得聊天室(頻道) id
    await channel_state.send(">> Bot is online <<") #使用 await 去啟用 send 協成
    
#成員加入
@bot.event
async def on_member_join(member):
    #print(f"{member} join!") #使用 f字串 使 member 能維持在變數
    clannel_join = bot.get_channel(setting["Welcome_channel"]) #取得聊天室(頻道) id
    await clannel_join.send(f'{member} join!') #使用 await 去啟用 send 協成

#成員離開
@bot.event
async def on_member_remove(member):
    #print(f"{member} leave!") #使用 f字串 使 member 能維持在變數
    clannel_leave = bot.get_channel(setting["Leave_channel"]) #取得聊天室(頻道) id
    await clannel_leave.send(f"{member} leave!") #使用 await 去啟用 send 協成



#建立 bot 指令

#command_list
@bot.command()
async def command_list(ctx):
    await ctx.send(cmd_list) #使用 await 去啟用 send 協成

#ping
@bot.command()
async def ping(ctx): # ctx(使用者, id, 所在伺服器, 所在頻道)
    # ctx = context(上下文)
    # A: 嗨 (上文) => 將附加 (使用者, id, 所在伺服器, 所在頻道) 等資訊
    # B: 安安 (下文)
    await ctx.send(f"延遲:{round(bot.latency*1000)}ms") #根據該 ctx 送出 bot 的 latency(延遲)
    # 1s(秒) = 1000ms(毫秒) 
    #運用 f 字串發出 ( {} 中任為變數)
    # round() 讓小數點後的數四捨五入


#stop
@bot.command()
async def stop(ctx):
    channel_state = bot.get_channel(setting["State_channel"])
    await channel_state.send(">> Bot is offline <<") #使用 await 去啟用 send 協成
    await bot.logout() #使 bot 登出(關閉迴圈)

#picture_jpg
@bot.command()
async def pic_fish(ctx):
    #發送 jpg 圖片
    #運用 discord.File 來宣告圖片檔
    pic_jpg = discord.File(setting["fish.jpg"])
    await ctx.send(file= pic_jpg) #利用 send 發送 file(pic_jpg)

#picture_png
@bot.command()
async def pic_teacher(ctx):
    #發送 png 圖片
    #運用 discord.File 來宣告圖片檔
    pic_png = discord.File(setting["teacher.png"])
    await ctx.send(file= pic_png) #利用 send 發送 file(pic_png)

#picture_gif
@bot.command()
async def pic_bird(ctx):
    #發送 png 圖片
    #運用 discord.File 來宣告圖片檔
    pic_gif = discord.File(setting["bird.gif"])
    await ctx.send(file= pic_gif) #利用 send 發送 file(pic_gif)

#picture_random
@bot.command()
async def 鯊鯊(ctx):
    #利用 choice() 隨機選取圖片
    random_pic = discord.File(random.choice(setting["sharks"]))
    await ctx.send(file= random_pic) #利用 send 發送 file(pic_gif)

# #附加 bot 專屬金鑰後啟動
bot.run(setting["Token"])

