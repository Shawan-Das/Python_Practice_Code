import BankAccount
import SavingsAccount
import CurrentAccount

variable = []
class Bank():

    def savings(self,name,balance,pwd,accountNumber,limit):
        s= SavingsAccount(name,balance,pwd,accountNumber,limit)
        variable.append(s)

    def current(self,name,balance,pwd,accountNumber,license):
        c=CurrentAccount(name,balance,pwd,accountNumber,license)
        variable.append(c)




