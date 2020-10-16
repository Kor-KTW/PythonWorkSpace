from tkinter import *

root = Tk()
root.title("Taewoo Gui")
root.geometry("640x480")

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")
# # btn1.pack(side="left")
# # btn2.pack(side="left")
# btn1.grid(row=0,column=0)
# btn2.grid(row=1,column=1)
# sticky -> grid에 할당된 영역만큼 늘리는 것. 방향을 지정할 수 있음.
# padx, y -> 간격 설정, button 에서는 글자와 테두리, grid에서는 grid와 grid사이의 간격.  
# cntrl f누르고 왼쪽에 >표시 누르면 replace 기능을 이용할 수 있음.
# width와 height를 이용하면 padx, y 와는 다르게 모두 동일한 크기를 갖게할 수 있음.

btn_f16 = Button(root, text="F16", width=5, height=2 )
btn_f17 = Button(root, text="F17", width=5, height=2 )
btn_f18 = Button(root, text="F18", width=5, height=2 )
btn_f19 = Button(root, text="F19", width=5, height=2 )

btn_f16.grid(row=0,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0,column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_clear = Button(root, text="clear", width=5, height=2 )
btn_equal = Button(root, text="=", width=5, height=2 )
btn_div = Button(root, text="/", width=5, height=2 )
btn_mul = Button(root, text="*", width=5, height=2 )

btn_clear.grid(row=1,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1,column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_7 = Button(root, text="7", width=5, height=2 )
btn_8 = Button(root, text="8", width=5, height=2 )
btn_9 = Button(root, text="9", width=5, height=2 )
btn_sub = Button(root, text="-", width=5, height=2 )

btn_7.grid(row=2,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2,column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_4 = Button(root, text="4", width=5, height=2 )
btn_5 = Button(root, text="5", width=5, height=2 )
btn_6 = Button(root, text="6", width=5, height=2 )
btn_add = Button(root, text="+", width=5, height=2 )

btn_4.grid(row=3,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3,column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_1 = Button(root, text="1", width=5, height=2 )
btn_2 = Button(root, text="2", width=5, height=2 )
btn_3 = Button(root, text="3", width=5, height=2 )
btn_enter = Button(root, text="enter", width=5, height=2 )

btn_1.grid(row=4,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4,column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) #현재위치로부터 아래쪽으로 줄을 더함 rowspan

btn_0 = Button(root, text="0", width=5, height=2 )
btn_dot = Button(root, text=".", width=5, height=2 )

btn_0.grid(row=5,column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) #현재위치로부터 오른쪽으로 줄을 더함 columnspan
btn_dot.grid(row=5,column=2, sticky=N+E+W+S, padx=3, pady=3)


root.mainloop()