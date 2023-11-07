# Account 객체를 딕셔너리로 관리하는 Bank 클래스
from Account import *

class Bank():
    def __init(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        # Increment to prepare for next account to be created
        self.nextAccountNumber += 1
        return newAccountNumber

    def openAccount(self):
        print('*** Open Account ***')
        userName = input('Name for the new account: ')
        userStartingAmount = int(input('Starting balance for this account:'))
        userPassword = input('Password for this account:')

        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)
        print()

    def closeAccount(self):
        print("*** Close Account ***")
        userAccountNumber = int(input('Account number: '))
        userPassword = input('Password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)

        if theBalance is not None:
            print('You had', theBalance, 'in your account, which is being returned to you.')
            # remove user's account from the dictionary of accounts
            del self.accountsDict[userAccountNumber]
            print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = int(input('Account number: '))
        userAccountPassword = input('Password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        accountNum = int(input('Account number: '))
        depositAmount = int(input('Amount to deposit: '))
        userAccountPassword = input('Password: ')
        oAccount = self.accountsDict[accountNum]
        theBalance = oAccount.deposit(depositAmount, userAccountPassword)
        if theBalance is not None:
            print('Your new balance is:', theBalance)

    def show(self):
        print("*** Show ***")
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('    Account number:', userAccountNumber)
            oAccount.show()

    def withdraw(self):
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAmount = input('Please enter the amount to withdraw: ')
        userAmount = int(userAmount)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None:
            print('Withdrew:', userAmount)
            print('Your new balance is:', theBalance)

    def bankInfo(self):
        print('Hours: 9 to 5')
        print('Address: 123 Main Street, Anytown, USA')
        print('Phone:  (650) 555-1212')
        print('We currently have', len(self.accountsDict), 'account(s) open.')