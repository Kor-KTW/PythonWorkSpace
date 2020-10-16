#overloading 메소드의 사용에서 부모말고 자식에서 사용하고싶을때


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name 
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AssultUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

class aircraft:
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" .format(name, location, self.flying_speed))

class assult_aircraft(AssultUnit, aircraft):
    def __init__(self, name, hp, damage, flying_speed):
        AssultUnit.__init__(self, name,hp,0,damage)#지상 speed 0
        aircraft.__init__(self, flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = AssultUnit("vulture", 80, 10, 20)
battlecruiser = assult_aircraft("battlecruiser", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("9시")
#오버로딩을 통해 move로 move와 fly를 통일시킴