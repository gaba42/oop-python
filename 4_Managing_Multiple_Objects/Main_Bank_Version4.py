# Interactive Menu
from Account import *

accountsDict = {}
nextAccountNumber = 0

oAccount = Account('Carmy', 30, 'bear')
accountsDict[next()] = oAccount
nextAccountNumber += 1

oAccount = Account('Tammy', 100, 'aus')
accountsDict[next()] = oAccount
nextAccountNumber += 1
