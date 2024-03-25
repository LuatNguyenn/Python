import random
import sys


userCard = [random.randint(2, 11), random.randint(2, 11)]

computerCard = [random.randint(2, 11), random.randint(2, 11)]


def askToPlayGame():
    print(
        """.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
      |  \/ K|                            _/ |                
      '------'                           |__/"""
        ""
    )
    playGame = str(input("Do you want to play the game ? (y/n)"))
    if playGame == "y":
        logic()


def checkIfBlackJack(userCard, computerCard):
    if userCard[0] == 11 and userCard[1] == 11:
        return "user win"
    elif computerCard[0] == 11 and computerCard[1] == 11:
        return "computer win"


def askToContinue():

    print(userCard)

    inputContinue = str(input("Do you want to continue (y/n)").lower())

    if inputContinue == "y":
        userCard.clear()
        computerCard.clear()
        userCard = [random.randint(2, 11), random.randint(2, 11)]
        computerCard = [random.randint(2, 11), random.randint(2, 11)]
        logic()
    elif inputContinue == "n":
        sys.exit()
    else:
        input("Invalid input")
        askToContinue()


def calculateTotalScore(cards):
    total = 0
    for score in cards:
        total += score
    return total


def compareResults():
    userScore = calculateTotalScore(userCard)
    computerScore = calculateTotalScore(computerCard)

    if userScore > computerScore and userScore < 22:
        return "user win"
    elif computerScore > userScore and computerScore < 22:
        return "computer win"


def computerDrawAnotherCard():
    newCard = random.randint(2, 11)
    if len(computerCard) == 2:
        computerCard.append(newCard)
    elif len(computerCard > 2):
        total = calculateTotalScore(computerCard)
        if total <= 21:
            return
        elif total < 17:
            computerDrawAnotherCard()
            print("COMPUTER CARD: ", computerCard)


def userDrawAnotherCard():
    newCard = random.randint(2, 11)
    userCard.append(newCard)


def isBust(totalScore):
    if totalScore > 21:
        return True


def showUserWin():
    print(
        f"YOUR CURRENT CARD {userCard}\nTOTAL SCORE: {calculateTotalScore(userCard)}\n\n"
    )
    print(
        f"COMPUTER FINAL HAND {computerCard}\nTOTAL SCORE: {calculateTotalScore(computerCard)}\n\n"
    )
    print("USER WIN\n")


def showComputerWin():
    print(
        f"YOUR CURRENT CARD {userCard}\nTOTAL SCORE: {calculateTotalScore(userCard)}\n\n"
    )
    print(
        f"COMPUTER FINAL HAND {computerCard}\nTOTAL SCORE: {calculateTotalScore(computerCard)}\n\n"
    )
    print("COMPUTER WIN\n")
    # askToContinue()


def logic():

    totalScore = userCard[0] + userCard[1]
    totalScore = calculateTotalScore(userCard)
    print("\n\n")
    print(f"YOUR CARD: {userCard}, CURRENT SCORE: {totalScore}")
    print(f"COMPUTER FIRST CARD: {computerCard[0]}")
    winner = checkIfBlackJack(userCard, computerCard)
    print("\n\n")
    if winner == "computer win":
        print(f"Computer win [BLACK JACK] {computerCard}")
        askToContinue()
    elif winner == "user win":
        print(f"User win [BLACK JACK] {userCard}")
        # askToContinue()

    drawFlag = True
    while drawFlag == True:
        drawCardInput = str(input("Do you want to draw another card? (y/n) ").lower())
        print("\n\n")
        if drawCardInput == "y":
            userDrawAnotherCard()
            totalScore = calculateTotalScore(userCard)
            print(f"YOUR CURRENT CARD {userCard}\nTOTAL SCORE: {totalScore}\n\n")
            if isBust(totalScore):
                print(f"-------------YOU BUSTED-------------\n")
                print(f"YOUR FINAL HAND: {userCard}, FINAL SCORE: {totalScore}")
                askToContinue()
                drawFlag = False

        elif drawCardInput == "n":
            drawFlag = False
            if computerCard[0] + computerCard[1] < 17:
                computerDrawAnotherCard()
                # drawFlag = False
                if compareResults() == "computer win":
                    showComputerWin()
                    return
                else:
                    showUserWin()
                    return

            else:
                compareResults()


askToPlayGame()
