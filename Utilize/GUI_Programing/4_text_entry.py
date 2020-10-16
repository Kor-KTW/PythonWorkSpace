from tkinter import *

root = Tk()
root.title("Taewoo Gui")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()
#text widget 생성
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # 한줄만 받을 수 있음.
e.insert(END, "한줄만 입력해요")
e.pack()
def btncmd():
    #내용 출력
    print(txt.get("1.0",END))#1=line, 0= column, END = END4
    print(e.get())
    #내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)
btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()