from tkinter import *

root = Tk()
root.title("Taewoo Gui")
root.geometry("640x480")
label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="Utilize/GUI_Programing/image.png")
label2 = Label(root, image=photo)
label2.pack()
def change():
    label1.config(text="또 만나요")
    global photo2
    photo2 = PhotoImage(file="Utilize/GUI_Programing/image2.png" )
    label2.config(image=photo2)
#Garbage Collection이라는 기능에의해 전역변수로 지정이되지않으면 삭제됨. 따라서 전역변수로 선언해야함.
btn = Button(root, text="클릭", command=change)
btn.pack()
root.mainloop()
