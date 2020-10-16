#pop-up
from tkinter import *

root = Tk()
root.title("Taewoo Gui")
root.geometry("640x480")

chkvar = IntVar() # chkvar에 int형으로 값을 저장한다.

chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.pack()
# chkbox.select() #자동 선택 처리
# chkbox.deselect() #자동 해제 처리

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())  #0 : 체크 해제, 1: 체크
    print(chkvar2.get())  #0 : 체크 해제, 1: 체크
    

btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()