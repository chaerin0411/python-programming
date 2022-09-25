'10장도전!프로그래밍06'
'다음을 참고해 마우스를 누른 체 이동하면 붉은색의 작은 원이 계속 그려지는 pygame 프로그램을 작성하시오.'
'마우스를 누른 채 이동하는 위치를 리스트 mpos에 모두 저장'
''' 변수 mdown은 마우스를 누른 채 이동하는 동안 True인 변수이며,
    메인 루프의 이벤트 처리 부분에서 다음 코드를 활용
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mdown = True
    elif event.type == pygame.MOUSEMOTION:
        if mdown:
            mpos.append(event.pos)
    elif event.type == pygame.MOUSEBUTTONUP:
        mdown = False '''
''' 리스트 mpos의 모든 원소에 대해 원을 그림
pygame.draw.circle(screen, RED, [x, y], 2) '''

import pygame

pygame.init() # 초기화

RED = [255, 0, 0]
WHITE = [255, 255, 255]
SIZE = [500, 500] # 윈도 크기

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('마우스로 그림 그리')

# 위치 좌표 리스트
mpos = []

# 화면 수정에 사용될 시계 저장
clock = pygame.time.Clock()

# 메인 루프
done = False
mdown = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mdown = True
        elif event.type == pygame.MOUSEMOTION:
            if mdown:
                mpos.append(event.pos) # 리스트에 추가
        elif event.type == pygame.MOUSEBUTTONUP:
            mdown = False

    # 배경색을 흰색으로
    screen.fill(WHITE)
    
    for pos in mpos:
        # 그리기
        pygame.draw.circle(screen, RED, pos, 5)
    
    pygame.display.update()
    # 초당 수정될 프레임 수 지정, 초당 20 프레임 화면이 수정됨
    clock.tick(20)

pygame.quit()
