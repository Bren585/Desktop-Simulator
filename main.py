from yahtzee import Yahtzee
from poker import Poker
from blackjack import Blackjack

players = None
choice = None

while players == None:
    try:
        print("How many players?")
        players = int(input(" > "))
    except ValueError:
        print("Invalid number.")
    if players == 0:
        print("No.")
        players == None

while choice != 0:
    print("Select a Game: ")
    print(" 1 - Blackjack")
    print(" 2 - Poker")
    print(" 3 - Yahtzee")
    print(" 0 - Exit")
    try:
        choice = int(input(" > "))
    except ValueError:
        print("That is not a valid input. Please try again.")
        continue

    if choice == 0:
        print("Goodbye.")
    elif choice == 1:
        Blackjack(players)
    elif choice == 2:
        if players < 3:
            print("Two few players.")
            continue
        Poker(players)
    elif choice == 3:
        Yahtzee(players)
    else:
        print("That is not a valid input. Please try again.")
