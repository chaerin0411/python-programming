'Practice06-02'
''' 다음 회사 6개의 주식 가격을 딕셔너리로 만든 후
다음과 같이 표준 입력으로 검색해 가격을 출력하는 프로그램을 작성하시오. '''
'검색을 계속하면서, 주식 이름이 없으면 종료'

stocks = {'삼성에스디에스': 242000, '삼성전자': 47000, '엔씨소프트': 52600, '핸디소프트': 5120, '골프존': 215000, '기아': 56300}
print(stocks)
print()
while True:
    which = input("주식 이름 ? ")
    if which in stocks:
        print('{}: {}'.format(which, stocks[which]))
    else:
        print('주식 이름이 없습니다.')
        break
    print()
