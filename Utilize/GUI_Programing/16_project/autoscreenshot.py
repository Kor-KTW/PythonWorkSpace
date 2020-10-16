import time
from PIL import ImageGrab

time.sleep(5) # 5 초 대기

for i in range(1,11):
    img = ImageGrab.grab() # 스크린 이미지 가져옴
    img.save(r"D:\PythonWorkSpace\Utilize\GUI_Programing\16_project\images\forcombine\image{}.png".format(i)) # 파일로 저장
    time.sleep(2) # 2초 단위