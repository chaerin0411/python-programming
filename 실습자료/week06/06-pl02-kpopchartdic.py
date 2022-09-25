'06-pl02-kpopchartdic.py'
'딕셔너리로 만드는 K-pop 차트'
''' 가수의 리스트 singer와 이에 대응되는 곡의 리스트인 song을 이해하고,
함수 zip()으로 두 리스트의 항목을 결합한다.
다시 위 결과의 리스트를 값, 순위를 키로 조합하는 딕셔너리 Kpchart를 만든다. '''

# K-pop 가수의 곡을 차트 순위에 맞춰 입력
singer = ['BTS', '볼빨간사춘기', 'BTS', '블랙핑크', '태연', 'BTS']
song = ['작은 것들을 위한 시', '나만 봄', '소우주', 'Kill This Love', '사계']

# zip() 함수로 가수와 곡을 조합
kpop = list(zip(singer, song))
print(kpop)

# dic()와 enumeratezip() 함수로 순위를 키로 가수와 곡을 사전으로 구성
kpchart = dict(enumerate(kpop, start = 1))

# 일반 출력
print(kpchart)
print()

# 모듈 pprint의 pprint() 함수 활용
import pprint
pprint.pprint(kpchart)
