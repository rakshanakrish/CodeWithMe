class Bank:
    def __init__(self,cust_name,account_no,balance):
        self.cust_name=cust_name
        self.account_no=account_no
        self.balance=balance
    def __str__(self):
        return str(self.balance)

Cust1=Bank('Rakshana',12345678,10)
print(Cust1)
        