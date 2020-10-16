from random import shuffle
from random import sample

lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
a = sample(lst,4)
print(a)

winner = a[0]
semi_winner = a[1:4]
print("["+str(winner)+"]",semi_winner)

print("- - 당첨자 발표 - -")
print("치킨 당첨자 : ["+str(winner)+"]")
print("커피 당첨자 :",semi_winner)
print("- - 축하 합니다 - -")