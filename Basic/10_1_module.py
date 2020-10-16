#module 호출 하기.
import for_module_10_1_1
for_module_10_1_1.price(3)
for_module_10_1_1.price_morning(3)
for_module_10_1_1.price_soldier(30)

#모듈 호출 후 별명 지정
import for_module_10_1_1 as mv
mv.price_soldier(3)
mv.price_morning(3)
mv.price(3)

#모듈 내 함수 호출.
from for_module_10_1_1 import * 
price(3)
price_morning(4)
price_soldier(5)

from for_module_10_1_1 import price_soldier as prices
prices(3)