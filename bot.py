
import discord
from discord.ext import commands, tasks
import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_NAME = os.getenv("CHANNEL_NAME", "王團時間表")
COMMAND_PREFIX = os.getenv("COMMAND_PREFIX", "\\")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

schedule_data = {
    "迷路的探路者": [
        ("每日", "22:10", "卡梅"),
        ("禮拜一", "21:40", "大米"),
        ("禮拜二", "22:15", "普坎"),
        ("禮拜三", "22:15", "混露"),
        ("禮拜四", "22:15", "混露"),
        ("禮拜六", "22:30", "史屋"),
        ("禮拜六", "20:30", "混露")
    ],
    "水豚君泡溫泉": [
        ("每日", "21:20", "卡梅"),
        ("禮拜一", "21:00", "小米"),
        ("禮拜二", "22:00", "史屋"),
        ("禮拜二", "22:15", "普坎"),
        ("禮拜三", "22:15", "混露"),
        ("禮拜四", "22:15", "混露")
    ]
}

@bot.event
async def on_ready():
    print(f'教會侍從上線囉！目前登入身份：{bot.user}')

@bot.command()
async def 查詢(ctx, *, 名字=None):
    if not 名字:
        await ctx.send("請提供要查詢的角色名稱，例如：`\查詢 迷路的探路者`")
        return
    if 名字 not in schedule_data:
        await ctx.send(f"未找到 {名字} 的打王記錄。")
        return
    embed = discord.Embed(title=f"{名字} 的打王時間", color=0x88ccff)
    for 頻率, 時間, 王名 in schedule_data[名字]:
        embed.add_field(name=f"{頻率}", value=f"{時間} 打 {王名}", inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)
