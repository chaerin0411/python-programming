Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # 두 실수의 사칙연산과 표준 입력 연산식의 계산
>>> num1 = float(input('첫 번째 수 입력 >> '))
첫 번째 수 입력 >> 10.0
>>> num2 = float(input('두 번째 수 입력 >> '))
두 번째 수 입력 >> 2.5
>>> print('합:', num1 + num2)
합: 12.5
>>> print('차:', num1 - num2)
차: 7.5
>>> print('곱하기:', num1 * num2)
곱하기: 25.0
>>> print('나누기:', num1 / num2)
나누기: 4.0
>>> expression = input('연산식 입력(예 3.2 + 4 * 1.5) >> ')
연산식 입력(예 3.2 + 4 * 1.5) >> 30 // 4
>>> print('연산식:', expression, '결과:', eval(expression))
연산식: 30 // 4 결과: 7
>>> 