import discord
import asyncio
from discord.ext import commands
from discord import Embed
from discord.ui import Button, View
from discord.utils import get
import os
import re

intents = discord.Intents.all()

TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix='/',intents=intents)

x = ["X","X","X","X","X"]
y = ["X","X","X","X","X"]
x1 = ["X","X","X","X","X"]
y1 = ["X","X","X","X","X"]
x2 = ["X","X","X","X","X"]
y2 = ["X","X","X","X","X"]
x3 = ["X","X","X","X","X"]
y3 = ["X","X","X","X","X"]
x4 = ["X","X","X","X","X"]
y4 = ["X","X","X","X","X"]

raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4 = 0,0,0,0,0,0,0,0,0,0,0
rd1,rd2,rd3,msg,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5="","","","","","","","","","","","",""
        
@bot.command()
async def 레이드(ctx, *, message=None):
    global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4
    button1 = Button(label="번 파티",emoji="1️⃣")
    button2 = Button(label="번 파티",emoji="2️⃣")
    button3 = Button(label="번 파티",emoji="1️⃣")
    button4 = Button(label="번 파티",emoji="2️⃣")
    button5 = Button(label="번 파티",emoji="1️⃣")
    button6 = Button(label="번 파티",emoji="2️⃣")
    button7 = Button(label="번 파티",emoji="1️⃣")
    button8 = Button(label="번 파티",emoji="2️⃣")
    button9 = Button(label="번 파티",emoji="1️⃣")
    button10 = Button(label="번 파티",emoji="2️⃣")

    async def button_callback1(interaction:discord.Interaction):
        if interaction.user.display_name in x:
            x.remove(interaction.user.display_name)
            embed = Embed(title="1번 레이드 길드 팟", description=mssg1)
            embed.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
            embed.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
            await msg.edit(embed=embed)
            await interaction.response.defer()
            i-1
        else:
            x.insert(i,interaction.user.display_name)
            embed = Embed(title="1번 레이드 길드 팟", description=mssg1)
            embed.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
            embed.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
            await msg.edit(embed=embed)
            await interaction.response.defer()
            i+1
    async def button_callback2(interaction:discord.Interaction):
        if interaction.user.display_name in y:
            y.remove(interaction.user.display_name)
            embed = Embed(title="1번 레이드 길드 팟", description=mssg1)
            embed.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
            embed.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
            await msg.edit(embed=embed)
            await interaction.response.defer()
            k-1
        else:
            y.insert(k,interaction.user.display_name)
            embed = Embed(title="1번 레이드 길드 팟", description=mssg1)
            embed.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
            embed.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
            await msg.edit(embed=embed)
            await interaction.response.defer()
            k+1
    async def button_callback3(interaction:discord.Interaction):
        if interaction.user.display_name in x1:
            x1.remove(interaction.user.display_name)
            embed1 = Embed(title="2번 레이드 길드 팟", description=mssg2)
            embed1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
            embed1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
            await msg1.edit(embed=embed1)
            await interaction.response.defer()
            i1-1
        else:
            x1.insert(i1,interaction.user.display_name)
            embed1 = Embed(title="2번 레이드 길드 팟", description=mssg2)
            embed1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
            embed1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
            await msg1.edit(embed=embed1)
            await interaction.response.defer()
            i1+1
    async def button_callback4(interaction:discord.Interaction):
        if interaction.user.display_name in y1:
            y1.remove(interaction.user.display_name)
            embed1 = Embed(title="2번 레이드 길드 팟", description=mssg2)
            embed1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
            embed1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
            await msg1.edit(embed=embed1)
            await interaction.response.defer()
            k1-1
        else:
            y1.insert(k1,interaction.user.display_name)
            embed1 = Embed(title="2번 레이드 길드 팟", description=mssg2)
            embed1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
            embed1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
            await msg1.edit(embed=embed1)
            await interaction.response.defer()
            k1+1
    async def button_callback5(interaction:discord.Interaction):
        if interaction.user.display_name in x2:
            x2.remove(interaction.user.display_name)
            embed2 = Embed(title="3번 레이드 길드 팟", description=mssg3)
            embed2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
            embed2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
            await msg2.edit(embed=embed2)
            await interaction.response.defer()
            i2-1
        else:
            x2.insert(i2,interaction.user.display_name)
            embed2 = Embed(title="3번 레이드 길드 팟", description=mssg3)
            embed2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
            embed2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
            await msg2.edit(embed=embed2)
            await interaction.response.defer()
            i2+1
    async def button_callback6(interaction:discord.Interaction):
        if interaction.user.display_name in y2:
            y2.remove(interaction.user.display_name)
            embed2 = Embed(title="3번 레이드 길드 팟", description=mssg3)
            embed2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
            embed2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
            await msg2.edit(embed=embed2)
            await interaction.response.defer()
            k2-1
        else:
            y2.insert(k2,interaction.user.display_name)
            embed2 = Embed(title="3번 레이드 길드 팟", description=mssg3)
            embed2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
            embed2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
            await msg2.edit(embed=embed2)
            await interaction.response.defer()
            k2+1
    async def button_callback7(interaction:discord.Interaction):
        if interaction.user.display_name in x3:
            x3.remove(interaction.user.display_name)
            embed3 = Embed(title="4번 레이드 길드 팟", description=mssg4)
            embed3.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
            embed3.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
            await msg3.edit(embed=embed3)
            await interaction.response.defer()
            i3-1
        else:
            x3.insert(i3,interaction.user.display_name)
            embed3 = Embed(title="4번 레이드 길드 팟", description=mssg4)
            embed3.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
            embed3.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
            await msg3.edit(embed=embed3)
            await interaction.response.defer()
            i3+1
    async def button_callback8(interaction:discord.Interaction):
        if interaction.user.display_name in y3:
            y3.remove(interaction.user.display_name)
            embed3 = Embed(title="4번 레이드 길드 팟", description=mssg4)
            embed3.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
            embed3.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
            await msg3.edit(embed=embed3)
            await interaction.response.defer()
            k3-1
        else:
            y3.insert(k3,interaction.user.display_name)
            embed3 = Embed(title="4번 레이드 길드 팟", description=mssg4)
            embed3.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
            embed3.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
            await msg3.edit(embed=embed3)
            await interaction.response.defer()
            k3+1
    async def button_callback9(interaction:discord.Interaction):
        if interaction.user.display_name in x4:
            x4.remove(interaction.user.display_name)
            embed4 = Embed(title="5번 레이드 길드 팟", description=mssg5)
            embed4.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
            embed4.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
            await msg4.edit(embed=embed4)
            await interaction.response.defer()
            i4-1
        else:
            x4.insert(i4,interaction.user.display_name)
            embed4 = Embed(title="5번 레이드 길드 팟", description=mssg5)
            embed4.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
            embed4.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
            await msg4.edit(embed=embed4)
            await interaction.response.defer()
            i4+1
    async def button_callback10(interaction:discord.Interaction):
        if interaction.user.display_name in y3:
            y4.remove(interaction.user.display_name)
            embed4 = Embed(title="5번 레이드 길드 팟", description=mssg5)
            embed4.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
            embed4.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
            await msg4.edit(embed=embed4)
            await interaction.response.defer()
            k4-1
        else:
            y4.insert(k4,interaction.user.display_name)
            embed4 = Embed(title="5번 레이드 길드 팟", description=mssg5)
            embed4.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
            embed4.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
            await msg4.edit(embed=embed4)
            await interaction.response.defer()
            k4+1  

        button1.callback = button_callback1
        button2.callback = button_callback2
        button3.callback = button_callback3
        button4.callback = button_callback4
        button5.callback = button_callback5
        button6.callback = button_callback6
        button7.callback = button_callback7
        button8.callback = button_callback8
        button9.callback = button_callback9
        button10.callback = button_callback10

        view = View(timeout=None)
        view.add_item(button1)
        view.add_item(button2)
        view1 = View(timeout=None)
        view1.add_item(button3)
        view1.add_item(button4)
        view2 = View(timeout=None)
        view2.add_item(button5)
        view2.add_item(button6)
        view3 = View(timeout=None)
        view3.add_item(button7)
        view3.add_item(button8)
        view4 = View(timeout=None)
        view4.add_item(button9)
        view4.add_item(button10)

        if ctx.message.author.display_name == "숯미남" or ctx.message.author.guild_permissions.administrator:
            if message == "초기화":
                x = ["X","X","X","X","X"]
                y = ["X","X","X","X","X"]
                x1 = ["X","X","X","X","X"]
                y1 = ["X","X","X","X","X"]
                x2 = ["X","X","X","X","X"]
                y2 = ["X","X","X","X","X"]
                x3 = ["X","X","X","X","X"]
                y3 = ["X","X","X","X","X"]
                x4 = ["X","X","X","X","X"]
                y4 = ["X","X","X","X","X"]

                raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4 = 0,0,0,0,0,0,0,0,0,0,0
                rd1,rd2,rd3,msg,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4="","","","","","","","","","","",""
            if raidcount == 0:
                        mssg1=message
                        abc = Embed(title="1번 레이드 길드 팟", description=mssg1)
                        abc.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
                        abc.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
                        msg = await ctx.send(embed=abc,view=view)
                        raidcount += 1
            if raidcount == 1:
                        mssg2=message
                        abc1 = Embed(title='2번 레이드 길드 팟',description=mssg2)
                        abc1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
                        abc1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
                        msg1 = await ctx.send(embed=abc1,view=view1)
                        raidcount += 1
            if raidcount == 2:
                        mssg3=message
                        abc2 = Embed(title='3번 레이드 길드 팟',description=mssg3)
                        abc2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
                        abc2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
                        msg2 = await ctx.send(embed=abc2,view=view2)
                        raidcount += 1
            if raidcount == 3:
                        mssg4=message
                        abc3 = Embed(title='4번 레이드 길드 팟',description=mssg4)
                        abc3.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
                        abc3.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
                        msg3 = await ctx.send(embed=abc3,view=view3)
                        raidcount += 1
            if raidcount == 4:
                        mssg5=message
                        abc4 = Embed(title='5번 레이드 길드 팟',description=mssg5)
                        abc4.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
                        abc4.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
                        msg4 = await ctx.send(embed=abc4,view=view4)
                        raidcount += 1
            if raidcount == 5:
                        await ctx.send("풀파티입니다.")
        else:
            ctx.send("임원이 아닙니다.")
@bot.command()
async def 레이드수정(ctx, *, raidedit=None):
    global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,msg,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,rd1,rd2,rd3
    if "1번" in raidedit:
        mssg1= re.sub("1번 ","",raidedit)
        rd1 = Embed(title="1번 레이드 길드 팟", description=mssg1)
        rd1.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
        rd1.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
        await msg.edit(embed=rd1)           
    if "2번" in raidedit:
        mssg2= re.sub("1번 ","",raidedit)
        rd2 = Embed(title="2번 레이드 길드 팟", description=mssg2)
        rd2.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
        rd2.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
        await msg1.edit(embed=rd2)
    if "3번" in raidedit:
        mssg3= re.sub("1번 ","",raidedit)
        rd3 = Embed(title="3번 레이드 길드 팟", description=mssg3)
        rd3.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
        rd3.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
        await msg2.edit(embed=rd3)
    if "4번" in raidedit:
        mssg4= re.sub("4번 ","",raidedit)
        rd4 = Embed(title="4번 레이드 길드 팟", description=mssg4)
        rd4.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
        rd4.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
        await msg2.edit(embed=rd4)
    if "5번" in raidedit:
        mssg5= re.sub("5번 ","",raidedit)
        rd5 = Embed(title="5번 레이드 길드 팟", description=mssg5)
        rd5.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
        rd5.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
        await msg2.edit(embed=rd5)

bot.run(TOKEN)
