# Higher or Lower
# 절차적 프로그래밍 기법으로 작성

import random

# 카드 상수
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamons')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
NCARDS = 8


# 입력받은 카드 덱에서 임의로 한 장의 카드를 선택해 반환한다.
def getCard(deckListIn):
    thisCard = deckListIn.pop()  # 카드 덱 맨 위의 카드를 꺼내 반환
    return thisCard


# 입력받은 카드 덱을 복사한 후 복사본을 무작위로 뒤섞어 반환한다
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # 원본 카드 덱의 복사본 생성
    random.shuffle(deckListOut)
    return deckListOut


# 메인 코드
print('Hihger or Lower 게임에 오신 것을 환영합니다.')
print('여러분은 다음에 보일 카드가 현재 카드보다 크거나 작은지 선택해야 합니다.')
print('맞힌다면 20점을 얻고 틀린다면 15점 감점됩니다.')
print('처음에는 50점이 주어집니다.')
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:  # 게임 여러 차례 플레이
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('카드 덱 가장 위의 카드 등급은 ', currentCardRank + ', 문양은 ' + currentCardSuit + ' 입니다.')
    print()

    for cardNumber in range(0, NCARDS):  #NCARDS만큼의 카드가 소진될 때까지
        answer = input('이 다음에 보여질 카드는 (등급 :' +
                       currentCardRank + ', 문양 :' +
                       currentCardSuit + ') 보다 클까요? 작을까요? (h 또는 l 입력): ')

        answer = answer.casefold()  #  입력된 내용을 모두 소문자화한다.
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('다음 카드의 등급은 ', nextCardRank + ', 문양은 ' + nextCardSuit + ' 입니다.')

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('맞혔습니다. 값이 더 큽니다.')
                score = score + 20

            else:
                print('틀렸습니다. 값이 더 크지 않았습니다.')
                score = score - 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('맞혔습니다. 값이 더 작습니다.')

            else:
                score = score - 15
                print('틀렸습니다. 값이 더 작지 않습니다.')

        print('현재 점수는 ' + str(score) + ' 입니다.')
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue  # 현재 문양은 필요 없다
        currentCardSuit = nextCardSuit

    goAgain = input('한 번 더 하려면 Enter 키를, 그만두려면 "q"를 입력하세요: ')
    if goAgain == 'q':
        break
print('수고하셨습니다.')