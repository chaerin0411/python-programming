'05-pl01-sportsnumber.py'
'스포츠 종목과 팀원 수를 리스트로 적절히 출력'
''' 리스트 생성과 리스트 컴프리헨션으로 다양한 구조의 리스트를 만든다.
만들어진 리스트에서 for문으로 항목을 적절히 출력하도록 한다.
for문에서 시퀀스로 range(4) 또는 range(2)를 사용할지,
리스트 자체를 사용할지를 선택하도록 한다 '''

sports = ['축구', '야구', '농구', '배구']
# 위 종목에 대응하는 팀원 수를 항목으로 구성
num = [11, 9, 5, 6]
print(sports)
print(num)
# 위 두 리스트로 출력
for i in range(len(sports)):
    print("%s: %d명 " % (sports[i], num[i]), end = ' ')
print(); print()

# 2차원 리스트로 생성
sponum = [sports, num]
print(sponum)
# 2차원 리스트에서 출력
for i in range(len(sponum[0])):
    print("%s: %d명 " % (sponum[0][i], sponum[1][i]), end = ' ')
print(); print()

# 다른 구조의 2차원 리스트 생성을 컴프리헨션으로 처리
psponum = [[sports[i], num[i]] for i in range(len(sports))]
print(psponum)
# 위 리스트에서 출력
for one in psponum:
    print("%s: %d명 " % (one[0], one[1]), end = ' ')
print()
