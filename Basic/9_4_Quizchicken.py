
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    chicken = 10
    waiting = 1
    




    while(True):
        print("[remaining chicken : {0}]".format(chicken))
        order = int(input("how many chicken do you want?"))
        if order <= chicken:
            print("[Order number : {0}] {1} of chicken(s) is(are) ordered".format(waiting, order))
            waiting += 1
            chicken -= order
            if chicken == 0:
                print
                raise SoldOutError("")
        else:
            print("remaining chicken is not enough.")


except ValueError:
    print("wrong input value")
except SoldOutError as err:
    print("Sold Out no more order")

###################################################################
###################################################################



