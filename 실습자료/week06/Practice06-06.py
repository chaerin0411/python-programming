'Practice06-06'
''' 1에서 20까지의 난수 5개를 두 번 얻어 각각 집합인 변수 A, B에 저장한다.
집합 A와 B의 합집합과 교집합, 차집합, 여집합을 구해 출력하는 프로그램을 작성하시오. '''
'모듈 random의 sample() 함수를 사용한 다음 문장을 집합 변수 A에 저장'

from random import randint
from random import sample

A = set(sample(list(range(1, 21)), 5))
B = set(sample(list(range(1, 21)), 5))
print('A = {} '.format(A))
print('B = {} '.format(B))
print()
print('A | B = {} '.format(A | B))
print('A & B = {} '.format(A & B))
print('A - B = {} '.format(A - B))
print('A ^ B = {} '.format(A ^ B))
