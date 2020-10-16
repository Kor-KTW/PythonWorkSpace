from tkinter import *

root = Tk()
root.title("Taewoo Gui")
root.geometry("640x480")

frame = Frame(root)
frame.pack()
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set)
for i in range(32):
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)
root.mainloop()
