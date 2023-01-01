import discord
from discord import app_commands
import asyncio
from discord import Embed
from discord.ui import Button, View
from discord.utils import get
import os
from discord.app_commands import Choice


TOKEN = os.environ['TOKEN']

class anlient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced  = True
        print(f'{self.user}이 시작되었습니다')
        game = discord.Game('파티 모집중')
        await self.change_presence(status=discord.Status.idle, activity=game)

client = anlient()
tree = app_commands.CommandTree(client)

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
rd1,rd2,rd3,rd4,rd5,msg,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5="","","","","","","","","","","","","","",""

@tree.command(name = "레이드", description="/레이드 일정")
async def slash2(interaction: discord.Interaction, 난이도: str, 군단장: str, 숙련: str, 일정: str):
    global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5
    button1 = Button(label="파티",emoji="1️⃣")
    button2 = Button(label="파티",emoji="2️⃣")
    button3 = Button(label="파티",emoji="1️⃣")
    button4 = Button(label="파티",emoji="2️⃣")
    button5 = Button(label="파티",emoji="1️⃣")
    button6 = Button(label="파티",emoji="2️⃣")
    button7 = Button(label="파티",emoji="1️⃣")
    button8 = Button(label="파티",emoji="2️⃣")
    button9 = Button(label="파티",emoji="1️⃣")
    button10 = Button(label="파티",emoji="2️⃣")

    async def button_callback1(interaction:discord.Interaction):
        if interaction.user.display_name in x:
            x.remove(interaction.user.display_name)
            embed = Embed(title="1팟 레이드 길드 팟", description=mssg1)
            embed.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
            embed.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed)
            i-1
        else:
            x.insert(i,interaction.user.display_name)
            embed = Embed(title="1팟 레이드 길드 팟", description=mssg1)
            embed.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
            embed.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed)
            i+1
    async def button_callback2(interaction:discord.Interaction):
        if interaction.user.display_name in y:
            y.remove(interaction.user.display_name)
            embed = Embed(title="1팟 레이드 길드 팟", description=mssg1)
            embed.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
            embed.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed)
            k-1
        else:
            y.insert(k,interaction.user.display_name)
            embed = Embed(title="1팟 레이드 길드 팟", description=mssg1)
            embed.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
            embed.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed)
            k+1
    async def button_callback3(interaction:discord.Interaction):
        if interaction.user.display_name in x1:
            x1.remove(interaction.user.display_name)
            embed1 = Embed(title="2팟 레이드 길드 팟", description=mssg2)
            embed1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
            embed1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed1)
            i1-1
        else:
            x1.insert(i1,interaction.user.display_name)
            embed1 = Embed(title="2팟 레이드 길드 팟", description=mssg2)
            embed1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
            embed1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed1)
            i1+1
    async def button_callback4(interaction:discord.Interaction):
        if interaction.user.display_name in y1:
            y1.remove(interaction.user.display_name)
            embed1 = Embed(title="2팟 레이드 길드 팟", description=mssg2)
            embed1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
            embed1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed1)
            k1-1
        else:
            y1.insert(k1,interaction.user.display_name)
            embed1 = Embed(title="2팟 레이드 길드 팟", description=mssg2)
            embed1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
            embed1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed1)
            k1+1
    async def button_callback5(interaction:discord.Interaction):
        if interaction.user.display_name in x2:
            x2.remove(interaction.user.display_name)
            embed2 = Embed(title="3팟 레이드 길드 팟", description=mssg3)
            embed2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
            embed2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed2)
            i2-1
        else:
            x2.insert(i2,interaction.user.display_name)
            embed2 = Embed(title="3팟 레이드 길드 팟", description=mssg3)
            embed2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
            embed2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed2)
            i2+1
    async def button_callback6(interaction:discord.Interaction):
        if interaction.user.display_name in y2:
            y2.remove(interaction.user.display_name)
            embed2 = Embed(title="3팟 레이드 길드 팟", description=mssg3)
            embed2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
            embed2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed2)
            k2-1
        else:
            y2.insert(k2,interaction.user.display_name)
            embed2 = Embed(title="3팟 레이드 길드 팟", description=mssg3)
            embed2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
            embed2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed2)
            k2+1
    async def button_callback7(interaction:discord.Interaction):
        if interaction.user.display_name in x3:
            x3.remove(interaction.user.display_name)
            embed3 = Embed(title="4팟 레이드 길드 팟", description=mssg4)
            embed3.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
            embed3.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed3)
            i3-1
        else:
            x3.insert(i3,interaction.user.display_name)
            embed3 = Embed(title="4팟 레이드 길드 팟", description=mssg4)
            embed3.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
            embed3.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed3)
            i3+1
    async def button_callback8(interaction:discord.Interaction):
        if interaction.user.display_name in y3:
            y3.remove(interaction.user.display_name)
            embed3 = Embed(title="4팟 레이드 길드 팟", description=mssg4)
            embed3.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
            embed3.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed3)
            k3-1
        else:
            y3.insert(k3,interaction.user.display_name)
            embed3 = Embed(title="4팟 레이드 길드 팟", description=mssg4)
            embed3.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
            embed3.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed3)
            k3+1
    async def button_callback9(interaction:discord.Interaction):
        if interaction.user.display_name in x4:
            x4.remove(interaction.user.display_name)
            embed4 = Embed(title="5팟 레이드 길드 팟", description=mssg5)
            embed4.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
            embed4.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed4)
            i4-1
        else:
            x4.insert(i4,interaction.user.display_name)
            embed4 = Embed(title="5팟 레이드 길드 팟", description=mssg5)
            embed4.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
            embed4.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed4)
            i4+1
    async def button_callback10(interaction:discord.Interaction):
        if interaction.user.display_name in y4:
            y4.remove(interaction.user.display_name)
            embed4 = Embed(title="5팟 레이드 길드 팟", description=mssg5)
            embed4.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
            embed4.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed4)
            k4-1
        else:
            y4.insert(k4,interaction.user.display_name)
            embed4 = Embed(title="5팟 레이드 길드 팟", description=mssg5)
            embed4.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
            embed4.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=embed4)
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

    rolesx = discord.utils.get(interaction.guild.roles, name="관리자")

    if rolesx in interaction.user.roles:
            if raidcount == 0:
                        mssg1=f"{난이도} {군단장}  {숙련}  {일정}"
                        abc = Embed(title="1팟 레이드 길드 팟", description=mssg1)
                        abc.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
                        abc.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
                        await interaction.response.send_message(embed=abc,view=view)
                        msg = await interaction.original_response()
                        raidcount += 1
            elif raidcount == 1:
                        mssg2=f"{난이도} {군단장}  {숙련}  {일정}"
                        abc1 = Embed(title='2팟 레이드 길드 팟',description=mssg2)
                        abc1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
                        abc1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
                        await interaction.response.send_message(embed=abc1,view=view1)
                        msg1 = await interaction.original_response()
                        raidcount += 1
            elif raidcount == 2:
                        mssg3=f"{난이도} {군단장}  {숙련}  {일정}"
                        abc2 = Embed(title='3팟 레이드 길드 팟',description=mssg3)
                        abc2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
                        abc2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
                        await interaction.response.send_message(embed=abc2,view=view2)
                        msg2 = await interaction.original_response()
                        raidcount += 1
            elif raidcount == 3:
                        mssg4=f"{난이도} {군단장}  {숙련}  {일정}"
                        abc3 = Embed(title='4팟 레이드 길드 팟',description=mssg4)
                        abc3.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
                        abc3.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
                        await interaction.response.send_message(embed=abc3,view=view3)
                        msg3 = await interaction.original_response()
                        raidcount += 1
            elif raidcount == 4:
                        mssg5=f"{난이도} {군단장}  {숙련}  {일정}"
                        abc4 = Embed(title='5팟 레이드 길드 팟',description=mssg5)
                        abc4.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
                        abc4.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
                        await interaction.response.send_message(embed=abc4,view=view4)
                        msg4 = await interaction.original_response()
                        raidcount += 1
            if raidcount == 5:
                        await interaction.response.send_message("풀파티입니다.")
    else:
        await interaction.response.send_message("관리자가 아닙니다.")


@app_commands.choices(팟 = [
    Choice(name = '1팟', value='1'),
    Choice(name = '2팟', value='2'),
    Choice(name = '3팟', value='3'),
    Choice(name = '4팟', value='4'),
    Choice(name = '5팟', value='5'),
])

@tree.command(name = "레이드수정", description="/레이드 일정")
async def slash3(interaction: discord.Interaction, 팟: str, 난이도: str, 군단장: str,숙련: str, 일정: str):
    global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5
    if 팟 == '1':
        mssg1=f"{난이도} {군단장}  {숙련}  {일정}"
        rd1 = Embed(title="1팟 레이드 길드 팟", description=mssg1)
        rd1.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
        rd1.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
        await msg.edit(embed=rd1)
        await interaction.response.send_message(f"수정 완료", ephemeral=True)
    if 팟 == '2':
        mssg2=f"{난이도} {군단장}  {숙련}  {일정}"
        rd2 = Embed(title="2팟 레이드 길드 팟", description=mssg2)
        rd2.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
        rd2.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
        await msg1.edit(embed=rd2)
        await interaction.response.send_message(f"수정 완료", ephemeral=True)
    if 팟 == '3':
        mssg3=f"{난이도} {군단장}  {숙련}  {일정}"
        rd3 = Embed(title="3팟 레이드 길드 팟", description=mssg3)
        rd3.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
        rd3.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
        await msg2.edit(embed=rd3)
        await interaction.response.send_message(f"수정 완료", ephemeral=True)
    if 팟 == '4':
        mssg4=f"{난이도} {군단장}  {숙련}  {일정}"
        rd4 = Embed(title="4팟 레이드 길드 팟", description=mssg4)
        rd4.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
        rd4.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
        await msg3.edit(embed=rd4)
        await interaction.response.send_message(f"수정 완료", ephemeral=True)
    if 팟 == '5':
        mssg5=f"{난이도} {군단장}  {숙련}  {일정}"
        rd5 = Embed(title="5팟 레이드 길드 팟", description=mssg5)
        rd5.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
        rd5.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
        await msg4.edit(embed=rd5)
        await interaction.response.send_message(f"수정 완료", ephemeral=True)
        
@tree.command(name = "레이드초기화", description="레이드 일정을 초기화합니다.")
async def slash3(interaction: discord.Interaction):
    global x,y,x1,y1,x2,y2,x3,y3,x4,y4,raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg4,mssg5
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
    rd1,rd2,rd3,rd4,rd5,msg,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg4,mssg5="","","","","","","","","","","","","",""
    await interaction.response.send_message(f"초기화 완료", ephemeral=True)

@tree.command(name = "파티모집기사용법",description="파티모집 어떻게 사용하나요?")
async def slash4(interaction: discord.Interaction):
    raidhelp = Embed(title='딜컷 파티모집기',description="사용법")
    raidhelp.add_field(name="/레이드", value="레이드 일정을 만듭니다.(max 5팟)", inline=False)
    raidhelp.add_field(name="/레이드수정", value="1팟~5팟 레이드 일정을 수정합니다.", inline=False)
    raidhelp.add_field(name="/레이드초기화", value="레이드 일정을 초기화합니다.", inline=False)
    raidhelp.set_footer(text="로요일마다 초기화하신 후 사용해주세요.")
    await interaction.response.send_message(embed=raidhelp,ephemeral=True) 
 
client.run(TOKEN)
