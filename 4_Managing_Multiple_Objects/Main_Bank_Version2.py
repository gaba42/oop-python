# List of account objects
# 다뤄야 할 데이터가 매우 많은 경우에는 리스트를 활용하는 게 좋은 해결책이다

from Account import *

accountsList = []

# create two accounts
oAccount = Account('Carmy', 30, 'Bear')
accountsList.append(oAccount)
print(f"Carmy's account number is {len(accountsList)}")

oAccount = Account('Tammy', 100, 'aus')
accountsList.append(oAccount)
print("Tammy's account number is 1")

accountsList[0].show()
accountsList[1].show()
print()

# Call some methods on the different accounts
print('Calling methods of the two accounts ...')
accountsList[0].deposit(50, 'Bear')
accountsList[1].withdraw(34, 'aus')
accountsList[1].deposit(100, 'aus')

# Show the accounts
accountsList[0].show()
accountsList[1].show()

# Create another account with information from the user
print()
userName = input('Name for the new user account: ')
userBalance = int(input('Starting balance for this account: '))
userPassword = input('Password for this account: ')
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)  # append to list of accounts

# Show the newly created user account
print('Created new account, account number is 2')
accountsList[2].show()

# deposit 100 into the new account
accountsList[2].deposit(100, userPassword)
usersBalance = accountsList[2].getBalance(userPassword)
print()
print("After depositing 100, user's balance is:", usersBalance)

# show the new account
accountsList[2].show()