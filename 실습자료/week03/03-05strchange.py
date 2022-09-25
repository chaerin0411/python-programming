Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str = input('2개의 단어를 빈 공간으로 구분해 입력하세요. >> ')
2개의 단어를 빈 공간으로 구분해 입력하세요. >> 사과 복숭아
>>> pos = str.find(' ')
>>> preWord = str[:pos]
>>> postWord = str[pos+1:]
>>> print(preWord, postWord)
사과 복숭아
>>> print(preWord[::-1], postWord[::-1])
과사 아숭복
>>> 