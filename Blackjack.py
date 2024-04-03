import random

class Card:
    value = 0
    name = ""
    
    def getValue():
        return self.value

    def getName():
        return self.name
    

def runGame():
    handValue = 0
    dealerValue = 0

    cardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    faceCards = [1, 2, 3]
    
    cardValue1 = random.choice(cardValues)
    if cardValue1 == 10:
        cardType = random.choice(faceCards)
        if cardType == 1:
            print("You are dealt a: Jack" )
        elif cardType == 2:
            print("You are dealt a: Queen")
        elif cardType == 3:
            print("You are dealt a: King")
    elif cardValue1 == 1:
        print("You are dealt an: Ace")
    else:
        print("You are dealt a: " + cardValue1)

    handValue += cardValue1

    cardValue2 = random.choice(cardValues)
    if cardValue2 == 10:
        cardType = random.choice(faceCards)
        if cardType == 1:
            print("You are dealt a: Jack" )
        elif cardType == 2:
            print("You are dealt a: Queen")
        elif cardType == 3:
            print("You are dealt a: King")
    elif cardValue2 == 1:
        print("You are dealt an: Ace")
    else:
        print("You are dealt a: " + cardValue2)

    handValue += cardValue2

    print("Your total hand value is: " + handValue)
    
    dealerCard1 = random.choice(cardValues)
    dealerValue += dealerCard1
    
    dealerCard2 = random.choice(cardValues)
    if dealerCard2 == 10:
        dealerCardType = random.choice(faceCards)
        if dealerCardType == 1:
            print("The dealer has a Jack showing")
        elif dealerCardType == 2:
            print("The dealer has a Queen showing")
        elif dealerCardType == 3:
            print("The dealer has a King showing")
    elif dealerCard2 == 1:
        print("The dealer has an Ace showing")
    else:
        print("The dealer has a " + dealerCard2 + " showing")

    dealerValue += dealerCard2

    

def main():
    gameNum = 1
    
    print("Welcome To BlackJack!")
    print("Game #" + str(gameNum))
    
    playAgain = True
    while playAgain:
        break

main()