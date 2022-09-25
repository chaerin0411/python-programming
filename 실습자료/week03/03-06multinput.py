Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> m, n, x, y = input('4개의 수 입력 >> ').split()
4개의 수 입력 >> 3.7 5.8 9 2.5
>>> a, b, c, d = float(m), float(n), float(x), float(y)
>>> print('입력값: ', a, b, c, d)
입력값:  3.7 5.8 9.0 2.5
>>> sum = a + b + c + d
>>> print('합: ', sum, '평균: ', sum / 4)
합:  21.0 평균:  5.25
>>> print('최대: ', max(a, b, c, d), '최소: ', min(a, b, c, d))
최대:  9.0 최소:  2.5
>>> 