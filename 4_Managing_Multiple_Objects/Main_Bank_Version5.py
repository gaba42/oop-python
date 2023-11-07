# 계좌들을 관리하는 Bank 객체를 제어하는 메인 프로그램

from Bank import *

# Create an instance of the Bank
oBank = Bank()

# Main
carmyAccountNumber = oBank.createAccount('Carmy', 30, 'Bear')
print("Carmy's account number is:", carmyAccountNumber)

tammyAccountNumber = oBank.createAccount('Tammy', 100, 'aus')
print("Tammy's account number is:", tammyAccountNumber)

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]  # grab the first letter
    print()

    if action == 'b':
        oBank.balance()

    elif action == 'c':
        oBank.closeAccount()

    elif action == 'd':
        oBank.deposit()

    elif action == 'i':
        oBank.bankInfo()

    elif action == 'o':
        oBank.openAccount()

    elif action == 's':
        oBank.show()

    elif action == 'q':
        break

    elif action == 'w':
        oBank.withdraw()

    else:
        print('Sorry, that was not a valid action.  Please try again.')

print('Done')