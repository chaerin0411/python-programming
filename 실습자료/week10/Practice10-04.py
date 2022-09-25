'10장도전!프로그래밍04'
"Tkinter 윈도 전체에 표시된 버튼 '인사 이벤트 처리'를 누르면 Tkinter의 이벤트 처리 방식 두 가지가 모두 실행되도록 구현한다."
'즉, 버튼을 누르면 두 가지 이벤트 처리에 대한 결과가 텍스트 모드로 출력되는 프로그램을 작성하시오.'
''' 버튼을 누르면 첫 줄은 메소드 bind()로 연결한 핸들러에서 출력하고, 두 번째 줄은 인자 command에 연결한 핸들러에서 출력'
bind: 안녕!
command: 안녕! '''
''' 버튼 btn은 다음으로 배치해 윈도 전체에 표시
btn.pack(expand=True, fill='both') '''

from tkinter import *

def click1(e):
    print('bind: 안녕!')

def click2():
    print('command: 안녕!')
    
win = Tk()
win.title('반가워요, Tkinter!')
win.geometry('300x200')

btn = Button(win, text='인사 이벤트 처리', command=click2)
btn.bind("<Button-1>", click1)
btn.pack(expand=True, fill='both')

win.mainloop()



