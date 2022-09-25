'9장도전!프로그래밍03'
"터틀 윈도 크기를 500, 500으로 지정한 후 다음과 같이 'yellow', 'red', 'blue'색의 직선을 200개 그려 다음과 같은 태극 문양을 그리는 프로그램을 작성하시오."
"바탕색은 'black' 지정"
'반복은 for i in range(200): 사용'
"선 색은 색상 리스트 ['yellow', 'red', 'blue']로 순으로 지정"
'선 두께는 i/200 + 1로 지정'
'직선을 (i * 2) 길이로 그리기'
'방향을 left(119)로 회전'

import turtle as t        

cols = ['yellow', 'red', 'blue'] # 색상 리스트

t.setup(500, 500) # 초기 원도의 크기 조정
t.speed(0) # 1에서 10까지 거북이 속도 증가, 0이면 최고속

''' 한 변의 길이가 i*2인 삼각형 그리기 '''
for i in range(200):
    t.bgcolor('black')
    t.pencolor(cols[i % len(cols)]) # 펜 색상 지정
    t.pensize(i/200 + 1) # 펜 두께 지정 
    t.forward(i * 2) # 선 그리기
    t.left(119) # 각도 수정
