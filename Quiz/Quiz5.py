from random import randint
a = []
c = []
for i in range(1,51):
    b = randint(5,50)
    a.append(b)
    if b > 15 :
        print("[ ] {0} 번째 손님 (소요시간 : {1}분)".format(i,b))
    elif b <= 15:
        c.append(b)
        print("[0] {0} 번째 손님 (소요시간 : {1}분)".format(i,b))

print("총 탑승 승객 : {0} 명".format(len(c)))