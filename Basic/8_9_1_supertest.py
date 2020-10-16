class Unit:
    def __init__(self):
        print("unit 생성자")

class flyable:
    def __init__(self):
        print("flyable 생성자")

class flyableUnit( flyable, Unit):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        flyable.__init__(self)

#dropship
dropship = flyableUnit()
