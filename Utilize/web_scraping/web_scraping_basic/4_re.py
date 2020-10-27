# # 정규식 regular expression 
# ex) 주민등록번호 형태.
# 940710-1933519
# abcdef-1111111 x 

# ex) email 주소
# xodn5492@naver.com
# xodnxodn@naver@naver.com x

# ex) 차량번호
# 11가 1234
# 111가 1234
# 1123가 1234 x

# ex) ip 주소
# 192.168.0.1
# 1000.2000.3000.4000 x

import re  

# asdv, book, desk
# ca?e
# care, cafe, case, cave, cake
# caae, cabe, cace, cade, ...

p = re.compile("ca.e") # . (ca.e) : 하나의 문자를 의미 > care, cafe .... not caffe
                       #  ^ (^de): 문자열의 시작을 의미 > desk, destination ... not fade
                       #  $ (se$) : 문자열의 끝을 의미 > case, base ... not sell


def print_match(m):
    if m:
        print("m.group() :", m.group())
        print("m.string :", m.string)
        print("m.start() :", m.start())
        print("m.end() :", m.end())
        print("m.span() :", m.span())
    else:
        print("매칭되지 않았습니다.")

#m = p.match("case")
m = p.match("careless") # 주어진 문자열이 처음부터 일치하는지 
# 확인하므로 care와 careless가 다르더라도 앞부분이 일치하여, match되었다고 인식.
#m = p.search("good care") # search는 주어진 문자열중에 일치하는게 있는지 확인
# print_match(m)
# print(m.group()) # 매치되지 않으면 에러발생.

lst = p.findall("good care cafe") # findall :일치하는 모든 것을 리스트 형태로 변환
# print(lst)
a = re.compile(".")
c = a.search("asdfasdf.py")
if a.search("asdfasdf.py"):
    print(c)
# print(c)
# 1. re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열이 처음부터 일치하는지
# 3. m = p.search("비교할 문자열") # search는 주어진 문자열중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") # findall :일치하는 모든 것을 리스트 형태로 변환

# . (ca.e) : 하나의 문자를 의미 > care, cafe .... not caffe
# #  ^ (^de): 문자열의 시작을 의미 > desk, destination ... not fade
#  $ (se$) : 문자열의 끝을 의미 > case, base ... not sell

#추가 공부는 w3school->python->RegEx or python re 검색.



