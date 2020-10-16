from random import *

print(random())
#0.0~1.0 임의의 값 생성 
#정확한 범위는 1.0을 포함하지 않는 범위 (0.0 <= x < 1.0)

print(random()*10) # 0.0~10

print(int(3.999999999))
print("-----Lottery-----")
print("")
print("---using random---")
print(int(random()*30)+1) #1~30 이하의 임의의 값 생성
print(int(random()*30)+1)
print(int(random()*30)+1)
print(int(random()*30)+1)

print("---using randrange---")
print(randrange(1,31)) #1~31 미만의 임의의 값 생성
print(randrange(1,31))
print(randrange(1,31))
print(randrange(1,31))

print("---using randint---")
print(randint(1,30)) #1~30 이하의 임의의 값 생성
print(randint(1,30))
print(randint(1,30))
print(randint(1,30))

lst = [1,2,3,4,5]
shuffle(lst)
print(lst)
print(sample(lst,  1))