'07-07globalvar.py'
'함수 내부에서 대입이 없는 변수는 전역 변수로 인식'

def addone():
    ''' 대입이 없는 변수가 참조되면 전역 변수로 인식 '''
    print('\t 전역 변수 i 읽기, i + 1: ', i + 1)

i = 20 # 전역 변수
print('i = ', i)
addone() # 함수 호출
print('i = ', i)
