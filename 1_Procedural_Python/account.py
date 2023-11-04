# encoding:utf-8
# OOP
# 계좌 클래스

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('incorrect password')
            return None

        if amountToDeposit < 0:
            print('You cannot depoist a negative amount')
            return None

        self.balance = self.balance + amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Incorrect password for this account')
            return None

        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None

        if amountToWithdraw > self.balance:
            print('You cannot withdraw more than you ahve in your account')
            return None

        self.balance -= amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Incorrect password')
            return None
        return self.balance

    def show(self):
        print('     Name:', self.name)
        print('     Balance:', self.balance)
        print('     Password:', self.password)
        print()


























