


class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


houses = []
house1 = House("southriver", "APT", "trade", "10uk", "2010")
house2= House("mapo", "officetel", "yearly", "5uk", "2007")
house3 = House("songpa", "villa", "monthly", "500/50", "2000")
houses.append(house1)
houses.append(house2)
houses.append(house3)
print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
