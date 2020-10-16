
# # input : 사용자 입력을 받는 함수
# language = input("어떤 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다.".format(language))

# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

# name = "kang"
# print(dir(name))


#https://docs.python.org/ko/3/library/functions.html#input 을 확인하면 다양한 내장 함수를 확인가능, 바로 사용할 수 있는 함수들.

#https://docs.python.org/ko/3/py-modindex.html#cap-r 를 확인하면 다양한 외장함수 확인가능, import를 이용하여 불러와야 사용가능한 함수들.

#경로내의 폴더, 파일 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py"))

#os : 운영체제에서 제공하는 기본 기능, getcwd : 현제 디렉토리
# import os
# print(os.getcwd())

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다. 삭제합니다.")
#     os.rmdir(folder)
    
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# time : 시간 관련 함수 
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())
today = datetime.date.today()
td = datetime.timedelta(days=100) # 100일 저장
print("오늘 부터 100일 후는", today+td)