# Account class

# Account 클래스 파일의 모든 내용 불러오기
from Account import *

# 계좌 두 개 생성
oCarmyAccount = Account('Carmy', 42, 'Bear')
print('Created an account for Carmy')

oTammyAccount = Account('Tammy', 100, 'aus')
print('Created an account for Tammy')

oCarmyAccount.show()
oTammyAccount.show()
print()

print('calling methods of the two accounts...')
oCarmyAccount.deposit(50, 'Bear')
oTammyAccount.withdraw(34, 'aus')
oTammyAccount.deposit(100, 'aus')

oCarmyAccount.show()
oTammyAccount.show()

# 새 계좌 생성
print()
userName = input('신규 계좌 사용자 이름은?')
userBalance = int(input('시작 잔고는?'))
userPassword = input('비밀번호는?')
oNewAccount = Account(userName, userBalance, userPassword)

oNewAccount.show()

oNewAccount.deposit(100, userPassword)
userBalance = oNewAccount.getBalance(userPassword)
print()
print('100달러 입근 후 잔고: ', userBalance)

oNewAccount.show()

