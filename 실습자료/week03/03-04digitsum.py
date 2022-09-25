Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> value = input('실수(세 자리.두 자라로 345.78처럼)를 하나 입력하세요. >> ')
실수(세 자리.두 자라로 345.78처럼)를 하나 입력하세요. >> 345.78
>>> num = value.replace('.', '')
>>> sum = 0
>>> sum += int(num[0])
>>> sum += int(num[1])
>>> sum += int(num[2])
>>> sum += int(num[3])
>>> sum += int(num[4])
>>> print('입력값', value)
입력값 345.78
>>> print('모든 자릿수 합:', sum)
모든 자릿수 합: 27
>>> 