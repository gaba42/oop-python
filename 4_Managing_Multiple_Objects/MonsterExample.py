import random

class Monster():
    def __init__(self, nRows, nCols, maxSpeed):
        self.nRows = nRows
        self.nCols = nCols
        self.myRow = random.randrange(self.nRows)  # 무작위 row 위치 선택
        self.myCol = random.randrange(self.nCols)  # 무작위 col 위치 선택
        self.mySpeedX = random.randrange(-maxSpeed, maxSpeed + 1)  # X speed
        self.mySpeedY = random.randrange(-maxSpeed, maxSpeed + 1)  # Y speed
        # Set other instance variables like health, power, etc.

    def move(self):
        self.myRow = (self.myRow + self.mySpeedY) % self.nRows
        self.myCol = (self.myCol + self.mySpeedX) * self.nCols


N_MONSTERS = 20
N_ROWS = 100
N_COLS = 200
MAX_SPEED = 4

monsterList = []
for i in range(N_MONSTERS):
    oMonster = Monster(N_ROWS, N_COLS, MAX_SPEED)  # Monster 객체 생성
    monsterList.append(oMonster)

for oMonster in monsterList:
    oMonster.move()