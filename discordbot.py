import discord
import asyncio
from discord.ext import commands
from discord import Embed
from discord.ui import Button, View
from discord.utils import get
import os

intents = discord.Intents.all()

TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix='/',intents=intents)

x = ["X","X","X","X","X"]
y = ["X","X","X","X","X"]

x1 = ["X","X","X","X","X"]
y1 = ["X","X","X","X","X"]

x2 = ["X","X","X","X","X"]
y2 = ["X","X","X","X","X"]

raidcount,i,k,i1,k1,i2,k2 = 0,0,0,0,0,0,0
msg,mssg1,mssg2,mssg3="","","",""
        
@bot.command()
async def 레이드(ctx, *, message=None):
        button1 = Button(label="번 파티",emoji="1️⃣")
        button2 = Button(label="번 파티",emoji="2️⃣")
        button3 = Button(label="번 파티",emoji="1️⃣")
        button4 = Button(label="번 파티",emoji="2️⃣")
        button5 = Button(label="번 파티",emoji="1️⃣")
        button6 = Button(label="번 파티",emoji="2️⃣")

        async def button_callback1(interaction:discord.Interaction):
                if interaction.user.display_name in x:
                        x.remove(interaction.user.display_name)
                        embed = Embed(title="레이드 길드 팟", description=mssg1)
                        embed.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
                        embed.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
                        await msg.edit(embed=embed)
                        await interaction.response.defer()
                else:
                        x.insert(i,interaction.user.display_name)
                        embed = Embed(title="레이드 길드 팟", description=mssg1)
                        embed.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
                        embed.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
                        await msg.edit(embed=embed)
                        await interaction.response.defer()
                        i+1
        async def button_callback2(interaction:discord.Interaction):
                if interaction.user.display_name in y:
                        y.remove(interaction.user.display_name)
                        embed = Embed(title="레이드 길드 팟", description=mssg1)
                        embed.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
                        embed.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
                        await msg.edit(embed=embed)
                        await interaction.response.defer()
                else:
                        y.insert(k,interaction.user.display_name)
                        embed = Embed(title="레이드 길드 팟", description=mssg1)
                        embed.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
                        embed.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
                        await msg.edit(embed=embed)
                        await interaction.response.defer()
                        k+1
        async def button_callback3(interaction:discord.Interaction):
                if interaction.user.display_name in x1:
                        x1.remove(interaction.user.display_name)
                        embed1 = Embed(title="레이드 길드 팟", description=mssg2)
                        embed1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
                        embed1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
                        await msg1.edit(embed=embed1)
                        await interaction.response.defer()
                else:
                        x1.insert(i1,interaction.user.display_name)
                        embed1 = Embed(title="레이드 길드 팟", description=mssg2)
                        embed1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
                        embed1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
                        await msg1.edit(embed=embed1)
                        await interaction.response.defer()
                        i1+1
        async def button_callback4(interaction:discord.Interaction):
                if interaction.user.display_name in y1:
                        y1.remove(interaction.user.display_name)
                        embed1 = Embed(title="레이드 길드 팟", description=mssg2)
                        embed1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
                        embed1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
                        await msg1.edit(embed=embed1)
                        await interaction.response.defer()
                else:
                        y1.insert(k1,interaction.user.display_name)
                        embed1 = Embed(title="레이드 길드 팟", description=mssg2)
                        embed1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
                        embed1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
                        await msg1.edit(embed=embed1)
                        await interaction.response.defer()
                        k1+1
        async def button_callback5(interaction:discord.Interaction):
                if interaction.user.display_name in x2:
                        x2.remove(interaction.user.display_name)
                        embed2 = Embed(title="레이드 길드 팟", description=mssg3)
                        embed2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
                        embed2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
                        await msg2.edit(embed=embed2)
                        await interaction.response.defer()
                else:
                        x2.insert(i2,interaction.user.display_name)
                        embed2 = Embed(title="레이드 길드 팟", description=mssg3)
                        embed2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
                        embed2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
                        await msg2.edit(embed=embed2)
                        await interaction.response.defer()
                        i2+1
        async def button_callback6(interaction:discord.Interaction):
                if interaction.user.display_name in y2:
                        y2.remove(interaction.user.display_name)
                        embed2 = Embed(title="레이드 길드 팟", description=mssg3)
                        embed2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
                        embed2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
                        await msg2.edit(embed=embed2)
                        await interaction.response.defer()
                else:
                        y2.insert(k2,interaction.user.display_name)
                        embed2 = Embed(title="레이드 길드 팟", description=mssg3)
                        embed2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
                        embed2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
                        await msg2.edit(embed=embed2)
                        await interaction.response.defer()
                        k2+1  

        button1.callback = button_callback1
        button2.callback = button_callback2
        button3.callback = button_callback3
        button4.callback = button_callback4
        button5.callback = button_callback5
        button6.callback = button_callback6

        view = View(timeout=None)
        view.add_item(button1)
        view.add_item(button2)
        view1 = View(timeout=None)
        view1.add_item(button3)
        view1.add_item(button4)
        view2 = View(timeout=None)
        view2.add_item(button5)
        view2.add_item(button6)

        global raidcount,msg,msg1,msg2,mssg1,mssg2,mssg3,x,x1,x2,y,y1,y2,k1,k2,k,i,i1,i2
        if message == "초기화":
                x = ["X","X","X","X","X"]
                y = ["X","X","X","X","X"]

                x1 = ["X","X","X","X","X"]
                y1 = ["X","X","X","X","X"]

                x2 = ["X","X","X","X","X"]
                y2 = ["X","X","X","X","X"]

                raidcount,i,k,i1,k1,i2,k2 = 0,0,0,0,0,0,0
                msg,mssg1,mssg2,mssg3="","","",""
        elif raidcount == 0:
                mssg1=message
                abc = Embed(title="1번 레이드 길드 팟", description=mssg1)
                abc.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
                abc.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
                msg = await ctx.send(embed=abc,view=view)
                raidcount += 1
        elif raidcount == 1:
                mssg2=message
                abc1 = Embed(title='2번 레이드 길드 팟',description=mssg2)
                abc1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
                abc1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
                msg1 = await ctx.send(embed=abc1,view=view1)
                raidcount += 1
        elif raidcount == 2:
                mssg3=message
                abc2 = Embed(title='3번 레이드 길드 팟',description=mssg3)
                abc2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
                abc2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
                msg2 = await ctx.send(embed=abc2,view=view2)
                raidcount += 1
        elif raidcount == 3:
                await ctx.send("풀파티입니다.")
@bot.command()
async def 레이드수정(ctx, *, raidedit=None):
    global raidcount,msg,msg1,mssg1,mssg2,mssg3,x,x1,x2,y,y1,y2,k1,k2,k,i,i1,i2
    if "1번" in raidedit:
        rd1 = Embed(title="1번 레이드 길드 팟", description=raidedit)
        rd1.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
        rd1.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
        await msg.edit(embed=rd1)           
    if "2번" in raidedit:
        rd2 = Embed(title="2번 레이드 길드 팟", description=raidedit)
        rd2.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
        rd2.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
        await msg1.edit(embed=rd2)
    if "3번" in raidedit:
        rd3 = Embed(title="3번 레이드 길드 팟", description=raidedit)
        rd3.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
        rd3.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
        await msg2.edit(embed=rd3)

bot.run(TOKEN)
