'12-12attributemro.py'
'다중 상속에서 메소드 해결 순서'

class Person():
    def hello(self):
        print('안녕, 난 사람이야!')

class Student(Person):
    def hello(self):
        super().do()
        print('안녕, 난 학생이야!')

class Employee(Person):
    def do(self):
        super().do()
        print('안녕, 난 직원이야!')

class Assistance(Employee, Student):
    def do(self):
        pass

print(Assistance.__mro__)
print(Assistance.mro())

i = Assistance()
i.do()
