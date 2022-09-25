'9장도전!프로그래밍05'
'터틀 윈도 크기를 800, 500으로 지정해 다음과 같이 임의 크기 원20개를 임의 위치에 그리는 프로그램을 작성하시오.'
'다음 변수를 사용해 터틀의 색과 모양을 순서대로 변경하고 다른 색으로 터틀 모양 이름 한글도 출력'
"tshs = ['arrow', 'circle', 'turtle', 'square', 'triangle', 'classic']"
"han = ['화살', '원', '거북이', '사각형', '삼각형', '전통']"
"cols = ['red', 'blue', 'green', 'purple', 'magenta', 'black', 'gray', 'yellow', 'cyan', 'orange', 'aqua']"
'원의 반지름은 3에서 50 사이의 난수로 결정'
'좌표 x, y는 다음 사용'
'x = randint(-300, 300)'
'y = randint(-200, 200)'

from random import randint
import turtle as t

def crandom():
    r = randint(3, 50)
    x = randint(-300, 300)
    y = randint(-200, 200)
    t.pu() # 이동에 선이 그려지지 않도록
    t.goto(x, y) # 이동
    t.pd() # 이동에 선이 그려지도록
    t.fillcolor(cols[i % len(cols)]) # 내부 칠할 색 지정
    t.shape(tshs[i % len(tshs)]) # 모양 지정
    t.begin_fill() # 칠하기 시작
    t.circle(r) # 원 그리기
    t.write(han [i % len(han)])
    t.end_fill() # 칠하기 종료

tshs = ['arrow', 'circle', 'turtle', 'square', 'triangle', 'classic']
han = ['화살', '원', '거북이', '사각형', '삼각형', '전통']
cols = ['red', 'blue', 'green', 'purple', 'magenta', 'black',
         'gray', 'yellow', 'cyan', 'orange', 'aqua']

t.setup(800, 500)
t.speed(10) # 1에서 10까지 거북이 속도 증가, 0이면 최고속
for i in range(20):
    crandom() # 함수 호출
