'08-04-incometax.py'
'Mini Project 4 : 종합 소득 세금 출력'
''' 마지막으로 표준 입력으로 받은 종합 소득 금액으로 세금을 계산해 출력하는 코드를 작성하자.
    과세 표준 구간의 세율과 누진 공제액이 쌓인 항목으로 리스트를 구성한다. '''
' 리스트와 튜플, 산술연산, if 조건, 표준 입력과 출력 활용 '
''' 세율과 누진 공제액 쌓인 항목의 리스트
    taxrate = [(6, 0), (15, 1_1080_000), (24, 5_220_000), (35, 14_900_000),
    (38, 19_400_000), (40, 25_400_000), (42, 35_400_000)] 
    종합 소득 과세 표준 구간에 따른 기준 종합 소득
    base = (0, 12_000000, 46_000000, 88_000000, 150_000000, 300_000000, 500_000000) '''

# 세율과 누진 공제액 쌓인 항목의 리스트
taxrate = [(6, 0), (15, 1_080_000), (24, 5_220_000), (35, 14_900_000),
    (38, 19_400_000), (40, 25_400_000), (42, 35_400_000)]

# 종합 소득 과세 표준 구간에 따른 기준 종합 소득
base = (0, 12_000000, 46_000000, 88_000000, 150_000000, 300_000000, 500_000000)

def getsection(income):
    '''
    종합 소득 금액 income에 따른 과세 표준 구간 번호를 반환
    인지 income: 종합 소득 금액
    '''
    if base[6] < income:
        section = 6
    elif base[5] < income:
        section = 5
    elif base[4] < income:
        section = 4
    elif base[3] < income:
        section = 3
    elif base[2] < income:
        section = 2
    elif base[1] < income:
        section = 1
    else:
        section = 0
    return section

income = int(input('종합 소득 금액 입력 >> '))
section = getsection(income)
tax = income * taxrate[section][0] / 100 - taxrate[section][1]

print("종합 소득: {:,.0f}".format(income))
print("세율: {}%".format(taxrate[section][0]))
print("세금: {:,.0f}".format(tax))
    
