import os
from tkinter import *

root = Tk()
root.title("제목 없음 - windows 메모장")
root.geometry("640x480")
#대상 파일명
filename = "mynote.txt"
def open_file():
    if os.path.isfile(filename): # 파일이 있으면 true, 없으면 false
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 본문 삭제
            txt.insert(END, file.read()) #본문 입력
    else:
        print("there is no file")
def save_file():
        with open(filename, "w", encoding="utf8") as file:
            file.write(txt.get("1.0", END))

menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_separator()
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit) 
menu.add_cascade(label="파일", menu=menu_file)
root.config(menu=menu)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="도움말")


scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill="y")
txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)

root.mainloop()