'07-06localvar.py'
'함수 내부에서 대입이 있는 변수는 지역 변수로 인식'

def addone():
    ''' 함수에서 대입에 사용되는 변수는 지역 변수 '''
    i = 30 # 지역 변수 생성
    i += 1 # 지역 변수 수정
    print('\t지역 변수 i:', i) # 지역 변수 참조

i = 20 # 전역 변수
print('i:', i) # 함수 호출
addone() # 함수 호출
print('i:', i) # 전역 변
