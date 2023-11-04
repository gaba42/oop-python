# 비객체지향
# 은행 프로그램 버전 1
# 단일 계좌

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print()
    print('잔고를 확인하려면 b를 누르세요.')
    print('입금하려면 d를 누르세요.')
    print('출금하려면 w를 누르세요.')
    print('계좌 정보를 보려면 s를 누르세요.')
    print('종료하려면 q를 누르세요.')
    print()

    action = input('어떤 작업을 하고 싶으신가요?')
    action = action.lower()  # 입력된 내용을 모두 소문자화한다.
    action = action[0]  # 첫 번째 문자만 사용한다.
    print()

    if action == 'b':
        print('잔고 확인:')
        userPassword = input('비밀번호를 입력하세요: ')
        if userPassword != accountPassword:
            print('비밀번호를 잘못 입력했습니다.')
        else:
            print('현재 잔고: ', accountBalance)

    elif action == 'd':
        print('입금:')
        userDepositAmount = input('입금하고 싶은 금액을 입력하세요: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('비밀번호를 입력하세요: ')

        if userDepositAmount < 0:
            print('입금 금액으로 음수를 입력할 수 없습니다!')

        elif userPassword != accountPassword:
            print('비밀번호를 잘못 입력했습니다.')

        else:  # OK
            accountBalance = accountBalance + userDepositAmount
            print('입금 후 잔고:', accountBalance)

    elif action == 's':   # 보여준다.
        print('계좌 정보 확인:')
        print('             계좌주:', accountName)
        print('             잔고:', accountBalance)
        print('             비밀번호:', accountPassword)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('출금:')
        userWithdrawAmount = input('출금하고자 하는 금액을 입력하세요: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('비밀번호를 입력하세요: ')

        if userWithdrawAmount < 0:
            print('출금 금액을 음수로 입력할 수 없습니다!')

        elif userPassword != accountPassword:
            print('비밀번호를 잘못 입력했습니다.')

        elif userWithdrawAmount > accountBalance:
            print('잔고보다 많은 금액을 출금할 수 없습니다.')

        else:  # OK
            accountBalance = accountBalance - userWithdrawAmount
            print('출금 후 잔고:', accountBalance)

print('끝')
