class BankAccount:
    def __init__(self,name="",balance=0.00,minblance=0.1,pwd='123456789',accountNUmber=""):
        self.name=name
        self.balance=balance
        self.minbalance=minblance
        self.pwd=pwd
        self.accountNumber=accountNUmber

    def setPass(self,newPass):
        self.pwd=newPass

    def setName(self,newName):
        self.name=newName

    def depodit(self,amount):
        self.balance+=amount

    def withdraw(self, amount):
        if(self.balance - amount > self.minbalance):
            self.balance= self.balance - amount
        else:
            print("Insufficient Balance")


