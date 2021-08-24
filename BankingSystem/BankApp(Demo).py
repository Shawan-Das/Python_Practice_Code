information=dict()
SavingsAccount=[]
CurrentAccount=[]
'''-----------Code Details--------
Savings                             Current
            0----Name
            1----AccountNumber
            2----PassWord
            3----Balance
            4----minimumBalance
5----Withdraw                    5-----licence
            *(6----PhoneNumber)
'''

'''-------Account Requirement Help----'''
def help():
    print("Basic Requirements: Name")
    print("Savings Account: you will need to deposit 2000tk to create Savings Account")
    print("Your minimum balance should be 200tk and you can't withdraw more than your maximum Withdraw limit")
    print()
    print("Current Account: you will need to deposit 5000 tk & a trade licence number to create Current Account")
    print("No withdraw limit but account's minimum balance should be 5000tk")
    print("Thank you")
'''---------------------------------------------'''

'''------Create Saving Account---------'''
def CreateSavingsAccount():
    pass

'''---------------------------'''


'''------Create Current Account---------'''
def CreateCurrentAccount():
    pass

'''-------------------------------'''

'''----------Add Savings Account--------------'''
def savings(name='',AccountNumber="",passWord='123456789',balance=0.00,maxWithdraw=0.00):
    SavingsAccount.clear()
    SavingsAccount.append(name)
    SavingsAccount.append(AccountNumber)
    SavingsAccount.append(passWord)
    SavingsAccount.append(balance)
    SavingsAccount.append(2000.00)
    SavingsAccount.append(maxWithdraw)
    if AccountNumber not in information.keys():
        information[AccountNumber]=SavingsAccount
        print("WellCome to Our Bank "+name)
        print("Your Current Balance: "+str(balance))
    else:
        print("Account Exist")
        print()
        print("      Try Again: 1")
        print("Create Current Account: 2")
        s=int(input("Option: "))

        if s==1: CreateSavingsAccount()
        if s==2: CreateCurrentAccount()

'''-----------------------'''


'''------------Add Current Account---------------'''
def current(name='',AccountNumber="",passWord='123456789',balance=5000.00,licence=''):
    CurrentAccount.clear()
    CurrentAccount.append(name)
    CurrentAccount.append(AccountNumber)
    CurrentAccount.append(passWord)
    CurrentAccount.append(balance)
    CurrentAccount.append(5000)
    CurrentAccount.append(licence)

    if AccountNumber not in information.keys():
        information[AccountNumber]=CurrentAccount
        print("WellCome to Our Bank "+name)
        print("Your Current Balance: "+str(balance))
    else:
        print("Account Exist")
        print()
        print("      Try Again : 1")
        print("Create Savings Account: 2")
        s = int(input("Option: "))

        if s == 1: CreateCurrentAccount()
        if s == 2: CreateSavingsAccount()

'''--------Deposit Amount------'''
def deposit():
    pass
'''---------------------------'''

'''--- Withdraw amount'''
def SavingsWithdraw():
    pass

def withdraw():
    pass
'''----------------'''


'''---------------Main Portion-----------'''
# print("Well Come to our service")
# print()
# print("Exit: 0")
# print("Create Account: 1")
# print("Deposit: 2")
# print("Withdraw: 3")
# print("Information: 4")
# print("Account Requirements : 5")
#
# option=int(input("Enter Option: "))

def main():
    while (True):
        print()
        print("Exit: 0")
        print("Create Account: 1")
        print("Deposit: 2")
        print("Withdraw: 3")
        print("Information: 4")
        print("Account Requirements : 5")

        option = int(input("Enter Option: "))

        if option == 0:
            break
        elif option == 2:
            deposit()
        elif option == 3:
            withdraw()
        elif option == 5:
            help()
        elif option == 2:
            print("Savings Account: 1")
            print("Current Account: 2")

            ad = int(input("Option: "))
            if ad == 1: CreateSavingsAccount()
            if ad == 2: CreateCurrentAccount()

if __name__=="__main__":
    main()

'''---------------------------------------------'''


