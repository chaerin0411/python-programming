'10장도전!프로그래밍02'
'Tkinter 위젯 버튼 6개를 그리드 위치 이름으로 지정해 다음과 같이 출력하는 Tkinter 프로그램을 작성하시오.'
'버튼의 가로 길이는 30으로 지정'
''' 다음 구문을 사용해 6개 버튼의 모양과 표시되는 이름을 결정
rtype = ['flat', 'groove', 'raised', 'ridge', 'solid', 'sunken']
for i, t in enumerate(rtype): '''

from tkinter import *

rtype = ['flat', 'groove', 'raised', 'ridge', 'solid', 'sunken']

win = Tk()
win.title('그리드에 배치한 버튼의 다양한 모습')


for i, t in enumerate(rtype):
    for r in range(3):
        for c in range(2):
            btni = Button(win, text='({}, {})'.format(r, c), width=30, relief= t) # 버튼
            btni.grid(row=r, column=c)

win.mainloop()
        


