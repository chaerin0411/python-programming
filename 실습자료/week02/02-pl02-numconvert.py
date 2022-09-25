Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 진수와 그에 맞는 정수를 입력받아 2진수, 8진수, 16진수 출력
>>> base = int(input('입력할 정수의 진수(base)는? '))
입력할 정수의 진수(base)는? 16
>>> invar = input(str(base) + '진수 정수 입력 >> ')
16진수 정수 입력 >> 1f
>>> data = int(invar, base) # 입력 문자열을 base 진수로 변환
>>> # 여러 진수로 출력
>>> print('2진수:', bin(data))
2진수: 0b11111
>>> print('8진수:', oct(data))
8진수: 0o37
>>> print('16진수:', hex(data))
16진수: 0x1f
>>> 