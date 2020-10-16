import os 
from tkinter import *
from tkinter import filedialog # file dialog의 경우 sub 모듈이기때문에 all 로 import가 안됨.
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from PIL import Image
root = Tk()
root.title("Taewoo Gui")

file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)
#########################
########functions########
#########################
#선택
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
    filetypes=(("PNG 파일", "*.png"), ("JPG 파일", ".jpg"), ("모든 파일", "*.*")), \
    initialdir=r"D:\PythonWorkSpace\Utilize\GUI_Programing\16_project\images\forcombine") #최초의 경로 row string 경로 처리시에 \\을 써야하나, r을 사용하면 탈출문자와 상관없이 그대로 사용가능 
    for file in files:
        list_file.insert(END, file)
#선택삭제
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

#저장 경로(폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "": # 사용자가 취소를 누를 때
        return
    txt_dest_path.delete(0, END) 
    txt_dest_path.insert(0, folder_selected)

def merge_image():
    images = [Image.open(x) for x in list_file.get(0, END)]#파일 목록 가지고오기
    #size[0] : width, size[1] : height
    # widths = [x.size[0] for x in images]
    # heights = [x.size[1] for x in images]
    widths, heights = zip(*(x.size for x in images))
    print("width : ", widths)
    print("height : ", heights)
    max_width, total_height = max(widths), sum(heights)
    # print("max width : ", max_width)
    # print("total height : ", total_height)
    result_img = Image.new("RGB", (max_width, total_height), (255,255,255)) #배경 흰색
    y_offset = 0 # y 위치
    
    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

        progress = (idx + 1 )/ len(images) *100
        p_var.set(progress)
        progress_bar.update()
    # for img in images:
    #     result_img.paste(img, (0, y_offset))
    #     y_offset += img.size[1]

    dest_path = os.path.join(txt_dest_path.get(),"nado_photo.jpg")
    result_img.save(dest_path)
    msgbox.showinfo("알림", "작업이 완료되었습니다.")


    
def start():
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())
    #파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고","이미지 파일을 추가하세요")
        return
    #저장 경로 확인
    if len(txt_dest_path.get())==0:
        msgbox.showwarning("경고", "저장경로를 선택하세요")
    merge_image()





#파일 프레임 (파일 추가, 삭제)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")
btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

#리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height = 15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)

scrollbar.config(command=list_file.yview)

#저장경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame) # 만약 여기서 텍스트 위젯을 이용했다면 기존 경로를 지울 때 "1.0", END를 이용했어야함 
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5) # 높이변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, padx=5, pady=5, command=browse_dest_path)
btn_dest_path.pack(side="right")

#옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)
#가로넓이옵션
#가로넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width =8 , padx=5, pady=5)
lbl_width.pack(side="left")
#가로 넓이 콤보
opt_width = ["원본유지","1024","800","640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left")

#간격옵션
lbl_space = Label(frame_option, text="간격", width =8 , padx=5, pady=5)
lbl_space.pack(side="left")
#간격 콤보
opt_space = ["없음","좁게","보통","넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left")

#파일포맷옵션
lbl_format = Label(frame_option, text="포맷", width =8 , padx=5, pady=5)
lbl_format.pack(side="left")
#포맷 콤보
opt_format = ["PNG","JPG","BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left")

#진행 상황
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var= DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

#실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text = "닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)
btn_start = Button(frame_run, padx=5, pady=5, text = "시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False,False) 
root.mainloop()
