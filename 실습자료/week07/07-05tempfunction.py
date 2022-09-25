'07-05tempfunction.py'
'섭씨 온도와 화씨 온도 간의 변환 함수'

def ctofahrenhite(cels):
    """ 인자인 섭씨 온도 cels을 화씨 온도로 변환해 반환 """
    return cels * 9/5 + 32

def ftocelsius(fahr):
    return (fahr - 32 ) * 5/9

for cels in range(28, 35, 2):
    print('섭씨: {}, 화씨: {:.2f}'.format(cels, ctofahrenhite(cels)))

for fahr in range(90, 103, 3):
    print('섭씨: {:.2f}, 화씨: {}'.format(ftocelsius(fahr), fahr))
