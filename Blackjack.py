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
    
    print("Your total hand value is: " + str(playerValue) + "\n")
    print("The dealer has a " + getCardName(dealerValue) + " showing\n")

    midGameMenu(playerValue, dealerValue)

def midGameMenu(handVal, dealerVal):
    choice = 0
    while choice != 1 and choice != 2: 
        choice = input("What do you do? Type a number(1/2):\n1. Hit\n2. Stay\nChoice: ")
        choice = int(choice)
    if choice == 1:
        pass
    if choice == 2:
        print("\nThe dealer reveals a total hand value of: " + str(dealerVal) + "\n")
        if dealerVal > handVal:
            print("The dealer is closer to 21, YOU LOSE")
        elif dealerVal < handVal:
            print("You are closer to 21, YOU WIN")
        elif dealerVal == handVal:
            print("You and the dealer PUSH")

    

def main():
    gameNum = 1
    
    print("Welcome To BlackJack!\n")
    print("Game #" + str(gameNum) + "\n")
    
    playAgain = True
    while playAgain:
        runGame()
        validResponse = False
        while not validResponse:
            response = input("\nWould you like to play again? (y/n): ")
            if response == "y":
                print("\n")
                playAgain = True
                validResponse = True
                gameNum += 1
                print("Game #" + str(gameNum))
            elif response == "n":
                print("\nThanks for playing!")
                playAgain = False
                validResponse = True
            else:
                print("That is not a valid response.")
        

main()