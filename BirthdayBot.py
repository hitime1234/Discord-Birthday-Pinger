#Birthdays
import BirthdayDB
global BirthdayList
BirthdayList = BirthdayDB.BirthDB()
#discord imports
from discord.utils import get
import discord
from discord import app_commands
from discord.ext import commands, tasks


try:
    with open("token.txt", "r") as f:
        TOKEN = f.readline().strip()
except:
    print("No token.txt found")
    if input("Press Enter to exit and create one") == "":
        with open("token.txt", "w") as f:
            f.write(input("Enter Token: "))
        exit()
    else:
        TOKEN = ""
try:
    with open("guild.txt", "r") as f:
        MY_GUILD = discord.Object(id=int(f.readline().strip()))
except:
    print("No guild.txt found")
    if input("Press Enter to exit and create one") == "":
        with open("guild.txt", "w") as f:
            f.write(input("Enter Discord Server ID: "))
        exit()
    else:
        MY_GUILD = 0

try:
    with open("channel.txt", "r") as f:
        Annoucements = int(f.readline().strip())
except:
    print("channel.txt found")
    if input("Press Enter to exit and create one") == "":
        with open("channel.txt", "w") as f:
            f.write(input("Enter Channel ID: "))
        exit()
    else:
        Annoucements = 0

try:
    with open("role.txt", "r") as f:
        for line in f:
            roles = line.split("\n")
            roles = [int(role.strip()) for role in roles]
except:
    print("No role.txt found")
    if input("Press Enter to exit and create one.\nYou can add additional ones in a new line of txt") == "":
        with open("role.txt", "w") as f:
            f.write(input("Enter Role ID: "))
        exit()
    else:
        roles = [] 
    



class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(command_prefix="?",intents=intents)
        self.tree = app_commands.CommandTree(self)
        
    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

    #checks everyday for a new birthday
    @tasks.loop(hours=24)
    async def birthdayloop(self):
        global BirthdayList,Annoucements
        print("Checking Birthdays")
        channel = client.get_channel(Annoucements)
        if BirthdayList.GetAllBirthdaysToday() == None:
            pass
        else:
            for person in BirthdayList.GetAllBirthdaysToday():
                await channel.send(person.BirthdayMessage())


intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.tree.command(name='addbirthday',guild=MY_GUILD,description='Adds a BirthdayToList Of birthdays')
@app_commands.checks.has_any_role(*roles) 
async def addBirthday(interaction: discord.Interaction, name: str, discordid: str, birthday: int, birthmonth: int, birthyear: int, message: str):
    global BirthdayList
    Person = BirthdayList.AddBirthday(name, discordid, birthday, birthmonth, birthyear, message)
    await interaction.response.send_message(str(Person) + "\nBirthday Added",ephemeral=True)
    print(str(Person) + " Birthday Added")


@client.tree.command(name='getbirthdays',guild=MY_GUILD,description='Gets BirthdayList')
@app_commands.checks.has_any_role(*roles) 
async def GetAllBirthdays(interaction: discord.Interaction):
    global BirthdayList
    await interaction.response.send_message(BirthdayList.GetAllBirthdays())

@client.tree.command(name='removebirthday',guild=MY_GUILD,description='Removes a Birthday from List Of birthdays')
@app_commands.checks.has_any_role(*roles) 
async def removeBirthday(interaction: discord.Interaction, discordid: str):
    global BirthdayList
    if BirthdayList.RemoveBirthday(discordid):
        await interaction.response.send_message("Birthday Removed",ephemeral=True)
    else:
        await interaction.response.send_message("Birthday not found",ephemeral=True)

@client.tree.command(name='resetbirthdays',guild=MY_GUILD,description='Resets BirthdayList')
@app_commands.checks.has_any_role(*roles) 
async def resetBirthdays(interaction: discord.Interaction):
    global BirthdayList
    BirthdayList.resetBirthdays()
    await interaction.response.send_message("Birthdays Reset",ephemeral=True)

@client.tree.command(name='getbirthday',guild=MY_GUILD,description='Gets Birthday by ID')
@app_commands.checks.has_any_role(*roles)
async def getBirthday(interaction: discord.Interaction, discordid: str):
    global BirthdayList
    await interaction.response.send_message(BirthdayList.GetBirthdayByID(discordid) or "Birthday not found",ephemeral=True)

#events
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------------------------------------------------')
    client.birthdayloop.start()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="Keeping Track Of Birthdays"))

#runs the bot
if __name__ == "__main__":    
    client.run(TOKEN)    

