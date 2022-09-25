# os.path.basename 사용
import os
# tkinter 라이브러리 사용
from tkinter import *
# pillow는 이미지 편집을 위한 라이브러리사용
from PIL import Image, ImageTk, ImageFilter
# 파일 열기, 다른 이름으로 저장, 메시지 박스 등 대화상자 사용
from tkinter import filedialog, messagebox
# 색상 다이얼로그 사용
from tkinter.colorchooser import *

root = None
canvas = None
# 이미지 파일 불러올 변수
im = None
tk_img = None
# 작업 중인 파일 이름을 저장
file_path = None
# 마우스 좌표를 위한 변수
x1, y1 = None, None
# Canvas에 그릴 선의 굵기를 위한 변수
wp = 5
# Canvas에 그릴 선의 색상
result = '#6B66FF'

# 파일 메뉴 함수
# 파일 메뉴에서 "새로운 파일"을 선택했을 때 호출되는 함수
def file_new():
    print("New File!")

# 파일 메뉴에서 "열기"를 선택했을 때 호출되는 함수
def file_open():
    print("Open File!")
    global im, tk_img
    fname = filedialog.askopenfilename()
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    root.update()

# 파일 메뉴에서 "저장"을 선택했을 때 호출되는 함수
def file_save():
    print("Save File!")
    filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("PPTX files", "*.pptx"), ("all files", "*.*")))
    

# 파일 메뉴에서 "다른 이름으로 저장"을 선택했을 때 호출되는 함수
def file_save_as():
    print("Save as File!")
    return result

# 파일 메뉴에서 "종료"를 선택했을 때 호출되는 함수    
def file_quit():
    print("Quit File!")
    root.destroy() # sys.exit(0)

# 파일 메뉴에서 "자르기"를 선택했을 때 호출되는 함수
def edit_cut():
    print("Cut File!")
    event_generate("<<Cut>>")

# 파일 메뉴에서 "복사"를 선택했을 때 호출되는 함수    
def edit_copy():
    print("Copy File!")
    event_generate("<<Copy>>")

# 파일 메뉴에서 "붙여넣기"를 선택했을 때 호출되는 함수    
def edit_paste():
    print("Past File!")
    event_generate("<<Paste>>")

# 파일 메뉴에서 "도움말"을 선택했을 때 호출되는 함수
def help_showabout():
    print("TkInter 편집기 버전 0.1")
    messagebox.showinfo('TkInter 편집기', 'TkInter 편집기 버전 0.1')

# Mouse Move에 대한 함수 정의, Mouse의 좌표를 통해 canvas에 선을 생성함
def mouseMove(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
    canvas.create_line(x1, y1, x1+1, y1+1, width=wp, fill=result)

# Mouse Scroll에 대한 함수 정의, 선의 굵기를 설정하고, Label에 굵기 문구 업데이트
def mouseScroll(event):
    global wp
    if event.delta==120:
        wp+=1
    if event.delta==-120:
        wp-=1
        if wp<1:
            wp = 1
    textSize.config(text= '굵기 : ' + str(wp))

# Canvas를 Clear 하는 함수 정의
def clearCanvas():
    canvas.delete("all")

# 색상을 선택하는 색상 다이얼로그 함수 정의
def callback() :
    global result
    result = askcolor(title = "Colour Chooser")
    result = result[1]

# 삼각형을 그리는 함수
def paintTriangle(event):
        global x1, y1
        x1 = event.x
        x2 = event.y
        canvas.create_polygon(x1, y1, x1, y1+140, x1+140, y1+60, fill=result) # (x1,y1), (x2,y2), (x3,y3)을 꼭지점으로 하는 삼각형 

# 사각형을 그리는 함수
def paintRect(event):
        global x1, y1
        x1 = event.x
        x2 = event.y
        canvas.create_rectangle(x1-10, y1-10, x1+100, y1+100, fill=result)

# 원을 그리는 함수
def paintOval(event):
        global x1, y1
        x1 = event.x
        x2 = event.y
        canvas.create_oval(x1-10, y1-10, x1+100, y1+100, fill=result)

def triangle():
        callback()
        canvas.bind("<Double-Button-1>", paintTriangle)

def rectangle():
        callback()
        canvas.bind("<Double-Button-1>", paintRect)

def oval():
        callback()
        canvas.bind("<Double-Button-1>", paintOval)
        
# tkinter 생성       
root = Tk()

# 메뉴의 최상위인 메뉴바 생성
menubar = Menu(root)

# 메뉴 아이템 File
filemenu = Menu(menubar, tearoff=0) # tearoff = 0 윈도에 분리되지 않도록 설정
filemenu.add_command(label="New", command=file_new)
filemenu.add_command(label="Open", command=file_open)
filemenu.add_command(label="Save", command=file_save)
filemenu.add_command(label="Save As...", command=file_save_as)
filemenu.add_separator() # 중간 구분자 추가
filemenu.add_command(label="Exit", command=file_quit)
# 메뉴바에 File을 추가
menubar.add_cascade(label="File", menu=filemenu)

# 메뉴 아이템 Edit
editmenu = Menu(menubar, tearoff=0) # tearoff = 0 윈도에 분리되지 않도록 설정
editmenu.add_command(label="Cut", command=edit_cut)
editmenu.add_command(label="Copy", command=edit_copy)
editmenu.add_command(label="Paste", command=edit_paste)
# 메뉴바에 Edit를 추가
menubar.add_cascade(label="Edit", menu=editmenu)

# 메뉴 아이템 Help
helpmenu = Menu(menubar, tearoff=0) # tearoff = 0 윈도에 분리되지 않도록 설정
helpmenu.add_command(label="TkEditor 편집기", command=help_showabout)
# 메뉴바에 Help를 추가
menubar.add_cascade(label="Help", menu=helpmenu)

# 메뉴 보이기
root.config(menu=menubar)

# 캔버스를 root에 위치시키고, 높이와 너비 설정함
canvas = Canvas(root, height=700,width=700)
# 캔버스에 B1-Motion(왼쪽 버튼에 대한 모션)을 정의한 mouseMove 함수와 bind함
canvas.bind('<B1-Motion>', mouseMove)
# 캔버스에 MouseWheel(마우스 휠)을 정의한 mouseScroll 함수와 bind함
canvas.bind('<MouseWheel>', mouseScroll)
# canvas를 아래쪽에 위치시킴
canvas.pack(side="bottom")

# root의 제목을 설정
root.title("TkInter 그림판")

# 버튼 6개와 라벨을 위치시킬 프레임 생성
frame = Frame(root)
# 프레임은 root에 위치시킴
frame.pack(side="top", fill="both")

# 종료 버튼 생성 및 설정
button = Button(frame, text=" Exit ", fg = "#FF0000", command=root.destroy)
# 종료 버튼을 frame에 위치 시킴
button.grid(row=0, column=0, sticky="w",padx=5)

# canvas를 clear할 버튼 생성 및 설정
clear = Button(frame, text=" Clear ", fg = "#6799FF", command=clearCanvas)
# clear 버튼을 frame에 위치 시킴
clear.grid(row=0, column=2, sticky="w", padx=5)

# 색상 선택 버튼 생성 및 설정
colorBtn = Button(frame, text="     Choose Color    ", fg="#6B66FF", command=callback)
colorBtn.grid(row=1, columnspan=2, sticky="w", padx=5)

# 선의 굵기에 대한 문구를 표시할 라벨 설정
textSize = Label(frame, text = "굵기 : " + str(wp))
# Label을 frame에 위치 시킴
textSize.grid(row=1, column=2, sticky="w", padx=5)

# 삼각형 버튼
triangleBtn = Button(frame, text=" 삼각형 ", fg="#FFC19E", command=triangle)
triangleBtn.grid(row=2, column=0, sticky="w", padx=5)

# 사각형 버튼
rectangleBtn = Button(frame, text=" 사각형 ", fg="#B5B2FF", command=rectangle)
rectangleBtn.grid(row=2, column=1, sticky="w", padx=5)

# 원형 버튼
ovalBtn = Button(frame, text=" 원형 ", fg="#FFB2D9", command=oval)
ovalBtn.grid(row=2, column=2, sticky="w", padx=5)

# 메인 루프 설정
root.mainloop()
