' 04-pl01-numguess.py'
' 1에서 10 사이의 수 맞히기'
''' 난수를 1개 생성해 정답으로 저장한 후
표준 입력으로 정답을 맞출 때까지 입력을 반복한다.
사용자가 입력한 값과 정답을 비교해 힌트를 준다.
정답이면 적절한 메시지를 출력하고 종료한다. '''

import random
answer = random.randint(1, 10)

indata = int(input('1에서 10 사이의 수를 맞히세요 >> '))
while True:
    if indata == answer:
        print('축하한다. {}: 정답이다.'.format(indata))
        break;
    elif indata < answer:
        str = '{}보다 더 큰 수로 다시 입력 >> '.format(indata)
    else:
        str = '{}보다 더 작은 수로 다시 입력 >> '.format(indata)
    indata = int(input(str))

print(" 종료 ".center(30, '*'))
