# marine : asult unit, soldier, use gun

marine_name = "marine"
marine_hp = 40
marine_damage = 5

print("{0} unit is created".format(marine_name))
print("hp {0}, damage {1}\n".format(marine_hp, marine_damage))

tank_name = "tank"
tank_hp = 150
tank_damage = 35

tank2_name = "tank"
tank2_hp = 150
tank2_damage = 35
print("{0} unit is created".format(tank_name))
print("hp {0}, damage {1}\n".format(tank_hp, tank_damage))
print("{0} unit is created".format(tank2_name))
print("hp {0}, damage {1}\n".format(tank2_hp, tank2_damage))
def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(marine_name, "1시", marine_damage)
attack(tank_name, "1시", tank_damage)

#using class 

print("-------------using class-------------")
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name 
        self.hp = hp
        self.damage = damage
        print("{0} unit is created".format(self.name))
        print("hp {0}, damage {1}\n".format(self.hp, self.damage))


marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank1 = Unit("Tank", 150, 35)
