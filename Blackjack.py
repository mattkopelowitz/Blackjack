import random

# Takes in the card value and returns the name of the card
def getCardName(cardValue):
    cardNames = {
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King",
    }
    return cardNames.get(cardValue, str(cardValue))

# Takes in the current value of player/dealer's hand and which person's hand it is, 
# and deals them a new card returning the new value of their hand
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

# This function runs a single game
def runGame():
    playerValue = 0
    dealerValue = 0

    playerValue = dealCard(playerValue, "Player")
    playerValue = dealCard(playerValue, "Player")

    dealerValue = dealCard(dealerValue, "Dealer")
    print("Your total hand value is: " + str(playerValue) + "\n")
    print("The dealer has a " + getCardName(dealerValue) + " showing\n")
    dealerValue = dealCard(dealerValue, "Dealer")
    
    return midGameMenu(playerValue, dealerValue) # Returns the result of the game

# This function handles the midgame where the player must make choices
def midGameMenu(handVal, dealerVal):
    choice = 0
    while choice != 1 and choice != 2: 
        if choice != 0:
            print("That is not a valid choice")
        choice = input("What do you do? Type a number(1/2):\n1. Hit\n2. Stay\nChoice: ")
        choice = int(choice)
        print("\n")

    # Player Hits
    if choice == 1:
        handVal = dealCard(handVal, "Player")
        print("Your new total hand value is " + str(handVal) + "\n")
        if handVal > 21:
            print("\nYou busted, YOU LOSE")
            return "Loss"
        elif handVal == 21:
            print("BLACKJACK, YOU WIN")
            return "Win"
        else:
            return midGameMenu(handVal, dealerVal) # recursion allows the player to keep hitting until they want to stop or bust
    
    # Player Stays
    elif choice == 2:
        print("\nThe dealer reveals a total hand value of: " + str(dealerVal) + "\n")

        while dealerVal <= 16:
            dealerVal =  dealCard(dealerVal, "Dealer")
            print("The dealer hits and now has a hand value of: " + str(dealerVal) + "\n")

        if dealerVal > 21:
            print("\nThe dealer busted, YOU WIN")
            return "Win"
        else:
            if dealerVal > handVal:
                print("The dealer is closer to 21, YOU LOSE")
                return "Loss"
            elif dealerVal < handVal:
                print("You are closer to 21, YOU WIN")
                return "Win"
            elif dealerVal == handVal:
                print("You and the dealer PUSH")
                return "Tie"

def main():
    # initial variables for keeping track of game number, total balance, and each game's bet amount
    gameNum = 1
    balance = 0
    bet = 0
    
    # Welcome message and determines balance
    print("Welcome To BlackJack!\n")
    balance = int(input("What bankroll would you like to deposit? $"))
    while type(balance) != int or balance < 0:
        balance = int(input("Please enter a valid number. $"))
    
    print("\nBalance: $" + str(balance) + "\n")
    print("Game #" + str(gameNum) + "\n")
    
    # Loop through games while player wants to keep playing or runs out of money
    playAgain = True
    while playAgain:
        # Checks to see if the player still has money in their balance
        if balance <= 0:
            print("Looks like your balance is at $0, Thanks for playing!")
            break
        
        # Asks the player for how much they want to bet on this hand and makes sure it isnt more than what they have in their balance
        bet = int(input("How much would you like to bet on this game? $"))
        while type(bet) != int or bet <= 0 or bet > balance:
            bet = int(input("Please enter a valid number. $"))

        # Subtracts the hand's bet amount from the player's balance
        balance -= bet
        result = runGame()

        # Determine hand result
        if result == "Win":
            balance += (bet*2)
        elif result == "Loss":
            pass
        elif result == "Tie":
            balance += bet
        
        # Continues the game
        validResponse = False
        while not validResponse:
            response = input("\nWould you like to play again? (y/n): ")
            if response == "y":
                print("\n")
                playAgain = True
                validResponse = True
                gameNum += 1
                print("\nBalance: $" + str(balance) + "\n")
                print("Game #" + str(gameNum))
            elif response == "n":
                print("\nThanks for playing! You're ending balance is: $" + str(balance))
                playAgain = False
                validResponse = True
            else:
                print("That is not a valid response.")
        

main()