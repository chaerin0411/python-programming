'Practice05-01(도전! 프로그래밍05-01)'
''' 1에서 99까지의 난수 10개로 리스트를 만든 후
리스트와 정렬된 리스트 그리고 내림차순으로 정렬된
역순 리스트를 출력하는 프로그램을 작성하시오. '''

from random import randint # from 모듈 import 변수
lst = []
for _ in range(9):
    lst.append(randint(1, 99))
    
print('리스트', lst)
print('정렬 리스트', sorted(lst))
print('역순 리스트', sorted(lst, reverse=True))

