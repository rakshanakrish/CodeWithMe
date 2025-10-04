class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposite(self,amt):
        if amt>0:
            self.__balance+=amt
    def withdraw(self,amt):
        if 0<amt<self.__balance:
            self.__balance-=amt
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
p1=BankAccount(1000)
p1.deposite(500)
p1.withdraw(200)
print(p1.get_balance())

