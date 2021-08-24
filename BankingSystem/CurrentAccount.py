import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self,name="", balance=0.00, pwd='123456789',accountNumber='',license=""):
        super().__init__(self, name, balance, 5000, pwd, accountNumber)
        self.license=license

    def setPass(self,newPass):
        self.pwd=newPass

    def setName(self,newName):
        self.name=newName

    def print_info(self):
        print("Name          : ",+self.name)
        print("Account Number: ",+self.accuntNumber)
        print("Balance       : ",+self.balance)
        print("License       : ",+self.license)
        