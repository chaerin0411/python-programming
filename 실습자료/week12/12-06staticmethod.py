'12-06staticmethod.py'
'정적 메소드로 섭씨와 화씨 간의 온도 변환'

''' 데커레이터(decorator)
정적 메소드는 메소드 헤드 문장 위에 @staticmethod를 기술
정적 메소드는 객체 뿐 아니라 클래스에서도 직접 접근
인자는 첫 번째 인자로 self 없이 실제로 필요한 인자를 기술 '''

class Degree:
    @staticmethod
    def tofahrenhite(celsius):
        return celsius * 1.8 + 32

    @staticmethod
    def tocelcius(fahrenhite):
        return (fahrenhite - 32) / 1.8

print('%.2f' % Degree.tofahrenhite(30))
print('%.2f' % Degree.tocelcius(100))

d = Degree()
print('%.2f' % Degree.tofahrenhite(35))
print('%.2f' % Degree.tocelcius(90))
