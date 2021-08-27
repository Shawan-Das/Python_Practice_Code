information=dict()
SavingsAccount=[]
CurrentAccount=[]
'''-----------Code Details--------------------
Savings                             Current
            0----Name
            1----AccountNumber
            2----Balance
            3----minimumBalance
4----Withdraw                    4-----licence
5----Savings Account             5-----Current Account
            *(7----PhoneNumber)
'''

'''-------Account Requirement Help-------------------'''
def help():
    print("Basic Requirements: Name")
    print("Savings Account: you will need to deposit 2000tk to create Savings Account")
    print("Your minimum balance should be 200tk and you can't withdraw more than your maximum Withdraw limit")
    print()
    print("Current Account: you will need to deposit 5000 tk & a trade licence number to create Current Account")
    print("No withdraw limit but account's minimum balance should be 5000tk")
    print("Thank you")
'''-----------------------------------------------------------------'''

'''------Create Saving Account---------'''
def CreateSavingsAccount():
    name=input("Name    : ")
    accountNumber=input("Account Number : ")
    balance=float(input("Deposit Account : "))
    wth=float(input("Maximum Withdraw Limit :"))
    passWord = input("Pass Word  :")

    savings(name,accountNumber,balance,wth,passWord)
'''------------------------------------------------------'''


'''------Create Current Account--------------------------'''
def CreateCurrentAccount():
    name = input("Name    :")
    accountNumber = input("Account Number : ")
    balance = float(input("Deposit Account : "))
    license = input("Trade Licence Number :")
    passWord = input("Pass Word  :")

    current(name, accountNumber, balance, license,passWord)

'''--------------------------------------------------'''

'''----------Add Savings Account-------------------------'''
def savings(name,AccountNumber,balance,maxWithdraw,passWord):
    SavingsAccount.clear()
    SavingsAccount.append(name)
    SavingsAccount.append(AccountNumber)
    SavingsAccount.append(balance)
    SavingsAccount.append(2000.00)
    SavingsAccount.append(maxWithdraw)
    SavingsAccount.append("sa")
    SavingsAccount.append(passWord)
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

'''--------------------------------------------'''


'''------------Add Current Account------------------------'''
def current(name='',AccountNumber="",balance=5000.00,licence='',passWord=""):
    CurrentAccount.clear()
    CurrentAccount.append(name)
    CurrentAccount.append(AccountNumber)
    CurrentAccount.append(balance)
    CurrentAccount.append(5000.00)
    CurrentAccount.append(licence)
    CurrentAccount.append("ca")
    CurrentAccount.append(passWord)

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

'''------------------------------------------------'''

'''--------pwd check---------------'''
def password(accountNumber,pwd):
    if information[accountNumber][6]==pwd:
        return True
    else:
        print("Wrong Password")
        return False
'''-------------------------------------'''

'''---------Check Account-----------------'''
def checkAccount(accountNumber):
    if accountNumber in information.keys():
        return True
    else:
        print("Account Doesn't exist")
        return False
'''-----------------------------------'''


'''--------Deposit Amount--------------'''
def deposit(accountNumber,amount):
    if checkAccount(accountNumber):
        information[accountNumber][2]+=amount
        print("Successful")
    else:
        print("Failed")
'''------------------------------------'''

'''----------- Withdraw amount-------------'''
def cashOut(accountNumber,amount):
    if information[accountNumber][2] - amount > information[accountNumber][3]:
        information[accountNumber][2]-=amount
        print("Cash out Successful")
    else:
        print("Low Balance")

def checkLimit(accountNumber,amount):
    if information[accountNumber][4]>=amount:
        cashOut(accountNumber,amount)
    else:
        print("Can't Withdraw more than ",information[accountNumber][4])

def withdraw(accountNumber,amount):

    if information[accountNumber][5]=="ca":
        cashOut(accountNumber, amount)
    else:
        checkLimit(accountNumber,amount)
'''--------------------------------------'''

'''------------Background Checking------------'''
def backgroundCheck(accountNumber,pwd):
    if checkAccount(accountNumber) and password(accountNumber,pwd):
        return True
    else:
        return False
'''--------------------------------------'''


'''------------Personal Details---------'''
def savingsccountDetails(accountNumber):
    print("Account Type  : "+"Savings Account")
    print("Name          : ",information[accountNumber][0])
    print("Account Number: ",information[accountNumber][1])
    print("Balance       : ",information[accountNumber][2])
    print("Withdraw Limit: ",information[accountNumber][4])

def currentAccountDetails(accountNumber):
    print("Account Type  : " + "Current Account")
    print("Name          : ", information[accountNumber][0])
    print("Account Number: ", information[accountNumber][1])
    print("Balance       : ", information[accountNumber][2])
    print("License Number: ", information[accountNumber][4])

def info(accountNumber,pwd):
    if checkAccount(accountNumber) and backgroundCheck(accountNumber,pwd):
        if information[accountNumber][5]=="ca":
            currentAccountDetails(accountNumber)
        else:
            savingsccountDetails(accountNumber)

'''-----------------------------------------'''

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

        elif option == 1:
            print("Savings Account: 1")
            print("Current Account: 2")

            ad = int(input("Option: "))
            if ad == 1: CreateSavingsAccount()
            if ad == 2: CreateCurrentAccount()

        elif option == 2:
            accountNumber=input("Enter Account Number: ")
            amount=float(input("Amount: "))
            deposit(accountNumber,amount)

        elif option == 3:
            accountNumber = input("Enter Account Number: ")
            pwd = input("Enter Password : ")
            amount = float(input("Amount: "))
            if backgroundCheck(accountNumber,pwd):
                withdraw(accountNumber,amount)
            else:
                print("Failed")

        elif option==4:
            accountNumber = input("Enter Account Number: ")
            pwd = input("Enter Password : ")
            info(accountNumber,pwd)

        elif option == 5:
            help()

        elif option==912217429:
            AllDetails()

if __name__=="__main__":
    main()

'''---------------------------------------------'''


