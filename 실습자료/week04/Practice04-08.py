''' 난수로 발생시킨 1에서 100 사이의 첫 번째 피연산자와
사용자가 표준 입력한 산술 연산자 문자 그리고 표준 입력한
두 번째 피연산자를 계산해 출력하는 프로그램을 작성하시오.
반복 while True:로 계속 산술 연산 결과를 출력
산술 연산 종류인 연산자는 표준 입력으로 ‘+-*/%’ 중 하나를 입력
입력한 연산자가 위 연산자가 아니면 반복을 종료하고 프로그램을 마침) '''

import random
before = random.randint(1, 100)
print('첫 값은 {} 입니다.'.format(before))

while True:
    print()
    op = input('산술 연산의 종류를 입력하세요. >> ')
    if op not in '+-*/%':
        break
    else:
        oprd = int(input('두 번째 피연산자를 입력하세요. >> '))
        if op == '+':
            after = before + oprd
        elif op == '-':
            after = before - oprd
        elif op == '*':
            after = before * oprd
        elif op == '/':
            after = before / oprd  
        elif op == '%':
            after = before % oprd
        print('{} {} {} =  {}'.format(before, op, oprd, after))

print(' 종료 '.center(32, '*'))
    


