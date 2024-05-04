import discord
import sqlite3
from random import sample
import random
import asyncio
import datetime
import requests
from typing import Optional
from dotenv import load_dotenv
import os
#client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


load_dotenv()

TOKEN = os.getenv("TOKEN")
if TOKEN is None:
    print("錯誤：找不到 Discord 令牌。請設置 TOKEN 環境變數。")

# 在客戶端準備好時執行的事件處理程


@client.event
async def on_ready():
  print('目前登入身份：', client.user)
  


@client.event
async def on_message(message):
  #排除自己的訊息，避免陷入無限循環
  if message.author == client.user:
    return


  if message.channel != 'sever':
    # 獲取要發言的頻道
    channel = client.get_channel(1232331488528171129)  # 替換 YOUR_CHANNEL_ID 為目標頻道的 ID

    
    nickname = message.author.nick or message.author.name
    random3_int = random.randint(0, 255)
    random4_int = random.randint(0, 255)
    random5_int = random.randint(0, 255)
    emb_color = discord.Color.from_rgb(random3_int, random4_int, random5_int)
    embed = discord.Embed(title='監測訊息',
                          description=f'{message.content}',
                          color=emb_color,
                          timestamp=datetime.datetime.now())
    embed.add_field(name='發送人', value=nickname, inline=False)
    embed.add_field(name='發送頻道', value=message.channel, inline=False)
    embed.add_field(name='發送伺服器', value=message.guild.name, inline=False)
    await channel.send(embed=embed)
    if message.attachments:
      for attachment in message.attachments:
        # 發送圖片連結
        await channel.send(attachment.url)
  
  if message.content == 'sever' :
      guilds = client.guilds
      for guild in guilds:
            print(f"{guild.name}")



# 啟動機器人
client.run(TOKEN)
