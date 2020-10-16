
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1

while(True):
    try:
        print("[remaining chicken : {0}]".format(chicken))
        order = int(input("how many chicken do you want?"))
        if order > chicken:
            print("remaining chicken is not enough.")

        elif order <=0:
            raise ValueError

        else:
            print("[Order number : {0}] {1} of chicken(s) is(are) ordered".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError("")
    

    except ValueError:
        print("wrong input value")
    except SoldOutError:
        print("Sold Out no more order")
        break