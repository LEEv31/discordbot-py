import discord
import asyncio
from discord.ext import commands
from discord import Embed
import os

intents = discord.Intents.all()

TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix='/',intents=intents)

x = ["X","X","X","X","X"]
y = ["X","X","X","X","X"]
i = 0
k = 0
a = ""
mmm = ""

@bot.command()
async def 레이드(ctx, *, message=None):
    if ctx.message.author.guild_permissions.administrator or ctx.message.author.name == "숯미남":
        global a
        a = message
        global abc
        global msg
        abc = Embed(title="레이드 길드 팟", description=a)
        abc.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
        abc.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
        msg = await ctx.send(embed=abc)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("⚠️")
     else:
        await ctx.send('임원이 아닙니다.')
@bot.command()
async def 레이드수정(ctx, *, mmm=None):
        global msg
        a=mmm
        abv = Embed(title="레이드 길드 팟", description=a)
        abv.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
        abv.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
        await msg.edit(embed=abv)
    
@bot.event
async def on_reaction_add(reaction, user):
        global msg
        if user.bot == 1:
            return None
        if str(reaction.emoji) == "1️⃣":
                x.insert(i,user.name)
                abd = Embed(title="레이드 길드 팟", description=a)
                abd.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
                abd.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
                await msg.edit(embed=abd)
                i+1

        if str(reaction.emoji) == "2️⃣":
                y.insert(k,user.name)
                abg = Embed(title="레이드 길드 팟", description=a)
                abg.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
                abg.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
                await msg.edit(embed=abg)
                k+1

        if str(reaction.emoji) == "⚠️":
            embed = Embed(title="⚠️길드팟 모집 완료⚠️")
            await reaction.message.channel.send(embed=embed)
@bot.event
async def on_reaction_remove(reaction, user):
        global msg
        if str(reaction.emoji) == "1️⃣":
                x.remove(user.name)
                abe = Embed(title="레이드 길드 팟", description=a)
                abe.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
                abe.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
                await msg.edit(embed=abe)
        if str(reaction.emoji) == "2️⃣":
                y.remove(user.name)
                abf = Embed(title="레이드 길드 팟", description=a)
                abf.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
                abf.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
                await msg.edit(embed=abf)

bot.run(TOKEN)
