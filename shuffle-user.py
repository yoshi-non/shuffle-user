import discord
import random
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True # メンバー管理の権限
intents.message_content = True # メッセージの内容を取得する権限
client = discord.Client(intents=intents)
TOKEN = os.environ.get('TOKEN')
@client.event
async def on_ready():
    print('Botがログインしました')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # ボット自身のメッセージには反応しない
    
    # 特定の値を排除する関数
    def remove_value(arr, value):
        return [x for x in arr if x != value]

    print(message.content)
    if ('/member' in message.content):
        members = message.guild.members
        member_names = [member.name for member in members]
        
        value_to_remove = "shuffle user"
        member_names = remove_value(member_names, value_to_remove)
        random.shuffle(member_names)
        output = '\n'.join(member_names)
        await message.channel.send(output)

client.run(TOKEN)
