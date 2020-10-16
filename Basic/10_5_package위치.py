#package를 python의 library안에 두면 편하게 사용가능함. 
from for_package_10_2 import *
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(for_package_10_2_2))