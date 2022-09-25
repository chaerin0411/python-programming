'9장도전!프로그래밍06'
''' 다음은 MatPlotlib의 함수 plot()으로 sin과 cos 그래프를 그리는 프로그램이다.
다음 내용을 참고하고, 소스의 빈 부분을 완성해 다음과 같이 출력하는 프로그램을 작성하시오. '''
'모듈 numpy의 sin, cos 함수를 사용'
'모듈 numpy의 linspace(from, to, step) 함수는 선형 구간을 지정한 구간의 수만큼 분할한 값으로 구성된 배열(array) 반환'
"Matplotlib.pyplot의 plot() 함수의 키워드 인자 ls는 그래프 선 모양으로 다음 네 가지 중 하나로 지정 가능: '-', '--', '-.', ':'"
'Mathplotlib.pyplot의 grdi()는 바탕의 격자를 그림'
'Mathplotlib.pyplot의 grdi()는 범례를 그림'

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi * 2, np.pi * 2, 720)
cos, sin = np.cos(x), np.sin(x)

plt.plot(x, sin, ls=':', label='sin')
plt.plot(x, cos, ls='--', label='cos')

plt.title("Graph of sin cos")
plt.xlabel('radians')
plt.ylabel('value')
plt.grid()
plt.legend()
plt.show()
