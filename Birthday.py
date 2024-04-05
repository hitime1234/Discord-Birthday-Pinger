from datetime import datetime
class BirthdayPerson:
    #initialize class of the person's birthday
    def __init__(self, name, DISCORDID: str, Birthday, BirthMonth, BirthYear,Message):
        self.name = name
        self.discordID = DISCORDID
        self.Birthday = int(Birthday)
        self.BirthMonth = int(BirthMonth)
        self.BirthYear = int(BirthYear)
        self.customMessage = Message
    
    #Check if it is the person's birthday
    def IsBirthday(self):
        
        # Check if it's a leap year
        if datetime.now().year % 4 == 0:
            #assumes all days are fine
            if self.Birthday == datetime.now().day and self.BirthMonth == datetime.now().month:
                return True
            else:
                return False    
        else:
            #assumes leap year birthdays are on 28 instead of 29
            if self.Birthday == datetime.now().day and self.BirthMonth == datetime.now().month:
                return True
            else:
                if self.Birthday == 29 and self.BirthMonth == 2:
                    if datetime.now().day == 28 and datetime.now().month == 2:
                        return True
                else:
                    return False

         
    #Get the age of the person
    def GetAge(self):
        if datetime.now() < datetime(datetime.now().year,self.BirthMonth,self.Birthday):
            #correct for the age not being correct if the birthday has not yet happened
            return (datetime.now().year-1) - self.BirthYear
        else:
            return (datetime.now().year) - self.BirthYear
        
    #Get String Of that person
    def __str__(self):
        return f"{self.name} with discord ID {self.discordID} is {self.GetAge()} years old. Birthday is on {self.Birthday}/{self.BirthMonth}/{self.BirthYear}"

    def BirthdayMessage(self):
        return f"{self.discordID}, Happy Birthday! {self.customMessage}.  You're {self.GetAge()} years old today!"
