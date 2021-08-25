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
6----Savings Account             6-----Current Account
            *(7----PhoneNumber)
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
    name=input("Name    :")
    accountNumber=input("Account Number: ")
    passWord=input("Pass Word  :")
    balance=float(input("Deposit Account : "))
    wth=float(input("Maximum Withdraw Limit :"))

    savings(name,accountNumber,passWord,balance,wth)
'''---------------------------'''


'''------Create Current Account---------'''
def CreateCurrentAccount():
    name = input("Name    :")
    accountNumber = input("Account Number: ")
    passWord = input("Pass Word  :")
    balance = float(input("Deposit Account : "))
    license = input("Maximum Withdraw Limit :")

    current(name, accountNumber, passWord, balance, license)

'''-------------------------------'''

'''----------Add Savings Account--------------'''
def savings(name='',AccountNumber="",passWord='123456789',balance=0.00,maxWithdraw=0.00):
    SavingsAccount.clear()
    SavingsAccount.append(name)
    SavingsAccount.append(AccountNumber)
    SavingsAccount.append(passWord)
    SavingsAccount.append(balance)
    SavingsAccount.append(2000.00)
    SavingsAccount.append("Savings Account")
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
    CurrentAccount.append("Current Account")

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


'''--------pwd check-----'''
def password(accountNumber,pwd):
    if information[accountNumber][2]==pwd:
        return True
    else:
        print("Wrong Password")
        return False
'''-------------------------------------'''

'''---------Check Account--------'''
def checkAccount(accountNumber):
    if accountNumber in information.keys():
        return True
    else:
        print("Account Doesn't exist")
        return False
'''-----------------------------------'''


'''--------Deposit Amount------'''
def deposit(accountNumber,amount):
    if checkAccount(accountNumber):
        information[accountNumber][3]+=amount
        print("Successful")
    else:
        print("Failed")
'''---------------------------'''

'''--- Withdraw amount-------'''
def cashOut(accountNumber,amount):
    information[accountNumber][3]-=amount

def checkLimit(accountNumber,amount):
    if information[accountNumber][5]<=amount:
        cashOut(accountNumber,amount)
    else:
        print("Can't Withdraw more than ",information[accountNumber][5])

def withdraw(accountNumber,amount):

    if information[accountNumber][6]=="Current Account":
        cashOut(accountNumber,amount)

    else:
        checkLimit(accountNumber,amount)

'''--------------------------------------'''

'''------------Background Checking------------'''
def backgroundCheck(accountNumber,pwd):
    if checkAccount(accountNumber) and password(pwd):
        return True
    else:
        return False

'''----------------'''
'''------------Personal Details---------'''
def savingsccountDetails(accountNumber):
    print("Account Type  : "+"Savings Account")
    print("Name          : ",information[0])
    print("Account Number: ",information[1])
    print("Balance       : ",information[3])
    print("Withdraw Limit: ",information[5])


def currentAccountDetails(accountNumber):
    print("Account Type  : " + "Current Account")
    print("Name          : ", information[0])
    print("Account Number: ", information[1])
    print("Balance       : ", information[3])
    print("License Number: ", information[5])

def info(accountNumber,pwd):
    if backgroundCheck(accountNumber,pwd):
        if information[accountNumber][6]=="Current Account":
            currentAccountDetails(accountNumber)
        else:
            savingsccountDetails(accountNumber)
'''-------------All Account Details----------'''
def AllDetails():
    print("Total Account: ",len(information))
    print()
    for i in information.keys():
        print(information[i])
        print()
'''-------------------'''

'''---------------Main Portion-----------'''

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

        if option == 0: break

        elif option == 2:
            accountNumber=input("Enter Account Number: ")
            amount=float(input("Amount: "))
            deposit(accountNumber,amount)

        elif option==4:
            accountNumber = input("Enter Account Number: ")
            pwd = input("Enter Password : ")
            info(accountNumber,pwd)

        elif option == 3:
            accountNumber = input("Enter Account Number: ")
            pwd=input("Enter Password : ")
            amount = float(input("Amount: "))
            if backgroundCheck(accountNumber,pwd):
                withdraw(accountNumber,amount)

        elif option == 5:
            help()
        elif option == 2:
            print("Savings Account: 1")
            print("Current Account: 2")

            ad = int(input("Option: "))
            if ad == 1: CreateSavingsAccount()
            if ad == 2: CreateCurrentAccount()

        if option==912217429:
            pass

if __name__=="__main__":
    main()

'''---------------------------------------------'''


