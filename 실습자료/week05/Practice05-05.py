'Practice05-05(도전! 프로그래밍05-05)'
''' 다음 리스트 sports와 num을 활용해 스포츠 종목과 팀원 수가 번갈아 나오는
리스트를 만든 후 다음과 같이 출력하는 프로그램을 작성하시오.
sports = ['축구', '야구', '농구', '배구']
num = [11, 9, 5, 6] '''
'리스트 sports에 insert() 메소드로 직접 팀원 수를 삽입'
'리스트 sports의 홀수 참조에 빈 문자 ''을 insert() 메소드로 삽입'
'위 결과 리스트에서 슬라이스 sports[1::2]에 num을 대입'

# 리스트 sports에 insert() 메소드로 직접 팀원 수를 삽입
sports = ['축구', '야구', '농구', '배구']
sports.insert(1, 11)
sports.insert(3, 9)
sports.insert(5, 5)
sports.insert(7, 6)
print('메소드 insert()로 팀원 수 삽입')
print(sports); print()

# 리스트 sports의 홀수 참조에 빈 문자 ''을 insert()메소드로 삽입
sports = ['축구', '야구', '농구', '배구']
for i in range(1, len(sports)*2, 2):
    sports.insert(i, '')
print('메소드 insert()로 \'\' 삽입')
print(sports); print()

# 위 결과 리스트에서 슬라이스 sports[1::2]에 num을 대입
num = [11, 9, 5, 6]
sports[1::2] = num
print('슬라이스 sports[1::2]에 num을 대입')
print(sports); print()
