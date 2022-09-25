Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str = '일요일 기러기'
>>> print(str[:3], str[4:])
일요일 기러기
>>> print(str[:-4], str[-3:]) #음수 이용
일요일 기러기
>>> print(str[:], str[::], str[::1]) # 모든 문자열 참조
일요일 기러기 일요일 기러기 일요일 기러기
>>> print(str[::2]) # 한 문자씩 건너뛰기
일일기기
>>> print(str[::3]) # 두 문자씩 건너뛰기
일 기
>>> print(str[::-2]) # 역순으로 한 문자씩 건너뛰기
기기일일
>>> print(str[::-1]) # 역순으로 출력
기러기 일요일
>>> 