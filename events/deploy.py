import discord
from discord.ext import commands

async def setup(bot):
    try:
        await bot.tree.sync()  
        print("スラッシュコマンド登録完了")
    except Exception as e:
        print(f"スラッシュコマンド登録失敗: {e}")
