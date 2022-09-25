'9장도전!프로그래밍04'
'다음 오각형 그림을 참고로 360도 회전하면서 오각형 60개를 그려 다음 결과와 같이 출력되는 프로그램을 작성하시오.'
'오른쪽 그림은 오각형을 90도의 방향으로 바꾸면서 4개 그린 그림'
'오각형 60개를 그린 최종 결과'

import turtle as t

def drawpentagon():
    for i in range(5):
        t.forward(100)
        t.left(360/5)
    
t.setup(500, 500) # 초기 원도의 크기 조정
t.speed(0) # 1에서 10까지 거북이 속도 증가, 0이면 최고속

# 한 변의 길이가 100인 오각형 그리기
for i in range(60):
    drawpentagon() # 함수 호출
    t.left(6)
