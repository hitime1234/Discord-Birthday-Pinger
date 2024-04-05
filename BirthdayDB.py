from Birthday import BirthdayPerson

FileOFDates = "BirthdayDB.txt"


class BirthDB:

    def __init__(self):
        hold = self.LoadBirthdays()
        if hold == None:
            self.BirthdayList = []
        else:
            self.BirthdayList = hold

    def LoadBirthdays(self):
        try:
            with open(FileOFDates, "r") as f:
                return [BirthdayPerson(*line.strip().split(",")) for line in f]
        except FileNotFoundError:
            print("No Birthdays Found")
            return []
            
    def SaveBirthdays(self):
        with open(FileOFDates, "w") as f:
            for person in self.BirthdayList:
                f.write(f"{person.name},{person.discordID},{person.Birthday},{person.BirthMonth},{person.BirthYear},{person.customMessage}\n")

    def AddBirthday(self, name, DISCORDID, Birthday, BirthMonth, BirthYear, Message):
        for person in self.BirthdayList:
            if person.discordID == DISCORDID:
                return "DUPLICATE IDS"
        
        NewPerson = BirthdayPerson(name, DISCORDID, int(Birthday), int(BirthMonth), int(BirthYear), Message)
        self.BirthdayList.append(NewPerson)
        self.SaveBirthdays()
        return NewPerson


    def RemoveBirthday(self, DISCORDID):
        for person in self.BirthdayList:
            if person.discordID == DISCORDID:
                self.BirthdayList.remove(person)
                self.SaveBirthdays()
                return True
        return False
    
    def resetBirthdays(self):
        self.BirthdayList = []
        self.SaveBirthdays()
    
    def GetAllBirthdaysToday(self):
        List = []
        if self.BirthdayList == []:
            return None
        for person in self.BirthdayList:
            if person.IsBirthday():
                List.append(person)
        if List == []:
            return None
        else:
            return List

    def GetBirthdayMessagesForToday(self):
        List = []
        for person in self.BirthdayList:
            if person.IsBirthday():
                List.append(person.BirthdayMessage())
        return List

    def GetAllBirthdays(self):
        list = []
        for person in self.BirthdayList:
            list.append(str(person))
        return list
            

def main():
    birth = BirthDB()
    #birth.resetBirthdays()
    #birth.AddBirthday("Test", "123456789", 1, 1, 2000, "Happy Birthday")
    #birth.AddBirthday("Test", "342874434", 5, 4, 2000, "Happy Birthday")
    #birth.AddBirthday("JACK", "490382443", 11, 8, 2004, "Happy Birthday")
    #print(birth.AddBirthday("JACKER", "490382443", 11, 8, 2004, "Happy Birthday"))
    print(birth.GetAllBirthdaysToday())
    print(birth.GetBirthdayMessagesForToday())
    print(birth.GetAllBirthdays())
    



if __name__ == "__main__":
    main()




    