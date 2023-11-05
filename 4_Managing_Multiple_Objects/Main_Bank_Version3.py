# Dictionary of account objects
# 개별 Account 객체 식별용

from Account import *

accountsDict = {}
nextAccountNumber = 0

# 새 계좌 2개 생성
oAccount = Account('Carmy', 30, 'Bear')
carmyAccountNumber = nextAccountNumber
accountsDict[carmyAccountNumber] = oAccount
print('Account number for Carmy is:', carmyAccountNumber)
nextAccountNumber += 1

oAccount = Account('Tammy', 100, 'aus')
tammyAccountNumber = nextAccountNumber
accountsDict[tammyAccountNumber] = oAccount
print('Account number for tammy is:', tammyAccountNumber)
nextAccountNumber += 1

accountsDict[carmyAccountNumber].show()
accountsDict[tammyAccountNumber].show()
print()

# Call some methods on the different accounts
print('Calling methods of the two accounts ...')
accountsDict[carmyAccountNumber].deposit(50, 'Bear')
accountsDict[tammyAccountNumber].withdraw(34, 'aus')
accountsDict[tammyAccountNumber].deposit(100, 'aus')

# Show the accounts
accountsDict[carmyAccountNumber].show()
accountsDict[tammyAccountNumber].show()

# create new account with user input
print()
userName = input('Name: ')
userBalance = int(input('Starting balance: '))
userPassword = input('Password: ')
oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = oAccount
print('Account number for new account is:', newAccountNumber)
nextAccountNumber += 1

# show the newly created user account
accountsDict[newAccountNumber].show()

# deposit 100 into the new account
accountsDict[newAccountNumber].deposit(100, userPassword)
userBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print("After depositing 100, user's balance is: ", userBalance)

# Show the new account
accountsDict[newAccountNumber].show()
