from replit import clear

# HINT: You can call clear() to clear the output in the console.

# clear.clear()
dictionary = []
continueBid = True

# this is to find winner
# of the game
# testing docstring now
# for commenting


def findWinner():
    winnerBid = 0
    winnerName = ""
    for i in range(0, len(dictionary)):
        print(dictionary[i])
        bidAmt = dictionary[i]["bidPrice"]
        if winnerBid < bidAmt:
            winnerBid = dictionary[i]["bidPrice"]
            winnerName = dictionary[i]["name"]
    print(f"Winner is {str(winnerName).title()} and {winnerBid}")


while continueBid:

    name = input("Welcome to bidding\nYour name ?\n")
    bidPrice = int(input("Your bid price?"))

    newObj = {"name": name, "bidPrice": bidPrice}
    dictionary.append(newObj)

    ans = input("Do you want to continue? (y/n): ")
    if ans == "y":
        clear()
        continueBid = True
    else:
        findWinner()
        continueBid = False
