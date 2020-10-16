#overloading 메소드의 사용에서 부모말고 자식에서 사용하고싶을때
from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name 
        self.hp = hp
        self.speed = speed

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AssultUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))


class aircraft:
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" .format(name, location, self.flying_speed))

class assult_aircraft(AssultUnit, aircraft):
    def __init__(self, name, hp, damage, flying_speed):
        AssultUnit.__init__(self, name,hp,damage,0)#지상 speed 0
        aircraft.__init__(self, flying_speed)
    def move(self, location):
        self.fly(self.name, location)

class buildingunit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self.name,hp,location)
        super().__init__(name,hp,0)
        self.location=location

supply_depot = buildingunit("supply_depot", 500, "7시")


class Marine(AssultUnit):
    def __init__(self):
        AssultUnit.__init__(self,"Marine",40,5,1)

    def stimpack(self):
        if self.hp > 10:
            self.hp -=10
            print("{0} : tsuahiya".format(self.name))
        else:
            print("{0} : not enogh hp".format(self.name))

class tank(AssultUnit):
    seize_developed = False 
    def __init__(self):
        AssultUnit.__init__(self, "Tank", 150, 35, 1)
        self.seize_mode = False

    def set_seize_mode(self):
        if tank.seize_developed == False:
            return

        #seize mode off
        if self.seize_mode == False:
            print("{0} : seize mode.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        else:
            print("{0} : tank mode.".foramt(self.name))
            self.damage /= 2
            self.seize_mode = False


class wraith(assult_aircraft):
    def __init__(self):
        assult_aircraft.__init__(self, "Warith", 80, 5, 20)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print("{0} : unclocked".format(self.name))
            self.clocked = False

        else:
            print("{0} : clocked".format(self.name))
            self.clocked = True

def game_start():
    print("game has been started.")

def game_over():
    print("player : gg")
    print("[player] left the game")

##############################################
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = tank()
t2 = tank() 
w1 = wraith()

assult_units = []
assult_units.append(m1)
assult_units.append(m2)
assult_units.append(m3)
assult_units.append(t1)
assult_units.append(t2)
assult_units.append(w1)

for unit in assult_units:
    unit.move("1시")

tank.seize_developed = True
print("upgraded complete")
#ready for battle
for unit in assult_units:
    if isinstance(unit, Marine): #>>>>>>>>만든객체가 특정 클레스의 인스턴스인지 확인
        unit.stimpack()
    if isinstance(unit, tank):
        unit.set_seize_mode()
    elif isinstance(unit, wraith):
        unit.clocking()
for unit in assult_units:
    unit.attack("1시")

#전군피해
for unit in assult_units:
    unit.damaged(randint(5,21))

game_over()