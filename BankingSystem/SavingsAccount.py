import BankAccount

class SavingsAccount(BankAccount):
    interest=0.5

    def __init__(self, name="", balance=0.00, pwd="123456789",accountNumber=" ",limit=0.00):
        super().__init__(self, name,balance,2000,pwd,accountNumber)
        self.maxLimit=limit

    def calculateInteresr(self):
        return self.interest * self.balance

    def getBalance(self):
        return self.getBalance() + self.balance

    def withdraw(self,amount):
        if(amount<=self.maxLimit):
            if (self.balance - amount > self.minbalance):
                self.balance = self.balance - amount
            else:
                print("Insufficient Balance")
        else:
            print("Can't withdraw more than: "+str(self.maxLimit))


    def print_info(self):
        print("Name          : ",+self.name)
        print("Account Number: ",+self.accuntNumber)
        print("Balance       : ",+self.balance)
        print("Withdraw Limit: ",+self.maxLimit)