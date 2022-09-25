'Practice05-08(도전! 프로그래밍05-08)'
''' 1에서 99까지의 난수 10개로 리스트를 만든 후 다시 이 리스트를 튜플로 변환하고,
다음과 같이 정렬된 리스트와 합, 항목 수, 최대, 최소, 평균을 출력하는 프로그램을 작성하시오. '''
'함수 tuple(리스트)은 리스트를 튜플로 반환'
'함수 sorted(튜플)은 튜플의 항목을 정렬해 다시 리스트로 반환'
'함수 min(튜플)은 튜플에서 최소인 항목을 반환'
'함수 max(튜플), sum(튜플) 등도 사용'
from random import randint

# 리스트 생성
lst = []
for _ in range(10):
    lst.append(randint(1, 99))
print('리스트: ', lst)

# 함수 tuple(), sorted
tup = tuple(lst)
print('튜플: ', tup)
print('튜플 정렬된 리스트: ', sorted(tup))
print()

# 함수 sum, len, max, min
print('합: %d, 항목수: %d' % (sum(tup), len(tup)))
print('최대: %d, 최소: %d, 평균: %.2f' % (max(tup), min(tup), sum(tup)/len(tup)))      
