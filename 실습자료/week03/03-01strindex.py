Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str = 'Hello python!'
>>> n = len(str)
>>> print('문자열', str, '길이', n)
문자열 Hello python! 길이 13
>>> print('첫 문자', str[0], str[-n])
첫 문자 H H
>>> print('가운데 문자', str[n//2], str[-n//2])
가운데 문자 p p
>>> print('마지막 문자', str[n-1], str[-1])
마지막 문자 ! !
>>> 