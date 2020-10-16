#pop-up
import tkinter.ttk  as ttk 
from tkinter import *

root = Tk()
root.title("Taewoo Gui")
root.geometry("640x480")

values =[str(i)+ "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정, 뿐만아니라 버튼 클릭을 통한 값설정도 가능.

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="read-only")
readonly_combobox.current(0) #0번째 값을 기본값으로.
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()
