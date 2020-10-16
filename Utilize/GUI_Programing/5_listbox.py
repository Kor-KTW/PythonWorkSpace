from tkinter import *

root = Tk()
root.title("Taewoo Gui")
root.geometry("640x480")

# listbox = Listbox(root, selectmode="single", height=0) #하나만 선택
listbox = Listbox(root, selectmode="extended", height=0) #동시 선택 가능 heitht=0을 선택하면 리스트의 크기만큼 높이가 설정됨.
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()
def btncmd():
    #삭제
#    listbox.delete(END) # 맨뒤에꺼 삭제
#    listbox.delete(0) # 맨앞에꺼 삭제
    #갯수 확인
    print("리스트에는",listbox.size(),"개가 있어요") 
    
    #항목 확인
    print("1~3번째의 항목 : ", listbox.get(0,2))

    #사종자에게 선택된 항목 확인(위치로 반환)
    print("선택된 항목 : ", listbox.curselection())

    

btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()