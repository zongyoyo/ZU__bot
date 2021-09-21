import discord
from discord.ext import commands


#開啟特定事件的訂閱內容 (配合 discord 1.5 版更新)
intents = discord.Intents.all()
#intents.members = True #啟用 members 事件訂閱

#建立 bot 實體並放到 Bot 變數中
bot = commands.Bot(command_prefix = "!", intents = intents)
# prefix = str 當每次要呼叫此機器人時都須輸入該 str



# asayn 協成範本
# asayn def funcname(parameter_list):
#   "function event"

# 開機
#建立 bot 觸發性事件 
#當 被啟動時 將會執行下方的事件
@bot.event
async def on_ready():
    print(">> Bot is online <<")
    channel_state = bot.get_channel(889859748655136768) #取得聊天室(頻道) id
    await channel_state.send(">> Bot is online <<") #使用 await 去啟用 send 協成
    

#成員加入
#建立 bot 觸發性事件
#當 有成員加入時 將會執行下方的事件
@bot.event
async def on_member_join(member):
    #print(f"{member} join!") #使用 f字串 使 member 能維持在變數
    clannel_join = bot.get_channel(889852944185442365) #取得聊天室(頻道) id
    await clannel_join.send(f'{member} join!') #使用 await 去啟用 send 協成

#成員離開
#建立 bot 觸發性事件
#當 有成員加入時 將會執行下方的事件
@bot.event
async def on_member_remove(member):
    #print(f"{member} leave!") #使用 f字串 使 member 能維持在變數
    clannel_leave = bot.get_channel(889852978268364800) #取得聊天室(頻道) id
    await clannel_leave.send(f"{member} leave!") #使用 await 去啟用 send 協成

#附加 bot 專屬金鑰後啟動
bot.run("ODg5NDg2ODAxODM4OTQwMTgw.YUh9Iw.FrqzbHUKuV42nISrEr9MzCIStWY")