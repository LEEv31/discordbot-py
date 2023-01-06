import discord
from discord import app_commands
import asyncio
from discord import Embed
from discord.ui import Select, View , Button
from discord.utils import get
import os
from discord.app_commands import Choice
import platform
from discord import ui

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
eb1,eb2,eb3,eb4,eb5,ek1,ek2,ek3,ek4,ek5="","","","","","","","","",""

class MyModal(ui.Modal, title="Information"):
    name =  ui.TextInput(label="수정할 내용을 적어주세요.",placeholder="ex)군단장 난이도 숙련도 일정", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        mssg1=f"{self.name}"
        rd1 = Embed(title="1팟 레이드 길드 팟", description=mssg1, color=0x3cc039)
        rd1.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
        rd1.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
        await interaction.response.edit_message(embed=rd1)
class MyModal1(ui.Modal, title="Information"):
    name1 =  ui.TextInput(label="수정할 내용을 적어주세요.",placeholder="ex)군단장 난이도 숙련도 일정", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        mssg2=f"{self.name1}"
        rd2 = Embed(title="2팟 레이드 길드 팟", description=mssg2, color=0x3cc039)
        rd2.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
        rd2.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
        await interaction.response.edit_message(embed=rd2)
class MyModal2(ui.Modal, title="Information"):
    name2 =  ui.TextInput(label="수정할 내용을 적어주세요.",placeholder="ex)군단장 난이도 숙련도 일정", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        mssg3=f"{self.name2}"
        rd3 = Embed(title="3팟 레이드 길드 팟", description=mssg3, color=0x3cc039)
        rd3.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
        rd3.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
        await interaction.response.edit_message(embed=rd3)
class MyModal3(ui.Modal, title="Information"):
    name3 =  ui.TextInput(label="수정할 내용을 적어주세요.",placeholder="ex)군단장 난이도 숙련도 일정", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        mssg4=f"{self.name3}"
        rd4 = Embed(title="4팟 레이드 길드 팟", description=mssg4, color=0x3cc039)
        rd4.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
        rd4.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
        await interaction.response.edit_message(embed=rd4)
class MyModal4(ui.Modal, title="Information"):
    name4 =  ui.TextInput(label="수정할 내용을 적어주세요.",placeholder="ex)군단장 난이도 숙련도 일정", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        mssg5=f"{self.name4}"
        rd5 = Embed(title="5팟 레이드 길드 팟", description=mssg5, color=0x3cc039)
        rd5.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
        rd5.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
        await interaction.response.edit_message(embed=rd5)       

class SelectMenu(discord.ui.Select):
    def __init__(self):
        global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5,eb1,eb2,eb3,eb4,eb5,ek1,ek2,ek3,ek4,ek5       
        options = [discord.SelectOption(label="버서커", description="버서커"),
                   discord.SelectOption(label="디스트로이어", description="디스트로이어"),
                   discord.SelectOption(label="워로드", description="워로드"),
                   discord.SelectOption(label="홀리나이트", description="홀리나이트"),
                   discord.SelectOption(label="슬레이어", description="슬레이어"),
                   discord.SelectOption(label="배틀마스터", description="배틀마스터"),
                   discord.SelectOption(label="인파이터", description="인파이터"),
                   discord.SelectOption(label="기공사", description="기공사"),
                   discord.SelectOption(label="창술사", description="창술사"),
                   discord.SelectOption(label="스트라이커", description="스트라이커"),
                   discord.SelectOption(label="데빌헌터", description="데빌헌터"),
                   discord.SelectOption(label="블래스터", description="블래스터"),
                   discord.SelectOption(label="호크아이", description="호크아이"),
                   discord.SelectOption(label="스카우터", description="스카우터"),
                   discord.SelectOption(label="건슬링어", description="건슬링어"),
                   discord.SelectOption(label="아르카나", description="아르카나"),
                   discord.SelectOption(label="서머너", description="서머너"),
                   discord.SelectOption(label="바드", description="바드"),
                   discord.SelectOption(label="소서리스", description="소서리스"),
                   discord.SelectOption(label="데모닉", description="데모닉"),
                   discord.SelectOption(label="블레이드", description="블레이드"),
                   discord.SelectOption(label="리퍼", description="리퍼"),
                   discord.SelectOption(label="소울이터", description="소울이터"),
                   discord.SelectOption(label="도화가", description="도화가"),
                   discord.SelectOption(label="기상술사", description="기상술사")]
        super().__init__(placeholder="1 파티", max_values=1, min_values=1, options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "버서커":
            user = f"{interaction.user.display_name}(버서커)"
        elif self.values[0] == "디스트로이어":
            user = f"{interaction.user.display_name}(디스트로이어)"
        elif self.values[0] == "워로드":
            user = f"{interaction.user.display_name}(워로드)"
        elif self.values[0] == "홀리나이트":
            user = f"{interaction.user.display_name}(홀리나이트)"
        elif self.values[0] == "슬레이어":
            user = f"{interaction.user.display_name}(슬레이어)"
        elif self.values[0] == "배틀마스터":
            user = f"{interaction.user.display_name}(배틀마스터)"
        elif self.values[0] == "인파이터":
            user = f"{interaction.user.display_name}(인파이터)"
        elif self.values[0] == "기공사":
            user = f"{interaction.user.display_name}(기공사)"
        elif self.values[0] == "창술사":
            user = f"{interaction.user.display_name}(창술사)"
        elif self.values[0] == "스트라이커":
            user = f"{interaction.user.display_name}(스트라이커)"
        elif self.values[0] == "데빌헌터":
            user = f"{interaction.user.display_name}(데빌헌터)"
        elif self.values[0] == "블래스터":
            user = f"{interaction.user.display_name}(블래스터)"
        elif self.values[0] == "호크아이":
            user = f"{interaction.user.display_name}(호크아이)"
        elif self.values[0] == "스카우터":
            user = f"{interaction.user.display_name}(스카우터)"
        elif self.values[0] == "건슬링어":
            user = f"{interaction.user.display_name}(건슬링어)"
        elif self.values[0] == "아르카나":
            user = f"{interaction.user.display_name}(아르카나)"
        elif self.values[0] == "서머너":
            user = f"{interaction.user.display_name}(서머너)"
        elif self.values[0] == "바드":
            user = f"{interaction.user.display_name}(바드)"
        elif self.values[0] == "소서리스":
            user = f"{interaction.user.display_name}(소서리스)"
        elif self.values[0] == "데모닉":
            user = f"{interaction.user.display_name}(데모닉)"
        elif self.values[0] == "블레이드":
            user = f"{interaction.user.display_name}(블레이드)"
        elif self.values[0] == "리퍼":
            user = f"{interaction.user.display_name}(리퍼)"
        elif self.values[0] == "소울이터":
            user = f"{interaction.user.display_name}(소울이터)"
        elif self.values[0] == "도화가":
            user = f"{interaction.user.display_name}(도화가)"
        elif self.values[0] == "기상술사":
            user = f"{interaction.user.display_name}(기상술사)"
        if user in x:
            x.remove(user)
            eb1 = Embed(title="1팟 레이드 길드 팟", description=mssg1)
            eb1.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
            eb1.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=eb1)
            i-1
        else:
            x.insert(i,user)
            ek1 = Embed(title="1팟 레이드 길드 팟", description=mssg1)
            ek1.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
            ek1.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=ek1)
            i+1
class SelectMenu1(discord.ui.Select):
    def __init__(self):
        global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5,eb1,eb2,eb3,eb4,eb5,ek1,ek2,ek3,ek4,ek5
        options1 = [discord.SelectOption(label="버서커", value="1", description="버서커"),
                   discord.SelectOption(label="디스트로이어", value="2", description="디스트로이어"),
                   discord.SelectOption(label="워로드", value="3", description="워로드"),
                   discord.SelectOption(label="홀리나이트", value="4", description="홀리나이트"),
                   discord.SelectOption(label="슬레이어", value="5", description="슬레이어"),
                   discord.SelectOption(label="배틀마스터", value="6", description="배틀마스터"),
                   discord.SelectOption(label="인파이터", value="7", description="인파이터"),
                   discord.SelectOption(label="기공사", value="8", description="기공사"),
                   discord.SelectOption(label="창술사", value="9", description="창술사"),
                   discord.SelectOption(label="스트라이커", value="10", description="스트라이커"),
                   discord.SelectOption(label="데빌헌터", value="11", description="데빌헌터"),
                   discord.SelectOption(label="블래스터", value="12", description="블래스터"),
                   discord.SelectOption(label="호크아이", value="13", description="호크아이"),
                   discord.SelectOption(label="스카우터", value="14", description="스카우터"),
                   discord.SelectOption(label="건슬링어", value="15", description="건슬링어"),
                   discord.SelectOption(label="아르카나", value="16", description="아르카나"),
                   discord.SelectOption(label="서머너", value="17", description="서머너"),
                   discord.SelectOption(label="바드", value="18", description="바드"),
                   discord.SelectOption(label="소서리스", value="19", description="소서리스"),
                   discord.SelectOption(label="데모닉", value="20", description="데모닉"),
                   discord.SelectOption(label="블레이드", value="21", description="블레이드"),
                   discord.SelectOption(label="리퍼", value="22", description="리퍼"),
                   discord.SelectOption(label="소울이터", value="23", description="소울이터"),
                   discord.SelectOption(label="도화가", value="24", description="도화가"),
                   discord.SelectOption(label="기상술사", value="25", description="기상술사")]
        super().__init__(placeholder="2 파티", max_values=1, min_values=1, options=options1)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "1":
            user1 = f"{interaction.user.display_name}(버서커)"
        elif self.values[0] == "2":
            user1 = f"{interaction.user.display_name}(디스트로이어)"
        elif self.values[0] == "3":
            user1 = f"{interaction.user.display_name}(워로드)"
        elif self.values[0] == "4":
            user1 = f"{interaction.user.display_name}(홀리나이트)"
        elif self.values[0] == "5":
            user1 = f"{interaction.user.display_name}(슬레이어)"
        elif self.values[0] == "6":
            user1 = f"{interaction.user.display_name}(배틀마스터)"
        elif self.values[0] == "7":
            user1 = f"{interaction.user.display_name}(인파이터)"
        elif self.values[0] == "8":
            user1 = f"{interaction.user.display_name}(기공사)"
        elif self.values[0] == "9":
            user1 = f"{interaction.user.display_name}(창술사)"
        elif self.values[0] == "10":
            user1 = f"{interaction.user.display_name}(스트라이커)"
        elif self.values[0] == "11":
            user1 = f"{interaction.user.display_name}(데빌헌터)"
        elif self.values[0] == "12":
            user1 = f"{interaction.user.display_name}(블래스터)"
        elif self.values[0] == "13":
            user1 = f"{interaction.user.display_name}(호크아이)"
        elif self.values[0] == "14":
            user1 = f"{interaction.user.display_name}(스카우터)"
        elif self.values[0] == "15":
            user1 = f"{interaction.user.display_name}(건슬링어)"
        elif self.values[0] == "16":
            user1 = f"{interaction.user.display_name}(아르카나)"
        elif self.values[0] == "17":
            user1 = f"{interaction.user.display_name}(서머너)"
        elif self.values[0] == "18":
            user1 = f"{interaction.user.display_name}(바드)"
        elif self.values[0] == "19":
            user1 = f"{interaction.user.display_name}(소서리스)"
        elif self.values[0] == "20":
            user1 = f"{interaction.user.display_name}(데모닉)"
        elif self.values[0] == "21":
            user1 = f"{interaction.user.display_name}(블레이드)"
        elif self.values[0] == "22":
            user1 = f"{interaction.user.display_name}(리퍼)"
        elif self.values[0] == "23":
            user1 = f"{interaction.user.display_name}(소울이터)"
        elif self.values[0] == "24":
            user1 = f"{interaction.user.display_name}(도화가)"
        elif self.values[0] == "25":
            user1 = f"{interaction.user.display_name}(기상술사)"
        if user1 in y:
            y.remove(user1)
            eb2 = Embed(title="1팟 레이드 길드 팟", description=mssg1, color=0x395bc0)
            eb2.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
            eb2.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=eb2)
            k-1
        else:
            y.insert(k,user1)
            ek2 = Embed(title="1팟 레이드 길드 팟", description=mssg1, color=0x395bc0)
            ek2.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
            ek2.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=ek2)
            k+1
class SelectMenu2(discord.ui.Select):
    def __init__(self):
        global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5,eb1,eb2,eb3,eb4,eb5,ek1,ek2,ek3,ek4,ek5
        options2 = [discord.SelectOption(label="버서커", description="버서커"),
                   discord.SelectOption(label="디스트로이어", description="디스트로이어"),
                   discord.SelectOption(label="워로드", description="워로드"),
                   discord.SelectOption(label="홀리나이트", description="홀리나이트"),
                   discord.SelectOption(label="슬레이어", description="슬레이어"),
                   discord.SelectOption(label="배틀마스터", description="배틀마스터"),
                   discord.SelectOption(label="인파이터", description="인파이터"),
                   discord.SelectOption(label="기공사", description="기공사"),
                   discord.SelectOption(label="창술사", description="창술사"),
                   discord.SelectOption(label="스트라이커", description="스트라이커"),
                   discord.SelectOption(label="데빌헌터", description="데빌헌터"),
                   discord.SelectOption(label="블래스터", description="블래스터"),
                   discord.SelectOption(label="호크아이", description="호크아이"),
                   discord.SelectOption(label="스카우터", description="스카우터"),
                   discord.SelectOption(label="건슬링어", description="건슬링어"),
                   discord.SelectOption(label="아르카나", description="아르카나"),
                   discord.SelectOption(label="서머너", description="서머너"),
                   discord.SelectOption(label="바드", description="바드"),
                   discord.SelectOption(label="소서리스", description="소서리스"),
                   discord.SelectOption(label="데모닉", description="데모닉"),
                   discord.SelectOption(label="블레이드", description="블레이드"),
                   discord.SelectOption(label="리퍼", description="리퍼"),
                   discord.SelectOption(label="소울이터", description="소울이터"),
                   discord.SelectOption(label="도화가", description="도화가"),
                   discord.SelectOption(label="기상술사", description="기상술사")]
        super().__init__(placeholder="1 파티", max_values=1, min_values=1, options=options2)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "버서커":
            user2 = f"{interaction.user.display_name}(버서커)"
        elif self.values[0] == "디스트로이어":
            user2 = f"{interaction.user.display_name}(디스트로이어)"
        elif self.values[0] == "워로드":
            user2 = f"{interaction.user.display_name}(워로드)"
        elif self.values[0] == "홀리나이트":
            user2 = f"{interaction.user.display_name}(홀리나이트)"
        elif self.values[0] == "슬레이어":
            user2 = f"{interaction.user.display_name}(슬레이어)"
        elif self.values[0] == "배틀마스터":
            user2 = f"{interaction.user.display_name}(배틀마스터)"
        elif self.values[0] == "인파이터":
            user2 = f"{interaction.user.display_name}(인파이터)"
        elif self.values[0] == "기공사":
            user2 = f"{interaction.user.display_name}(기공사)"
        elif self.values[0] == "창술사":
            user2 = f"{interaction.user.display_name}(창술사)"
        elif self.values[0] == "스트라이커":
            user2 = f"{interaction.user.display_name}(스트라이커)"
        elif self.values[0] == "데빌헌터":
            user2 = f"{interaction.user.display_name}(데빌헌터)"
        elif self.values[0] == "블래스터":
            user2 = f"{interaction.user.display_name}(블래스터)"
        elif self.values[0] == "호크아이":
            user2 = f"{interaction.user.display_name}(호크아이)"
        elif self.values[0] == "스카우터":
            user2 = f"{interaction.user.display_name}(스카우터)"
        elif self.values[0] == "건슬링어":
            user2 = f"{interaction.user.display_name}(건슬링어)"
        elif self.values[0] == "아르카나":
            user2 = f"{interaction.user.display_name}(아르카나)"
        elif self.values[0] == "서머너":
            user2 = f"{interaction.user.display_name}(서머너)"
        elif self.values[0] == "바드":
            user2 = f"{interaction.user.display_name}(바드)"
        elif self.values[0] == "소서리스":
            user2 = f"{interaction.user.display_name}(소서리스)"
        elif self.values[0] == "데모닉":
            user2 = f"{interaction.user.display_name}(데모닉)"
        elif self.values[0] == "블레이드":
            user2 = f"{interaction.user.display_name}(블레이드)"
        elif self.values[0] == "리퍼":
            user2 = f"{interaction.user.display_name}(리퍼)"
        elif self.values[0] == "소울이터":
            user2 = f"{interaction.user.display_name}(소울이터)"
        elif self.values[0] == "도화가":
            user2 = f"{interaction.user.display_name}(도화가)"
        elif self.values[0] == "기상술사":
            user2 = f"{interaction.user.display_name}(기상술사)"
        if user2 in x1:
            x1.remove(user2)
            eb3 = Embed(title="2팟 레이드 길드 팟", description=mssg2, color=0x395bc0)
            eb3.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
            eb3.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=eb3)       
            i1-1
        else:
            x1.insert(i1,user2)
            ek3 = Embed(title="2팟 레이드 길드 팟", description=mssg2, color=0x395bc0)
            ek3.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
            ek3.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=ek3)             
            i1+1
class SelectMenu3(discord.ui.Select):
    def __init__(self):
        global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5,eb1,eb2,eb3,eb4,eb5,ek1,ek2,ek3,ek4,ek5
        options3 = [discord.SelectOption(label="버서커", description="버서커"),
                   discord.SelectOption(label="디스트로이어", description="디스트로이어"),
                   discord.SelectOption(label="워로드", description="워로드"),
                   discord.SelectOption(label="홀리나이트", description="홀리나이트"),
                   discord.SelectOption(label="슬레이어", description="슬레이어"),
                   discord.SelectOption(label="배틀마스터", description="배틀마스터"),
                   discord.SelectOption(label="인파이터", description="인파이터"),
                   discord.SelectOption(label="기공사", description="기공사"),
                   discord.SelectOption(label="창술사", description="창술사"),
                   discord.SelectOption(label="스트라이커", description="스트라이커"),
                   discord.SelectOption(label="데빌헌터", description="데빌헌터"),
                   discord.SelectOption(label="블래스터", description="블래스터"),
                   discord.SelectOption(label="호크아이", description="호크아이"),
                   discord.SelectOption(label="스카우터", description="스카우터"),
                   discord.SelectOption(label="건슬링어", description="건슬링어"),
                   discord.SelectOption(label="아르카나", description="아르카나"),
                   discord.SelectOption(label="서머너", description="서머너"),
                   discord.SelectOption(label="바드", description="바드"),
                   discord.SelectOption(label="소서리스", description="소서리스"),
                   discord.SelectOption(label="데모닉", description="데모닉"),
                   discord.SelectOption(label="블레이드", description="블레이드"),
                   discord.SelectOption(label="리퍼", description="리퍼"),
                   discord.SelectOption(label="소울이터", description="소울이터"),
                   discord.SelectOption(label="도화가", description="도화가"),
                   discord.SelectOption(label="기상술사", description="기상술사")]
        super().__init__(placeholder="2 파티", max_values=1, min_values=1, options=options3)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "버서커":
            user3 = f"{interaction.user.display_name}(버서커)"
        elif self.values[0] == "디스트로이어":
            user3 = f"{interaction.user.display_name}(디스트로이어)"
        elif self.values[0] == "워로드":
            user3 = f"{interaction.user.display_name}(워로드)"
        elif self.values[0] == "홀리나이트":
            user3 = f"{interaction.user.display_name}(홀리나이트)"
        elif self.values[0] == "슬레이어":
            user3 = f"{interaction.user.display_name}(슬레이어)"
        elif self.values[0] == "배틀마스터":
            user3 = f"{interaction.user.display_name}(배틀마스터)"
        elif self.values[0] == "인파이터":
            user3 = f"{interaction.user.display_name}(인파이터)"
        elif self.values[0] == "기공사":
            user3 = f"{interaction.user.display_name}(기공사)"
        elif self.values[0] == "창술사":
            user3 = f"{interaction.user.display_name}(창술사)"
        elif self.values[0] == "스트라이커":
            user3 = f"{interaction.user.display_name}(스트라이커)"
        elif self.values[0] == "데빌헌터":
            user3 = f"{interaction.user.display_name}(데빌헌터)"
        elif self.values[0] == "블래스터":
            user3 = f"{interaction.user.display_name}(블래스터)"
        elif self.values[0] == "호크아이":
            user3 = f"{interaction.user.display_name}(호크아이)"
        elif self.values[0] == "스카우터":
            user3 = f"{interaction.user.display_name}(스카우터)"
        elif self.values[0] == "건슬링어":
            user3 = f"{interaction.user.display_name}(건슬링어)"
        elif self.values[0] == "아르카나":
            user3 = f"{interaction.user.display_name}(아르카나)"
        elif self.values[0] == "서머너":
            user3 = f"{interaction.user.display_name}(서머너)"
        elif self.values[0] == "바드":
            user3 = f"{interaction.user.display_name}(바드)"
        elif self.values[0] == "소서리스":
            user3 = f"{interaction.user.display_name}(소서리스)"
        elif self.values[0] == "데모닉":
            user3 = f"{interaction.user.display_name}(데모닉)"
        elif self.values[0] == "블레이드":
            user3 = f"{interaction.user.display_name}(블레이드)"
        elif self.values[0] == "리퍼":
            user3 = f"{interaction.user.display_name}(리퍼)"
        elif self.values[0] == "소울이터":
            user3 = f"{interaction.user.display_name}(소울이터)"
        elif self.values[0] == "도화가":
            user3 = f"{interaction.user.display_name}(도화가)"
        elif self.values[0] == "기상술사":
            user3 = f"{interaction.user.display_name}(기상술사)"
        if user3 in 1:
            y1.remove(user3)
            eb3 = Embed(title="2팟 레이드 길드 팟", description=mssg2, color=0x395bc0)
            eb3.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
            eb3.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=eb3)
            k1-1
        else:
            y1.insert(k1,user3)
            ek3 = Embed(title="2팟 레이드 길드 팟", description=mssg2, color=0x395bc0)
            ek3.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
            ek3.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=ek3)            
            k1+1
class SelectMenu4(discord.ui.Select):
    def __init__(self):
        global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5,eb1,eb2,eb3,eb4,eb5,ek1,ek2,ek3,ek4,ek5
        options4 = [discord.SelectOption(label="버서커", description="버서커"),
                   discord.SelectOption(label="디스트로이어", description="디스트로이어"),
                   discord.SelectOption(label="워로드", description="워로드"),
                   discord.SelectOption(label="홀리나이트", description="홀리나이트"),
                   discord.SelectOption(label="슬레이어", description="슬레이어"),
                   discord.SelectOption(label="배틀마스터", description="배틀마스터"),
                   discord.SelectOption(label="인파이터", description="인파이터"),
                   discord.SelectOption(label="기공사", description="기공사"),
                   discord.SelectOption(label="창술사", description="창술사"),
                   discord.SelectOption(label="스트라이커", description="스트라이커"),
                   discord.SelectOption(label="데빌헌터", description="데빌헌터"),
                   discord.SelectOption(label="블래스터", description="블래스터"),
                   discord.SelectOption(label="호크아이", description="호크아이"),
                   discord.SelectOption(label="스카우터", description="스카우터"),
                   discord.SelectOption(label="건슬링어", description="건슬링어"),
                   discord.SelectOption(label="아르카나", description="아르카나"),
                   discord.SelectOption(label="서머너", description="서머너"),
                   discord.SelectOption(label="바드", description="바드"),
                   discord.SelectOption(label="소서리스", description="소서리스"),
                   discord.SelectOption(label="데모닉", description="데모닉"),
                   discord.SelectOption(label="블레이드", description="블레이드"),
                   discord.SelectOption(label="리퍼", description="리퍼"),
                   discord.SelectOption(label="소울이터", description="소울이터"),
                   discord.SelectOption(label="도화가", description="도화가"),
                   discord.SelectOption(label="기상술사", description="기상술사")]
        super().__init__(placeholder="1 파티", max_values=1, min_values=1, options=options4)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "버서커":
            user4 = f"{interaction.user.display_name}(버서커)"
        elif self.values[0] == "디스트로이어":
            user4 = f"{interaction.user.display_name}(디스트로이어)"
        elif self.values[0] == "워로드":
            user4 = f"{interaction.user.display_name}(워로드)"
        elif self.values[0] == "홀리나이트":
            user4 = f"{interaction.user.display_name}(홀리나이트)"
        elif self.values[0] == "슬레이어":
            user4 = f"{interaction.user.display_name}(슬레이어)"
        elif self.values[0] == "배틀마스터":
            user4 = f"{interaction.user.display_name}(배틀마스터)"
        elif self.values[0] == "인파이터":
            user4 = f"{interaction.user.display_name}(인파이터)"
        elif self.values[0] == "기공사":
            user4 = f"{interaction.user.display_name}(기공사)"
        elif self.values[0] == "창술사":
            user4 = f"{interaction.user.display_name}(창술사)"
        elif self.values[0] == "스트라이커":
            user4 = f"{interaction.user.display_name}(스트라이커)"
        elif self.values[0] == "데빌헌터":
            user4 = f"{interaction.user.display_name}(데빌헌터)"
        elif self.values[0] == "블래스터":
            user4 = f"{interaction.user.display_name}(블래스터)"
        elif self.values[0] == "호크아이":
            user4 = f"{interaction.user.display_name}(호크아이)"
        elif self.values[0] == "스카우터":
            user4 = f"{interaction.user.display_name}(스카우터)"
        elif self.values[0] == "건슬링어":
            user4 = f"{interaction.user.display_name}(건슬링어)"
        elif self.values[0] == "아르카나":
            user4 = f"{interaction.user.display_name}(아르카나)"
        elif self.values[0] == "서머너":
            user4 = f"{interaction.user.display_name}(서머너)"
        elif self.values[0] == "바드":
            user4 = f"{interaction.user.display_name}(바드)"
        elif self.values[0] == "소서리스":
            user4 = f"{interaction.user.display_name}(소서리스)"
        elif self.values[0] == "데모닉":
            user4 = f"{interaction.user.display_name}(데모닉)"
        elif self.values[0] == "블레이드":
            user4 = f"{interaction.user.display_name}(블레이드)"
        elif self.values[0] == "리퍼":
            user4 = f"{interaction.user.display_name}(리퍼)"
        elif self.values[0] == "소울이터":
            user4 = f"{interaction.user.display_name}(소울이터)"
        elif self.values[0] == "도화가":
            user4 = f"{interaction.user.display_name}(도화가)"
        elif self.values[0] == "기상술사":
            user4 = f"{interaction.user.display_name}(기상술사)"
        if user4 in x2:
            x2.remove(user4)
            eb4 = Embed(title="3팟 레이드 길드 팟", description=mssg3, color=0x395bc0)
            eb4.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
            eb4.add_field(name="2 파티", value=y1[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=eb4)     
            i1-1
        else:
            x2.insert(i1,user4)
            ek4 = Embed(title="3팟 레이드 길드 팟", description=mssg3, color=0x395bc0)
            ek4.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
            ek4.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=ek4)         
            i1+1
class SelectMenu5(discord.ui.Select):
    def __init__(self):
        global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5,eb1,eb2,eb3,eb4,eb5,ek1,ek2,ek3,ek4,ek5
        options5 = [discord.SelectOption(label="버서커", description="버서커"),
                   discord.SelectOption(label="디스트로이어", description="디스트로이어"),
                   discord.SelectOption(label="워로드", description="워로드"),
                   discord.SelectOption(label="홀리나이트", description="홀리나이트"),
                   discord.SelectOption(label="슬레이어", description="슬레이어"),
                   discord.SelectOption(label="배틀마스터", description="배틀마스터"),
                   discord.SelectOption(label="인파이터", description="인파이터"),
                   discord.SelectOption(label="기공사", description="기공사"),
                   discord.SelectOption(label="창술사", description="창술사"),
                   discord.SelectOption(label="스트라이커", description="스트라이커"),
                   discord.SelectOption(label="데빌헌터", description="데빌헌터"),
                   discord.SelectOption(label="블래스터", description="블래스터"),
                   discord.SelectOption(label="호크아이", description="호크아이"),
                   discord.SelectOption(label="스카우터", description="스카우터"),
                   discord.SelectOption(label="건슬링어", description="건슬링어"),
                   discord.SelectOption(label="아르카나", description="아르카나"),
                   discord.SelectOption(label="서머너", description="서머너"),
                   discord.SelectOption(label="바드", description="바드"),
                   discord.SelectOption(label="소서리스", description="소서리스"),
                   discord.SelectOption(label="데모닉", description="데모닉"),
                   discord.SelectOption(label="블레이드", description="블레이드"),
                   discord.SelectOption(label="리퍼", description="리퍼"),
                   discord.SelectOption(label="소울이터", description="소울이터"),
                   discord.SelectOption(label="도화가", description="도화가"),
                   discord.SelectOption(label="기상술사", description="기상술사")]
        super().__init__(placeholder="2 파티", max_values=1, min_values=1, options=options5)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "버서커":
            user5 = f"{interaction.user.display_name}(버서커)"
        elif self.values[0] == "디스트로이어":
            user5 = f"{interaction.user.display_name}(디스트로이어)"
        elif self.values[0] == "워로드":
            user5 = f"{interaction.user.display_name}(워로드)"
        elif self.values[0] == "홀리나이트":
            user5 = f"{interaction.user.display_name}(홀리나이트)"
        elif self.values[0] == "슬레이어":
            user5 = f"{interaction.user.display_name}(슬레이어)"
        elif self.values[0] == "배틀마스터":
            user5 = f"{interaction.user.display_name}(배틀마스터)"
        elif self.values[0] == "인파이터":
            user5 = f"{interaction.user.display_name}(인파이터)"
        elif self.values[0] == "기공사":
            user5 = f"{interaction.user.display_name}(기공사)"
        elif self.values[0] == "창술사":
            user5 = f"{interaction.user.display_name}(창술사)"
        elif self.values[0] == "스트라이커":
            user5 = f"{interaction.user.display_name}(스트라이커)"
        elif self.values[0] == "데빌헌터":
            user5 = f"{interaction.user.display_name}(데빌헌터)"
        elif self.values[0] == "블래스터":
            user5 = f"{interaction.user.display_name}(블래스터)"
        elif self.values[0] == "호크아이":
            user5 = f"{interaction.user.display_name}(호크아이)"
        elif self.values[0] == "스카우터":
            user5 = f"{interaction.user.display_name}(스카우터)"
        elif self.values[0] == "건슬링어":
            user5 = f"{interaction.user.display_name}(건슬링어)"
        elif self.values[0] == "아르카나":
            user5 = f"{interaction.user.display_name}(아르카나)"
        elif self.values[0] == "서머너":
            user5 = f"{interaction.user.display_name}(서머너)"
        elif self.values[0] == "바드":
            user5 = f"{interaction.user.display_name}(바드)"
        elif self.values[0] == "소서리스":
            user5 = f"{interaction.user.display_name}(소서리스)"
        elif self.values[0] == "데모닉":
            user5 = f"{interaction.user.display_name}(데모닉)"
        elif self.values[0] == "블레이드":
            user5 = f"{interaction.user.display_name}(블레이드)"
        elif self.values[0] == "리퍼":
            user5 = f"{interaction.user.display_name}(리퍼)"
        elif self.values[0] == "소울이터":
            user5 = f"{interaction.user.display_name}(소울이터)"
        elif self.values[0] == "도화가":
            user5 = f"{interaction.user.display_name}(도화가)"
        elif self.values[0] == "기상술사":
            user5 = f"{interaction.user.display_name}(기상술사)"
        if user5 in y2:
            y2.remove(user5)
            eb5 = Embed(title="3팟 레이드 길드 팟", description=mssg3, color=0x395bc0)
            eb5.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
            eb5.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=eb5)      
            i2-1
        else:
            y2.insert(k2,user5)
            ek5 = Embed(title="3팟 레이드 길드 팟", description=mssg3, color=0x395bc0)
            ek5.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
            ek5.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=ek5)       
            k2+1
class SelectMenu6(discord.ui.Select):
    def __init__(self):
        global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5,eb1,eb2,eb3,eb4,eb5,ek1,ek2,ek3,ek4,ek5
        options6 = [discord.SelectOption(label="버서커", description="버서커"),
                   discord.SelectOption(label="디스트로이어", description="디스트로이어"),
                   discord.SelectOption(label="워로드", description="워로드"),
                   discord.SelectOption(label="홀리나이트", description="홀리나이트"),
                   discord.SelectOption(label="슬레이어", description="슬레이어"),
                   discord.SelectOption(label="배틀마스터", description="배틀마스터"),
                   discord.SelectOption(label="인파이터", description="인파이터"),
                   discord.SelectOption(label="기공사", description="기공사"),
                   discord.SelectOption(label="창술사", description="창술사"),
                   discord.SelectOption(label="스트라이커", description="스트라이커"),
                   discord.SelectOption(label="데빌헌터", description="데빌헌터"),
                   discord.SelectOption(label="블래스터", description="블래스터"),
                   discord.SelectOption(label="호크아이", description="호크아이"),
                   discord.SelectOption(label="스카우터", description="스카우터"),
                   discord.SelectOption(label="건슬링어", description="건슬링어"),
                   discord.SelectOption(label="아르카나", description="아르카나"),
                   discord.SelectOption(label="서머너", description="서머너"),
                   discord.SelectOption(label="바드", description="바드"),
                   discord.SelectOption(label="소서리스", description="소서리스"),
                   discord.SelectOption(label="데모닉", description="데모닉"),
                   discord.SelectOption(label="블레이드", description="블레이드"),
                   discord.SelectOption(label="리퍼", description="리퍼"),
                   discord.SelectOption(label="소울이터", description="소울이터"),
                   discord.SelectOption(label="도화가", description="도화가"),
                   discord.SelectOption(label="기상술사", description="기상술사")]
        super().__init__(placeholder="1 파티", max_values=1, min_values=1, options=options6)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "버서커":
            user6 = f"{interaction.user.display_name}(버서커)"
        elif self.values[0] == "디스트로이어":
            user6 = f"{interaction.user.display_name}(디스트로이어)"
        elif self.values[0] == "워로드":
            user6 = f"{interaction.user.display_name}(워로드)"
        elif self.values[0] == "홀리나이트":
            user6 = f"{interaction.user.display_name}(홀리나이트)"
        elif self.values[0] == "슬레이어":
            user6 = f"{interaction.user.display_name}(슬레이어)"
        elif self.values[0] == "배틀마스터":
            user6 = f"{interaction.user.display_name}(배틀마스터)"
        elif self.values[0] == "인파이터":
            user6 = f"{interaction.user.display_name}(인파이터)"
        elif self.values[0] == "기공사":
            user6 = f"{interaction.user.display_name}(기공사)"
        elif self.values[0] == "창술사":
            user6 = f"{interaction.user.display_name}(창술사)"
        elif self.values[0] == "스트라이커":
            user6 = f"{interaction.user.display_name}(스트라이커)"
        elif self.values[0] == "데빌헌터":
            user6 = f"{interaction.user.display_name}(데빌헌터)"
        elif self.values[0] == "블래스터":
            user6 = f"{interaction.user.display_name}(블래스터)"
        elif self.values[0] == "호크아이":
            user6 = f"{interaction.user.display_name}(호크아이)"
        elif self.values[0] == "스카우터":
            user6 = f"{interaction.user.display_name}(스카우터)"
        elif self.values[0] == "건슬링어":
            user6 = f"{interaction.user.display_name}(건슬링어)"
        elif self.values[0] == "아르카나":
            user6 = f"{interaction.user.display_name}(아르카나)"
        elif self.values[0] == "서머너":
            user6 = f"{interaction.user.display_name}(서머너)"
        elif self.values[0] == "바드":
            user6 = f"{interaction.user.display_name}(바드)"
        elif self.values[0] == "소서리스":
            user6 = f"{interaction.user.display_name}(소서리스)"
        elif self.values[0] == "데모닉":
            user6 = f"{interaction.user.display_name}(데모닉)"
        elif self.values[0] == "블레이드":
            user6 = f"{interaction.user.display_name}(블레이드)"
        elif self.values[0] == "리퍼":
            user6 = f"{interaction.user.display_name}(리퍼)"
        elif self.values[0] == "소울이터":
            user6 = f"{interaction.user.display_name}(소울이터)"
        elif self.values[0] == "도화가":
            user6 = f"{interaction.user.display_name}(도화가)"
        elif self.values[0] == "기상술사":
            user6 = f"{interaction.user.display_name}(기상술사)"
        if user6 in x3:
            x3.remove(user6)
            eb6 = Embed(title="4팟 레이드 길드 팟", description=mssg4, color=0x395bc0)
            eb6.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
            eb6.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=eb6)            
            i3-1
        else:
            x3.insert(i3,user6)
            ek6 = Embed(title="4팟 레이드 길드 팟", description=mssg4, color=0x395bc0)
            ek6.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
            ek6.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=ek6)            
            i3+1
class SelectMenu7(discord.ui.Select):
    def __init__(self):
        global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5,eb1,eb2,eb3,eb4,eb5,ek1,ek2,ek3,ek4,ek5
        options7 = [discord.SelectOption(label="버서커", description="버서커"),
                   discord.SelectOption(label="디스트로이어", description="디스트로이어"),
                   discord.SelectOption(label="워로드", description="워로드"),
                   discord.SelectOption(label="홀리나이트", description="홀리나이트"),
                   discord.SelectOption(label="슬레이어", description="슬레이어"),
                   discord.SelectOption(label="배틀마스터", description="배틀마스터"),
                   discord.SelectOption(label="인파이터", description="인파이터"),
                   discord.SelectOption(label="기공사", description="기공사"),
                   discord.SelectOption(label="창술사", description="창술사"),
                   discord.SelectOption(label="스트라이커", description="스트라이커"),
                   discord.SelectOption(label="데빌헌터", description="데빌헌터"),
                   discord.SelectOption(label="블래스터", description="블래스터"),
                   discord.SelectOption(label="호크아이", description="호크아이"),
                   discord.SelectOption(label="스카우터", description="스카우터"),
                   discord.SelectOption(label="건슬링어", description="건슬링어"),
                   discord.SelectOption(label="아르카나", description="아르카나"),
                   discord.SelectOption(label="서머너", description="서머너"),
                   discord.SelectOption(label="바드", description="바드"),
                   discord.SelectOption(label="소서리스", description="소서리스"),
                   discord.SelectOption(label="데모닉", description="데모닉"),
                   discord.SelectOption(label="블레이드", description="블레이드"),
                   discord.SelectOption(label="리퍼", description="리퍼"),
                   discord.SelectOption(label="소울이터", description="소울이터"),
                   discord.SelectOption(label="도화가", description="도화가"),
                   discord.SelectOption(label="기상술사", description="기상술사")]
        super().__init__(placeholder="2 파티", max_values=1, min_values=1, options=options7)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "버서커":
            user7 = f"{interaction.user.display_name}(버서커)"
        elif self.values[0] == "디스트로이어":
            user7 = f"{interaction.user.display_name}(디스트로이어)"
        elif self.values[0] == "워로드":
            user7 = f"{interaction.user.display_name}(워로드)"
        elif self.values[0] == "홀리나이트":
            user7 = f"{interaction.user.display_name}(홀리나이트)"
        elif self.values[0] == "슬레이어":
            user7 = f"{interaction.user.display_name}(슬레이어)"
        elif self.values[0] == "배틀마스터":
            user7 = f"{interaction.user.display_name}(배틀마스터)"
        elif self.values[0] == "인파이터":
            user7 = f"{interaction.user.display_name}(인파이터)"
        elif self.values[0] == "기공사":
            user7 = f"{interaction.user.display_name}(기공사)"
        elif self.values[0] == "창술사":
            user7 = f"{interaction.user.display_name}(창술사)"
        elif self.values[0] == "스트라이커":
            user7 = f"{interaction.user.display_name}(스트라이커)"
        elif self.values[0] == "데빌헌터":
            user7 = f"{interaction.user.display_name}(데빌헌터)"
        elif self.values[0] == "블래스터":
            user7 = f"{interaction.user.display_name}(블래스터)"
        elif self.values[0] == "호크아이":
            user7 = f"{interaction.user.display_name}(호크아이)"
        elif self.values[0] == "스카우터":
            user7 = f"{interaction.user.display_name}(스카우터)"
        elif self.values[0] == "건슬링어":
            user7 = f"{interaction.user.display_name}(건슬링어)"
        elif self.values[0] == "아르카나":
            user7 = f"{interaction.user.display_name}(아르카나)"
        elif self.values[0] == "서머너":
            user7 = f"{interaction.user.display_name}(서머너)"
        elif self.values[0] == "바드":
            user7 = f"{interaction.user.display_name}(바드)"
        elif self.values[0] == "소서리스":
            user7 = f"{interaction.user.display_name}(소서리스)"
        elif self.values[0] == "데모닉":
            user7 = f"{interaction.user.display_name}(데모닉)"
        elif self.values[0] == "블레이드":
            user7 = f"{interaction.user.display_name}(블레이드)"
        elif self.values[0] == "리퍼":
            user7 = f"{interaction.user.display_name}(리퍼)"
        elif self.values[0] == "소울이터":
            user7 = f"{interaction.user.display_name}(소울이터)"
        elif self.values[0] == "도화가":
            user7 = f"{interaction.user.display_name}(도화가)"
        elif self.values[0] == "기상술사":
            user7 = f"{interaction.user.display_name}(기상술사)"
        if user7 in y3:
            y3.remove(user7)
            eb5 = Embed(title="4팟 레이드 길드 팟", description=mssg4, color=0x395bc0)
            eb5.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
            eb5.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=eb5)          
            k3-1
        else:
            y3.insert(k3,user7)
            ek5 = Embed(title="4팟 레이드 길드 팟", description=mssg4, color=0x395bc0)
            ek5.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
            ek5.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=ek5)           
            k3+1
class SelectMenu8(discord.ui.Select):
    def __init__(self):
        raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5,eb1,eb2,eb3,eb4,eb5,ek1,ek2,ek3,ek4,ek5
        options8 = [discord.SelectOption(label="버서커", description="버서커"),
                   discord.SelectOption(label="디스트로이어", description="디스트로이어"),
                   discord.SelectOption(label="워로드", description="워로드"),
                   discord.SelectOption(label="홀리나이트", description="홀리나이트"),
                   discord.SelectOption(label="슬레이어", description="슬레이어"),
                   discord.SelectOption(label="배틀마스터", description="배틀마스터"),
                   discord.SelectOption(label="인파이터", description="인파이터"),
                   discord.SelectOption(label="기공사", description="기공사"),
                   discord.SelectOption(label="창술사", description="창술사"),
                   discord.SelectOption(label="스트라이커", description="스트라이커"),
                   discord.SelectOption(label="데빌헌터", description="데빌헌터"),
                   discord.SelectOption(label="블래스터", description="블래스터"),
                   discord.SelectOption(label="호크아이", description="호크아이"),
                   discord.SelectOption(label="스카우터", description="스카우터"),
                   discord.SelectOption(label="건슬링어", description="건슬링어"),
                   discord.SelectOption(label="아르카나", description="아르카나"),
                   discord.SelectOption(label="서머너", description="서머너"),
                   discord.SelectOption(label="바드", description="바드"),
                   discord.SelectOption(label="소서리스", description="소서리스"),
                   discord.SelectOption(label="데모닉", description="데모닉"),
                   discord.SelectOption(label="블레이드", description="블레이드"),
                   discord.SelectOption(label="리퍼", description="리퍼"),
                   discord.SelectOption(label="소울이터", description="소울이터"),
                   discord.SelectOption(label="도화가", description="도화가"),
                   discord.SelectOption(label="기상술사", description="기상술사")]
        super().__init__(placeholder="1 파티", max_values=1, min_values=1, options=options8)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "버서커":
            user8 = f"{interaction.user.display_name}(버서커)"
        elif self.values[0] == "디스트로이어":
            user8 = f"{interaction.user.display_name}(디스트로이어)"
        elif self.values[0] == "워로드":
            user8 = f"{interaction.user.display_name}(워로드)"
        elif self.values[0] == "홀리나이트":
            user8 = f"{interaction.user.display_name}(홀리나이트)"
        elif self.values[0] == "슬레이어":
            user8 = f"{interaction.user.display_name}(슬레이어)"
        elif self.values[0] == "배틀마스터":
            user8 = f"{interaction.user.display_name}(배틀마스터)"
        elif self.values[0] == "인파이터":
            user8 = f"{interaction.user.display_name}(인파이터)"
        elif self.values[0] == "기공사":
            user8 = f"{interaction.user.display_name}(기공사)"
        elif self.values[0] == "창술사":
            user8 = f"{interaction.user.display_name}(창술사)"
        elif self.values[0] == "스트라이커":
            user8 = f"{interaction.user.display_name}(스트라이커)"
        elif self.values[0] == "데빌헌터":
            user8 = f"{interaction.user.display_name}(데빌헌터)"
        elif self.values[0] == "블래스터":
            user8 = f"{interaction.user.display_name}(블래스터)"
        elif self.values[0] == "호크아이":
            user8 = f"{interaction.user.display_name}(호크아이)"
        elif self.values[0] == "스카우터":
            user8 = f"{interaction.user.display_name}(스카우터)"
        elif self.values[0] == "건슬링어":
            user8 = f"{interaction.user.display_name}(건슬링어)"
        elif self.values[0] == "아르카나":
            user8 = f"{interaction.user.display_name}(아르카나)"
        elif self.values[0] == "서머너":
            user8 = f"{interaction.user.display_name}(서머너)"
        elif self.values[0] == "바드":
            user8 = f"{interaction.user.display_name}(바드)"
        elif self.values[0] == "소서리스":
            user8 = f"{interaction.user.display_name}(소서리스)"
        elif self.values[0] == "데모닉":
            user8 = f"{interaction.user.display_name}(데모닉)"
        elif self.values[0] == "블레이드":
            user8 = f"{interaction.user.display_name}(블레이드)"
        elif self.values[0] == "리퍼":
            user8 = f"{interaction.user.display_name}(리퍼)"
        elif self.values[0] == "소울이터":
            user8 = f"{interaction.user.display_name}(소울이터)"
        elif self.values[0] == "도화가":
            user8 = f"{interaction.user.display_name}(도화가)"
        elif self.values[0] == "기상술사":
            user8 = f"{interaction.user.display_name}(기상술사)"
        if user8 in x4:
            x4.remove(user8)
            eb8 = Embed(title="5팟 레이드 길드 팟", description=mssg5, color=0x395bc0)
            eb8.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
            eb8.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=eb8)             
            i4-1
        else:
            x4.insert(i4,user8)
            ek8 = Embed(title="5팟 레이드 길드 팟", description=mssg5, color=0x395bc0)
            ek8.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
            ek8.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=ek8)            
            i4+1
class SelectMenu9(discord.ui.Select):
    def __init__(self):
        global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5,eb1,eb2,eb3,eb4,eb5,ek1,ek2,ek3,ek4,ek5
        options9 = [discord.SelectOption(label="버서커", description="버서커"),
                   discord.SelectOption(label="디스트로이어", description="디스트로이어"),
                   discord.SelectOption(label="워로드", description="워로드"),
                   discord.SelectOption(label="홀리나이트", description="홀리나이트"),
                   discord.SelectOption(label="슬레이어", description="슬레이어"),
                   discord.SelectOption(label="배틀마스터", description="배틀마스터"),
                   discord.SelectOption(label="인파이터", description="인파이터"),
                   discord.SelectOption(label="기공사", description="기공사"),
                   discord.SelectOption(label="창술사", description="창술사"),
                   discord.SelectOption(label="스트라이커", description="스트라이커"),
                   discord.SelectOption(label="데빌헌터", description="데빌헌터"),
                   discord.SelectOption(label="블래스터", description="블래스터"),
                   discord.SelectOption(label="호크아이", description="호크아이"),
                   discord.SelectOption(label="스카우터", description="스카우터"),
                   discord.SelectOption(label="건슬링어", description="건슬링어"),
                   discord.SelectOption(label="아르카나", description="아르카나"),
                   discord.SelectOption(label="서머너", description="서머너"),
                   discord.SelectOption(label="바드", description="바드"),
                   discord.SelectOption(label="소서리스", description="소서리스"),
                   discord.SelectOption(label="데모닉", description="데모닉"),
                   discord.SelectOption(label="블레이드", description="블레이드"),
                   discord.SelectOption(label="리퍼", description="리퍼"),
                   discord.SelectOption(label="소울이터", description="소울이터"),
                   discord.SelectOption(label="도화가", description="도화가"),
                   discord.SelectOption(label="기상술사", description="기상술사")]
        super().__init__(placeholder="2 파티", max_values=1, min_values=1, options=options9)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "버서커":
            user9 = f"{interaction.user.display_name}(버서커)"
        elif self.values[0] == "디스트로이어":
            user9 = f"{interaction.user.display_name}(디스트로이어)"
        elif self.values[0] == "워로드":
            user9 = f"{interaction.user.display_name}(워로드)"
        elif self.values[0] == "홀리나이트":
            user9 = f"{interaction.user.display_name}(홀리나이트)"
        elif self.values[0] == "슬레이어":
            user9 = f"{interaction.user.display_name}(슬레이어)"
        elif self.values[0] == "배틀마스터":
            user9 = f"{interaction.user.display_name}(배틀마스터)"
        elif self.values[0] == "인파이터":
            user9 = f"{interaction.user.display_name}(인파이터)"
        elif self.values[0] == "기공사":
            user9 = f"{interaction.user.display_name}(기공사)"
        elif self.values[0] == "창술사":
            user9 = f"{interaction.user.display_name}(창술사)"
        elif self.values[0] == "스트라이커":
            user9 = f"{interaction.user.display_name}(스트라이커)"
        elif self.values[0] == "데빌헌터":
            user9 = f"{interaction.user.display_name}(데빌헌터)"
        elif self.values[0] == "블래스터":
            user9 = f"{interaction.user.display_name}(블래스터)"
        elif self.values[0] == "호크아이":
            user9 = f"{interaction.user.display_name}(호크아이)"
        elif self.values[0] == "스카우터":
            user9 = f"{interaction.user.display_name}(스카우터)"
        elif self.values[0] == "건슬링어":
            user9 = f"{interaction.user.display_name}(건슬링어)"
        elif self.values[0] == "아르카나":
            user9 = f"{interaction.user.display_name}(아르카나)"
        elif self.values[0] == "서머너":
            user9 = f"{interaction.user.display_name}(서머너)"
        elif self.values[0] == "바드":
            user9 = f"{interaction.user.display_name}(바드)"
        elif self.values[0] == "소서리스":
            user9 = f"{interaction.user.display_name}(소서리스)"
        elif self.values[0] == "데모닉":
            user9 = f"{interaction.user.display_name}(데모닉)"
        elif self.values[0] == "블레이드":
            user9 = f"{interaction.user.display_name}(블레이드)"
        elif self.values[0] == "리퍼":
            user9 = f"{interaction.user.display_name}(리퍼)"
        elif self.values[0] == "소울이터":
            user9 = f"{interaction.user.display_name}(소울이터)"
        elif self.values[0] == "도화가":
            user9 = f"{interaction.user.display_name}(도화가)"
        elif self.values[0] == "기상술사":
            user9 = f"{interaction.user.display_name}(기상술사)"
        if user9 in y4:
            y4.remove(user9)
            eb9 = Embed(title="5팟 레이드 길드 팟", description=mssg5, color=0x395bc0)
            eb9.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
            eb9.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=eb9)      
            k4-1
        else:
            y4.insert(i4,user9)
            ek9 = Embed(title="5팟 레이드 길드 팟", description=mssg5, color=0x395bc0)
            ek9.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
            ek9.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
            await interaction.response.edit_message(embed=ek9)           
            k4+1
class select1(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectMenu())
        self.add_item(SelectMenu1())
        self.add_item(button1)
class select2(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectMenu2())
        self.add_item(SelectMenu3())
        self.add_item(button2)
class select3(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectMenu4())
        self.add_item(SelectMenu5())
        self.add_item(button3)
class select4(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectMenu6())
        self.add_item(SelectMenu7())
        self.add_item(button4)
class select5(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectMenu8())
        self.add_item(SelectMenu9())
        self.add_item(button5)

@app_commands.choices(난이도 = [
    Choice(name = '노말', value='노말'),
    Choice(name = '하드', value='하드'),
    Choice(name = '헬', value='헬'),
])
@app_commands.choices(군단장 = [
    Choice(name = '발탄', value='발탄'),
    Choice(name = '비아키스', value='비아키스'),
    Choice(name = '쿠크세이튼', value='쿠크세이튼'),
    Choice(name = '아브렐슈드', value='아브렐슈드'),
    Choice(name = '일리아칸', value='일리아칸'),
])
@app_commands.choices(숙련 = [
    Choice(name = '트라이', value='트라이'),
    Choice(name = '반숙', value='반숙'),
    Choice(name = '숙련', value='숙련'),
])

@tree.command(name = "레이드", description="레이드 일정을 추가합니다.")
async def slash2(interaction: discord.Interaction, 난이도: str, 군단장: str, 숙련: str, 일정: str):
    global raidcount,i,k,i1,k1,i2,k2,i3,k3,i4,k4,rd1,rd2,rd3,rd4,rd5,msg,msg1,msg2,msg3,msg4,mssg1,mssg2,mssg3,mssg3,mssg4,mssg5,button1,button2,button3,button4,button5
    button1 = Button(label="수정")
    button2 = Button(label="수정")
    button3 = Button(label="수정")
    button4 = Button(label="수정")
    button5 = Button(label="수정")

    async def button_callback1(interaction:discord.Interaction):
        await interaction.response.send_modal(MyModal())
    async def button_callback2(interaction:discord.Interaction):
        await interaction.response.send_modal(MyModal1())
    async def button_callback3(interaction:discord.Interaction):
        await interaction.response.send_modal(MyModal2())
    async def button_callback4(interaction:discord.Interaction):
        await interaction.response.send_modal(MyModal3())
    async def button_callback5(interaction:discord.Interaction):
        await interaction.response.send_modal(MyModal4())

    button1.callback = button_callback1
    button2.callback = button_callback2
    button3.callback = button_callback3
    button4.callback = button_callback4
    button5.callback = button_callback5

    rolesx = discord.utils.get(interaction.guild.roles, name="관리자")
    rolesx1 = discord.utils.get(interaction.guild.roles, name="비틱궁당장")
    if rolesx in interaction.user.roles or rolesx1 in interaction.user.roles:
            if raidcount == 0:
                        mssg1=f"{난이도} {군단장}  {숙련}  {일정}"
                        abc = Embed(title="1팟 레이드 길드 팟", description=mssg1, color=0x395bc0)
                        abc.add_field(name="1 파티", value=x[0]+"\n"+x[1]+"\n"+x[2]+"\n"+x[3]+"\n", inline=True)
                        abc.add_field(name="2 파티", value=y[0]+"\n"+y[1]+"\n"+y[2]+"\n"+y[3]+"\n", inline=True)
                        await interaction.response.send_message(embed=abc,view=select1())
                        msg = await interaction.original_response()
                        raidcount += 1
            elif raidcount == 1:
                        mssg2=f"{난이도} {군단장}  {숙련}  {일정}"
                        abc1 = Embed(title='2팟 레이드 길드 팟',description=mssg2, color=0x395bc0)
                        abc1.add_field(name="1 파티", value=x1[0]+"\n"+x1[1]+"\n"+x1[2]+"\n"+x1[3]+"\n", inline=True)
                        abc1.add_field(name="2 파티", value=y1[0]+"\n"+y1[1]+"\n"+y1[2]+"\n"+y1[3]+"\n", inline=True)
                        await interaction.response.send_message(embed=abc1,view=select2())
                        msg1 = await interaction.original_response()
                        raidcount += 1
            elif raidcount == 2:
                        mssg3=f"{난이도} {군단장}  {숙련}  {일정}"
                        abc2 = Embed(title='3팟 레이드 길드 팟',description=mssg3, color=0x395bc0)
                        abc2.add_field(name="1 파티", value=x2[0]+"\n"+x2[1]+"\n"+x2[2]+"\n"+x2[3]+"\n", inline=True)
                        abc2.add_field(name="2 파티", value=y2[0]+"\n"+y2[1]+"\n"+y2[2]+"\n"+y2[3]+"\n", inline=True)
                        await interaction.response.send_message(embed=abc2,view=select3())
                        msg2 = await interaction.original_response()
                        raidcount += 1
            elif raidcount == 3:
                        mssg4=f"{난이도} {군단장}  {숙련}  {일정}"
                        abc3 = Embed(title='4팟 레이드 길드 팟',description=mssg4, color=0x395bc0)
                        abc3.add_field(name="1 파티", value=x3[0]+"\n"+x3[1]+"\n"+x3[2]+"\n"+x3[3]+"\n", inline=True)
                        abc3.add_field(name="2 파티", value=y3[0]+"\n"+y3[1]+"\n"+y3[2]+"\n"+y3[3]+"\n", inline=True)
                        await interaction.response.send_message(embed=abc3,view=select4())
                        msg3 = await interaction.original_response()
                        raidcount += 1
            elif raidcount == 4:
                        mssg5=f"{난이도} {군단장}  {숙련}  {일정}"
                        abc4 = Embed(title='5팟 레이드 길드 팟',description=mssg5, color=0x395bc0)
                        abc4.add_field(name="1 파티", value=x4[0]+"\n"+x4[1]+"\n"+x4[2]+"\n"+x4[3]+"\n", inline=True)
                        abc4.add_field(name="2 파티", value=y4[0]+"\n"+y4[1]+"\n"+y4[2]+"\n"+y4[3]+"\n", inline=True)
                        await interaction.response.send_message(embed=abc4,view=select5())
                        msg4 = await interaction.original_response()
                        raidcount += 1
            if raidcount == 5:
                        await interaction.response.send_message("풀파티입니다.")
    else:
        await interaction.response.send_message("관리자가 아닙니다.")
        
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
    raidhelp = Embed(title='딜컷 파티모집기',description="사용법", color=0xb3be23)
    raidhelp.add_field(name="/레이드", value="레이드 일정을 만듭니다.(max 5팟)", inline=False)
    raidhelp.add_field(name="/레이드수정", value="1팟~5팟 레이드 일정을 수정합니다.", inline=False)
    raidhelp.add_field(name="/레이드초기화", value="레이드 일정을 초기화합니다.", inline=False)
    raidhelp.set_footer(text="로요일마다 초기화하신 후 사용해주세요.")
    await interaction.response.send_message(embed=raidhelp,ephemeral=True) 
  
@tree.command(name = "파티모집기도움말",description="파티모집 어떻게 사용하나요?)")
async def slash5(interaction: discord.Interaction):
    raidhelp1 = Embed(title='딜컷 파티모집기',description="사용법", color=0xb3be23)
    raidhelp1.add_field(name="/레이드", value="레이드 일정을 만듭니다.(max 5팟)", inline=False)
    raidhelp1.add_field(name="/레이드수정", value="1팟~5팟 레이드 일정을 수정합니다.", inline=False)
    raidhelp1.add_field(name="/레이드초기화", value="레이드 일정을 초기화합니다.", inline=False)
    raidhelp1.set_footer(text="로요일마다 초기화하신 후 사용해주세요.")
    await interaction.response.send_message(embed=raidhelp1,ephemeral=False) 
 
client.run(TOKEN)
