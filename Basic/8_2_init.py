#init---생성자, class로부터 생성되는 객체(unit class의 인스턴스)에 
#대한 정보를 self 부분을 제외한 정보를 가져옴
#self를 제외한 정보의 갯수를 동일하게해야 객체를 만들수 있음.

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