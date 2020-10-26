# write는 덮어쓰기이니 주의할 것
import time
import datetime
import os,glob
import shutil
import re

a = input("기존의 스케쥴을 정리하시겠습니까? Y/N")
a = a.lower()
if a =='y':
    for file in glob.glob("*_*"):
        a = re.compile(".py$")
        if a.search(file):
            continue
        shutil.move(file,'Past/')

daystring = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
today = datetime.date.today()
b = input("새로운 주간 일정 파일을 생성하시겠습니까? Y/N")
b = b.lower()
if b =='y':
    if today.weekday() == 0:
        for i in range(0,7):
            td = datetime.timedelta(days=i) # 일주일 저장
            targetday = today+td
            schedule_file = open(targetday.strftime("%Y_%m_%d"), "w", encoding="utf8")
            print(" - "+ targetday.strftime("%Y년 %m월 %d일 ") + daystring[targetday.weekday()] + " 일정 - ", file=schedule_file)
            print(" - 일간일정 - ", file=schedule_file)
            print("1. ", file=schedule_file)
            print("2. ", file=schedule_file)
            print("3. ", file=schedule_file)
            print("4. ", file=schedule_file)
            print("5. ", file=schedule_file)

            print(" - 주간일정 - ", file=schedule_file)
            print("1. 파이썬 웹 스크롤링 강의 마무리하기", file=schedule_file)
            print("2. ", file=schedule_file)
            print("3. ", file=schedule_file)
            print("4. ", file=schedule_file)
            print("5. ", file=schedule_file)
            print(" - 연간일정 - ", file=schedule_file)
            print("1. ", file=schedule_file)
            print("2. ", file=schedule_file)
            print("3. ", file=schedule_file)
            print("4. ", file=schedule_file)
            print("5. ", file=schedule_file)
    else:
        print("오늘은 월요일이 아닙니다.")