'9장도전!프로그래밍01'
'모듈 math와 random을 불러와 random() 함수로 발생한 값을 활용해 다음과 같이 원의 면적을 출력하는 프로그램을 작성하시오.'
'모듈 math의 원주율 pi 사용'
'모듈 random의 함수 random()*10으로 반지름 사용'
'반지름은 내장 함수 round()로 소수점 두 자리 사용'
'함수 getarea(r)로 원의 면적을 반환'

import math
import random as rd

def getarea(r):
    return r*r*math.pi

r = round(rd.random()*10, 2)
print('원의 반지름: %.2f'% r)
print('원주율 pi: %.4f'% math.pi)
print('반지름 %.2f인 원의 면적은 %.2f'% (r, getarea(r)))
