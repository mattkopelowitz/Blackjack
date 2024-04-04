import random

def getCardName(cardValue):
    cardNames = {
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King",
    }
    return cardNames.get(cardValue, str(cardValue))

def dealCard(handValue, handName):
    cardValue = random.choice([1,2,3,4,5,6,7,8,9,10])
    if cardValue == 10:
        faceValue = random.choice([11, 12, 13])
        cardName = getCardName(faceValue)
    else:
        cardName = getCardName(cardValue)
    
    if handName == "Player":
        print("You are dealt a " + cardName)
    handValue += cardValue
    return handValue

def runGame():
    playerValue = 0
    dealerValue = 0

    playerValue = dealCard(playerValue, "Player")
    playerValue = dealCard(playerValue, "Player")

    dealerValue = dealCard(dealerValue, "Dealer")
    dealerValue = dealCard(dealerValue, "Dealer")
    
    print("Your total hand value is: " + str(playerValue))
    print("The dealer has a " + getCardName(dealerValue) + " showing")
    

def main():
    gameNum = 1
    
    print("Welcome To BlackJack!")
    print("Game #" + str(gameNum))
    
    playAgain = True
    while playAgain:
        runGame()
        validResponse = False
        while not validResponse:
            response = input("Would you like to play again? (y/n): ")
            if response == "y":
                playAgain = True
                validResponse = True
                gameNum += 1
                print("Game #" + str(gameNum))
            elif response == "n":
                playAgain = False
                validResponse = True
            else:
                print("That is not a valid response.")
        

main()