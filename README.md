# usage 
run BirthdayBot.py

you will need to rerun it 3 times or manually make

token.txt - token for bot from discord.com/developers

role.txt - can accept mutiple role ids on new lines

channel.txt

# requirements 

Requirments are in requirements.txt

but the only requirement is discord.py

# commands

all commands will be role locked to roles as stated in role.txt

/addbirthday name: str, discordid: str, birthday: int, birthmonth: int, birthyear: int, message: str

/getbirthdays 

/removebirthday discordid: str

/resetbirthdays

*future commands might appear here*

# naming schemes

discordid / self.discordID: can be anything. But it's best you do @hitime for example as it will appear <@yourdiscordid> in messages and will ping the person

message / self.customMessage: is any kind of string 

# changing BirthdayMessage:

In birthdayPerson Class in birthday.py

line 47:

return f"{self.discordID}, Happy Birthday! {self.customMessage}.  You're {self.GetAge()} years old today!" 
- is the default

