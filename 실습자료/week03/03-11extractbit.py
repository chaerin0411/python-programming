Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = int(input('정수 하나를 입력하세요 >> '))
정수 하나를 입력하세요 >> 195
>>> mask = 0b1111 # 0xf도 가능
>>> print('정수 {0} 2진수로는 {0:b}'.format(a))
정수 195 2진수로는 11000011
>>> print('가장 오른쪽 4비트: {0:04b} 정수로는 {0}'.format(a & mask))
가장 오른쪽 4비트: 0011 정수로는 3
>>> 