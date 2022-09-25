'12-11diamondinheritance.py'
'다이어몬도 상속에서의 메소드 호출'

class Person():
    def do(self):
        print('사람은 무언가 해야 합니다.')

class Student(Person):
    def do(self):
        super().do()
        print('공부하는 학생입니다.')

class Employee(Person):
    def do(self):
        super().do()
        print('일하는 직원입니다.')

class Assistance(Employee, Student):
    def do(self):
        super().do()
        print('학생을 도와주는 조료입니다.')

i = Assistance()
i.do()
