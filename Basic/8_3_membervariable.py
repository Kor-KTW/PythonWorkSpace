#member variable => self.name, self.hp etc, and it can use out of class
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name 
        self.hp = hp
        self.damage = damage
        print("{0} unit is created".format(self.name))
        print("hp {0}, damage {1}\n".format(self.hp, self.damage))


# marine1 = Unit("Marine", 40, 5)
# marine2 = Unit("Marine", 40, 5)
# tank1 = Unit("Tank", 150, 35)
#wraith : aircraft, clocking
wraith1 = Unit("wraith", 125, 6)
print("hp {0}, damage {1}\n".format(wraith1.hp, wraith1.damage))

wraith2 = Unit("caputred wraith", 125, 6)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} is clocking now.".format(wraith2.name))