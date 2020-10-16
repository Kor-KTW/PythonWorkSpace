class SoldoutError(Exception):
    pass

try:
    chicken = 10
    waiting = 1
    while chicken != 0:
        
        a=int(input("어서오십시오 몇마리의 치킨을 주문하시겠습니까?"))
        if a > chicken:
            print("죄송합니다. 현재 최대 {0}마리의 치킨을 주문하실 수 있습니다.".format(chicken))
            b=input("{0}마리의 치킨이라도 주문 하시겠습니까? yes/no".format(chicken))
            if b == "yes":
                print("{0}마리의 치킨을 주문하셨습니다. 대기번호는 {1}번 입니다.".format(chicken,waiting))
                chicken = 0
                raise SoldoutError()
            else:
                print("안녕히가십시오 다음에 뵙겠습니다.")
                print("다음 손님?")
        if a < chicken:
            print("{0}마리의 치킨을 주문하셨습니다. 대기번호는 {1}번 입니다.".format(a,waiting))
            print("다음 손님?")
            waiting +=1

        if a == chicken:
            print("{0}마리의 치킨을 주문하셨습니다. 대기번호는 {1}번 입니다.".format(a,waiting))
            raise SoldoutError()

except ValueError:
    print("잘못된 값을 입력하셨습니다.")

except SoldoutError:
    print("다른 손님분들껜 죄송하지만, 재료가 소진되어 더이상 주문을 받지 않습니다.\n다음에 뵙겠습니다.")