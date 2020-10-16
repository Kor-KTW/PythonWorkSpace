from tkinter import *

root = Tk()
root.title("Taewoo Gui")
btn1 = Button(root, text = "버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼22222222222222222222222")
btn2.pack()
# Padx,y = 여백, width, height=높이 넓이 자체.
btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼444444444444444")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()
photo = PhotoImage(file="Utilize/GUI_Programing/image.png")
btn6 = Button(root, image=photo)
btn6.pack()
def btcmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btcmd)
btn7.pack()

root.mainloop()
