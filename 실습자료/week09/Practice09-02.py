'9장도전!프로그래밍02'
'모듈 math의 factorial() 함수와 모듈 statistics의 median(), mean(), variance(), stdev() 함수를 사용해 다음과 같이 출력하는 프로그램을 작성하시오.'
'모듈로 다시 활용될 수 있도록 다음 조건 블록에 코딩'
"if __name__ == '__main__':"
'다음 리스트 자료의 중앙 값, 평균, 분산, 표준편차를 출력'
'st = [80, 99, 77, 65, 92, 74, 82]'

from math import factorial
from statistics import median, mean, variance, stdev

st = [80, 99, 77, 65, 92, 74, 82]

if __name__ == '__main__':
    print(' 1! =  {}'.format(factorial(1)))
    print(' 6! =  {}'.format(factorial(6)))
    print('11! =  {}'.format(factorial(11)))
    print('16! =  {}'.format(factorial(16)))
    print()
    print(st)
    print('중앙 값: %.2f' % median(st))
    print('평균: %.2f' % mean(st))
    print('분산: %.2f' % variance(st))
    print('표준편차: %.2f' % stdev(st))


    

