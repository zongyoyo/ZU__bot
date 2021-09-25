import discord
from discord.ext import commands
import json
import os


with open("setting.json", mode="r", encoding="utf-8") as json_file:
    setting = json.load(json_file)



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

#設定 Cog 讀取與程式的重新載入

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cmds.{extension}") #運用內建 load_extension() 函示
    await ctx.send(f"Loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cmds.{extension}") #運用內建 unload_extension() 函示
    await ctx.send(f"Unloaded {extension} done.")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cmds.{extension}") #運用內建 reload_extension() 函示
    await ctx.send(f"Reloaded {extension} done.")


#建立 bot 指令
    #已改用 Cog 處理


for filename in os.listdir("./cmds"): 
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")


if __name__ == "__main__":
    # #附加 bot 專屬金鑰後啟動
    bot.run(setting["Token"])

