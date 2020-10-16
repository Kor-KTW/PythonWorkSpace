from random import *
comment_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

shuffle(comment_list)
winners_list=sample(comment_list, 4)
print(" -- winner announcement -- ")
print("dinner dinner chicken dinner :",winners_list[0])
print("cat poooooo coffee :",winners_list[1:4])
print(" -- 축하합니다 -- ")

####################################################################
users = range(1, 21) #1~20까지 숫자를 생성
print(type(users))
users=list(users)
print(type(users))
print(users)