'10-02widgetpack.py'
'레이블과 엔트리, 버튼 위젯으로 윈도 생성'

from tkinter import *

win = Tk()
win.title('여러 위젯 구성')

lb1 = Label(win, text="레이블(Label)") # 레이블
lb1.pack() # 레이블을 윈도에 맞게 적정하게 배치

txt = Entry(win) # 엔트리
txt.insert(0, '엔트리(Entry)')
txt.pack()

btn = Button(win, text="OK") # 버튼
btn.pack()

win.mainloop()
