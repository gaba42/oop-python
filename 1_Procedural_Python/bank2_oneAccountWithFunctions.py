# 비객체지향
# 은행 프로그램 버전 2
# 단일 계좌

accountName = ''
accountBalance = 0
accountPassword = ''


def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password


def show():
    global accountName, accountBalance, accountPassword
    print('             계좌주:', accountName)
    print('             잔고:', accountBalance)
    print('             비밀번호:', accountPassword)
    print()


def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('비밀번호를 잘못 입력했습니다.')
        return None
    return accountBalance


def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('입금 금액으로 음수를 입력할 수 없습니다!')
        return None

    if password != accountPassword:
        print('비밀번호를 잘못 입력했습니다.')
        return None

    accountBalance = accountBalance + amountToDeposit
    return accountBalance


def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('출금 금액을 음수로 입력할 수 없습니다.')
        return None

    if password != accountPassword:
        print('비밀번호를 잘못 입력했습니다.')
        return None

    if amountToWithdraw > accountBalance:
        print('잔고보다 많은 금액을 출금할 수 없습니다.')
        return None

    accountBalance = accountBalance - amountToWithdraw
    return accountBalance


newAccount('Joe', 100, 'soup')  # 계좌 생성

while True:
    print()
    print('잔고를 확인하려면 b를 누르세요.')
    print('입금하려면 d를 누르세요.')
    print('출금하려면 w를 누르세요.')
    print('계좌 정보를 보려면 s를 누르세요.')
    print('종료하려면 q를 누르세요.')
    print()

    action = input('어떤 작업을 하고 싶으신가요?')
    action = action.lower()  # 입력된 내용을 모두 소문자화한다
    action = action[0]  # 첫 번째 문자만 사용한다.
    print()

    if action == 'b':
        print('잔고 확인')
        userPassword = input('비밀번호를 입력하세요.')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('현재 잔고:', theBalance)

    elif action == 'd':
        print('입금:')
        userDepositAmount = input('입금하고 싶은 금액을 입력하세요: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('비밀번호를 입력하세요: ')

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('현재 잔고:', newBalance)

    elif action == 'w':
        print('출금:')
        userWithdrawAmount = int(input('출금하고 싶은 금액을 입력하세요: '))
        userPassword = input('비밀번호를 입력하세요: ')

        newBalance = withdraw(userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('현재 잔고:', newBalance)

    elif action == 's':
        print('계좌정보:')
        show()

    elif action == 'q':
        print('종료')
        break
