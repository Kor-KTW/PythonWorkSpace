from random import *
cnt = 0
for i in range(1, 51):
    a = randint(5,51)
    print(str(i)+"번째 손님 (소요시간 : "+ str(a) + ")")
    if a < 15 :
        cnt+=1

print("총 탑승 승객 :", cnt,"분")