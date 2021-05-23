class Traveler:
    def __init__(self,travelerName, Country, Age, countryFrom):
        self.travelerName = travelerName
        self.traveledContry = Country
        self.travelerAge = Age
        self.countryFrom = countryFrom

class TravelAgency:
    def __init__(self, travelerList):
        self.travelerList = travelerList
    def countTravelersTraveledContry(self,con):
        count = 0
        for i in self.travelerList:
            if con in i.traveledContry :
                count += 1
        return count
    
    def getTravelerTravelledMaxCountry(self):
        ma = 0
        name = ""
        for i in self.travelerList:
            if ma < len(i.traveledContry):
                ma =max(ma, len(i.traveledContry))
                name = i.travelerName
        return name
if __name__ == "__main__":
    n = int(input())
    t_ls = []
    for i in range(n):
        name = input()
        m = int(input())
        country = []
        for i in range(m):
            country.append(input())
        age = int(input())
        countryFrom = input()
        t = Traveler(name, country, age, countryFrom)
        t_ls.append(t)
    t_agn = TravelAgency(t_ls)
    c =input()
    print(t_agn.countTravelersTraveledContry(c))
    print(t_agn.getTravelerTravelledMaxCountry())
