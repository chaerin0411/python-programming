'Practice06-04'
'이 단원의 프로젝트 Lab에서 코딩한 가위바위보 게임을 다음과 같이 수정해 프로그램을 작성하시오.'
'게임의 회수는 20으로 하고 매번 승자의 승리 회수 또는 비긴 회수가 출력'
'마지막에는 다음과 같이 비긴 회수와 각각의 승률이 출력'

from random import choice
# 한글의 format 출력 문제로 '보'를 '보오'로
dcs = {'가위': '보오', '바위': '가위', '보오': '바위'}
# 출력에 필요한 단어를 구성해 리스트로 생성
tit = ['비김', '철수', '영희', '승자']
# rock scissors paper
rsp = ('가위', '바위', '보오')

# 승리 횟수를 저장
cnt = {tit[0]: 0, tit[1]: 0, tit[2]: 0}

# 제목 출력
print('*'* 20)
print('{:4} {:4} {:^5}'.format(tit[1], tit[2], tit[3]))
print('*'* 20)

# 총 게임 횟수
number = 20
for _ in range(number):
    # 철수의 결정
    cs = choice(rsp)
    # 영희 결정
    yh = choice(rsp)

    # 철수와 영희의 결정 출력
    print('{:4} {:4}'.format(cs, yh), end = ' ')

    # 비기는 조건
    if cs == yh:
        index = 0 #  비김 출력
    # 철수가 이기는 조건
    elif dcs[cs] == yh:
        index = 1 # 철수 출력
    # 영희가 이기는 조건
    else:
        index = 2 # 영희 출력
    cnt[tit[index]] += 1
    # 게임 결과 출력
    print('{:3}{}'.format(tit[index], cnt[tit[index]]))
print()
print('총 게임 회수: %d  비긴 회수: %d' % (number, cnt[tit[0]]))

vgame = cnt[tit[1]] + cnt[tit[2]]
print('철수 승률: {:.2f}'.format(cnt[tit[1]]/vgame))
print('영희 승률: {:.2f}'.format(cnt[tit[2]]/vgame))                          
