#self 가 없는건 외부에서 받아온 데이터.
class Unit:
    def __init__(self, name, hp):
        self.name = name 
        self.hp = hp
    
class AssultUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1= AssultUnit("Firebat", 50, 16)
firebat1.attack("5si")

firebat1.damaged(25)
firebat1.damaged(25)
