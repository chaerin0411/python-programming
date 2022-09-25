'10-02moverectwithkey.py'
'프로젝트 Lab2'
'방향 키로 사각형 이동'
''' 방향 키를 사용해 녹색의 사각형을 이동시키는 pygame 프로그램을 작성해 보자.
pygame에서 키보드를 누를 때 pygame.KEYDOWN이 발생하며,
키보드를 누른 후 뗄 때 pygame.KEYUP이 발생한다. '''
''' 방향 키를 사용해 사각형을 이동시키려면 메인 루프의 이벤트 처리에서 방향 키 누름을 인지해
일정한 거리만큼 이동하도록 좌표를 수정한 후 사각형을 다시 그린다.
누른 방향 키를 떼면 현재 위치에서 사각형을 그린다. 이 작업을 무한 반복한다.
오른쪽 방향 키로는 x의 값을 2 증가시키고, 왼쪽 방향 키로는 x의 값을 2 감소시킨다.
또한 위 방향키로는 y의 값을 2 감소시키고, 아래 방향 키로는 y의 값을 2 증가시킨다.
누른 방향 키를 놓으면 좌표를 증가시키지 않고 현재 위치에서 사각형을 그린다. '''

import pygame
from pygame.locals import QUIT, KEYUP, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# 화면에 사각형을 그리고 초당 화면 프레임 수정
def paint(surface, x, y):
    # 사각형 그리기
    def drawrect(surface, x, y):
        sizeX, sizeY  = 30, 30
        pygame.draw.rect(surface, GREEN, [x, y, sizeX, sizeY])

    surface.fill(WHITE)
    drawrect(surface, x, y)
    pygame.display.update()
    # 초당 화면 수정 프레임 수 지정
    clock.tick(60)

# 시작: 초기화
pygame.init()
surface = pygame.display.set_mode([600, 400])
pygame.display.set_caption("키보드 이벤트 처리")

# 화면 수정 시간에 사용
clock = pygame.time.Clock()

# 방향키에 따른 이동 거리와 첨자 관리
INC = (-2, 0, 2) # 방향 키에 따른 이동 거리
posX = 1 # 위 값 중 하나의 첨자
posY = 1 # 위 값 중 하나의 첨자

# 사각형의 첫 위치
x, y = 10, 10

# 메인 루프
done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        # 키를 누르면
        elif event.type == KEYDOWN:
            key = event.key
            if key == K_LEFT:
                pos = 0
            elif key == K_RIGHT:
                pos = 2
            elif key == K_UP:
                pos = 0
            elif key == K_DOWN:
                pos = 2

        # 키를 올리면(놓으면)
        elif event.type == KEYUP:
            key = event.key
            # 왼쪽 오른쪽 키면, x 증가를 0으로
            if key == K_LEFT or key == K_RIGHT:
                posX = 1
            # 위 아래 키면, y 증가를 0으로
            elif key == K_UP or key == K_DOWN:
                posY = 1

    # 좌표 (x, y)를 수정해 사각형 그리기
    x, y = x + INC[posX], y + INC[posY]
    paint(surface, x, y)

pygame.quit()
