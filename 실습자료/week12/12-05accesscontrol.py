'12-05accesscontrol.py'
'속성과 메소드의 접근 제어'

class Account:
    ''' 은행 계좌를 표현하는 클래스 '''
    def __init__(self, name, amount):
        self.name = name
        self.__balance = amount # 비공개 속성

    def __str__(self):
        return '예금주 {}, 잔고 {}'.format(self.name, self.__balance)

    def __info(self): # 비공개 메소드 구현
        print('\t', self) # 위 메소드 __str__(slef) 호출
        # print(self.__str__())

    def widthdraw(self, amount):
        self.__balance -= amount
        print('출금 {}원 이후:'.format(amount))
        self.__info()

    def deposit(self, amount):
        self.__balance += amount
        print('입금 {}원 이후:'.format(amount))
        self.__info()

acc = Account('이은행', 100000)
print(acc) # 문자열화 메소드 __str__(self) 호출
acc.deposit(5000)
acc.widthdraw(10000)
print(acc.__balance) # 참조 불가능해 오류 발생
acc.__info() # 참조 불가능해 오류 발생
