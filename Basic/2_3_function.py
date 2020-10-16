#Absolute
print(abs(-30))
#Exponential
print(pow(4,2)) # pow(4,2)=4**2=16

#min, max
print(max(5,12)) 
print(min(5,12))

#round up and down
print(round(3.14))
print(round(4.99))


print("--------have to use with 'from math import'--------")
#from math import *과 같이 사용할 수도 있으나, *을 사용할 경우 모든 함수를 가져오게됨. 
from math import ceil
from math import floor
from math import sqrt

#ceil and floor
print(ceil(3.14))
print(floor(4.99))
print(sqrt(16))