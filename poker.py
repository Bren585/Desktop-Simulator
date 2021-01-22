from pieces import *

def treat(values, suits, num):
    for x in range(0, num):
        if suits[x] == 0:
            suits[x] = "S"
        elif suits[x] == 1:
            suits[x] = "D"
        elif suits[x] == 2:
            suits[x] = "C"
        elif suits[x] == 3:
            suits[x] = "H"

    for x in range(0, num):
        if values[x] == 1:
            values[x] = "A"
        elif values[x] == 11:
            values[x] = "J"
        elif values[x] == 12:
            values[x] = "Q"
        elif values[x] == 13:
            values[x] = "K"

def Poker(numPlayers):
    play = True
    
    table = Table(numPlayers)
    dealer = -1

    while(play):

        deck = Pile(True)
        disc = Pile()
        play = Pile()
        for player in table.players:
            player.bet = 0

        ## Deal
        dealer += 1
        if dealer >= numPlayers:
            dealer = 0
        
        deck.shuffle()

        for i in range(0, 2 * numPlayers):
            j = i + dealer
            while j >= numPlayers:
                j -= numPlayers
            table.players[j].addTop(deck.draw())

        lBlind = dealer + 1
        if lBlind >= numPlayers:
            lBlind - numPlayers
        
        bBlind = dealer + 2
        if bBlind >= numPlayers:
            bBlind - numPlayers

        print("Player {} is the dealer.".format(dealer + 1))
        print("Players {} and {} are the little and big blind, respectively.".format(lBlind + 1, bBlind + 1))
        print()

        table.players[lBlind].bet += 5
        table.players[bBlind].bet += 10
        table.checkPot()
        
        start = dealer + 3
        if start >= numPlayers:
            start -= numPlayers

        for round in range(0,4):
        
            ## Betting

            canCheck = True
            if round == 0:
                canCheck = False

            passed = 0
            
            while passed < numPlayers:
                for i in range(0, numPlayers):
                    if passed >= numPlayers:
                        continue

                    j = start + i
                    while j >= numPlayers:
                        j -= numPlayers

                    if table.players[j].isFolded:
                        passed += 1
                        continue
                    
                    print("Player {}, it's your turn.".format(j + 1))
                    print("Press enter to view your cards.")
                    input()
                    suits = [table.players[j].cards[x].suit for x in range(0,2)]
                    values = [table.players[j].cards[x].value for x in range(0,2)]
                    treat(values, suits, 2)

                    print(",-----, ,-----,")
                    print("|{:<2}   | |{:<2}   |".format(values[0], values[1]))
                    print("|  {}  | |  {}  |".format(suits[0], suits[1]))
                    print("|   {:>2}| |   {:>2}|".format(values[0], values[1]))
                    print("'-----' '-----'")
                    print()
                    print("The current bet is {}.".format(table.topBet()))
                    for x in range(0, numPlayers):
                        folded = None
                        if table.players[x].isFolded:
                            folded = "has"
                        else:
                            folded = "has not"
                        print("Player {} has bet {} and {} folded.".format(x + 1, table.players[x].bet, folded))
                    print()

                    print("How will you play?")
                    print(" 1 - Check")
                    print(" 2 - Call")
                    print(" 3 - Raise by 5")
                    print(" 4 - Raise by 10")
                    print(" 5 - Fold")
                    print()
                    choice = None

                    while choice == None:
                        try:
                            choice = int(input(" > "))
                        except ValueError:
                            print("Invalid option.")
                            continue
                            
                        if choice == 1:
                            if not canCheck:
                                print("You cannot check now.")
                                choice = None
                        elif choice == 2:
                            table.players[j].bet = table.topBet()
                            passed += 1
                        elif choice == 3:
                            table.players[j].bet = table.topBet() + 5
                            passed = 1
                        elif choice == 4:
                            table.players[j].bet = table.topBet() + 10
                            passed = 1
                        elif choice == 5:
                            table.players[j].isFolded = True
                        else:
                            print("Invalid option.")
                            choice = None
                    
                    for i in range(0, 100):
                        print()
                
            if round == 0:
                print("Here comes the flop.")
                play.addTop(deck.draw())
                play.addTop(deck.draw())
                play.addTop(deck.draw())
                suits = [play.cards[x].suit for x in range(0,3)]
                values = [play.cards[x].value for x in range(0,3)]
                treat(values, suits, 3)
                print(",-----, ,-----, ,-----, ")
                print("|{:<2}   | |{:<2}   | |{:<2}   | ".format(values[0], values[1], values[2]))
                print("|  {}  | |  {}  | |  {}  | ".format(suits[0], suits[1], suits[2]))
                print("|   {:>2}| |   {:>2}| |   {:>2}| ".format(values[0], values[1], values[2]))
                print("'-----' '-----' '-----' ")
                print("Press enter to continue.")
                input()
            elif round == 1:
                print("Here comes the turn.")
                disc.addTop(deck.draw())
                play.addTop(deck.draw())
                suits = [play.cards[x].suit for x in range(0,4)]
                values = [play.cards[x].value for x in range(0,4)]
                treat(values, suits, 4)
                print(",-----, ,-----, ,-----, ,-----,")
                print("|{:<2}   | |{:<2}   | |{:<2}   | |{:<2}   | ".format(values[0], values[1], values[2], values[3]))
                print("|  {}  | |  {}  | |  {}  | |  {}  |".format(suits[0], suits[1], suits[2], suits[3]))
                print("|   {:>2}| |   {:>2}| |   {:>2}| |   {:>2}| ".format(values[0], values[1], values[2], values[3]))
                print("'-----' '-----' '-----' '-----'")
                print("Press enter to continue.")
                input()
            else:
                print("Here comes the river.")
                disc.addTop(deck.draw())
                disc.addTop(deck.draw())
                play.addTop(deck.draw())
                suits = [play.cards[x].suit for x in range(0,5)]
                values = [play.cards[x].value for x in range(0,5)]
                treat(values, suits, 5)
                print(",-----, ,-----, ,-----, ,-----, ,-----,")
                print("|{:<2}   | |{:<2}   | |{:<2}   | |{:<2}   | |{:<2}   |".format(values[0], values[1], values[2], values[3], values[4]))
                print("|  {}  | |  {}  | |  {}  | |  {}  | |  {}  |".format(suits[0], suits[1], suits[2], suits[3], suits[4]))
                print("|   {:>2}| |   {:>2}| |   {:>2}| |   {:>2}| |   {:>2}|".format(values[0], values[1], values[2], values[3], values[4]))
                print("'-----' '-----' '-----' '-----' '-----'")
                print("Press enter to continue.")
                input()

        ## Hand Reveal

        dSuits = [play.cards[x].suit for x in range(0,5)]
        dValues = [play.cards[x].value for x in range(0,5)]
        treat(dValues, dSuits, 5)
        scores = []
        
        for x in range(0, len(table.players)):
            print("Player {}, please evaluate your hand.".format(x + 1))
            print()
            print(",-----, ,-----, ,-----, ,-----, ,-----,")
            print("|{:<2}   | |{:<2}   | |{:<2}   | |{:<2}   | |{:<2}   |".format(dValues[0], dValues[1], dValues[2], dValues[3], dValues[4]))
            print("|  {}  | |  {}  | |  {}  | |  {}  | |  {}  |".format(dSuits[0], dSuits[1], dSuits[2], dSuits[3], dSuits[4]))
            print("|   {:>2}| |   {:>2}| |   {:>2}| |   {:>2}| |   {:>2}|".format(dValues[0], dValues[1], dValues[2], dValues[3], dValues[4]))
            print("'-----' '-----' '-----' '-----' '-----'")
            suits = [table.players[x].cards[y].suit for y in range(0,2)]
            values = [table.players[x].cards[y].value for y in range(0,2)]
            treat(values, suits, 2)
            print()
            print(",-----, ,-----,")
            print("|{:<2}   | |{:<2}   |".format(values[0], values[1]))
            print("|  {}  | |  {}  |".format(suits[0], suits[1]))
            print("|   {:>2}| |   {:>2}|".format(values[0], values[1]))
            print("'-----' '-----'")
            print()
            print("Select a Trick.")
            print(" 0 - High Card")
            print(" 1 - One Pair")
            print(" 2 - Two Pair")
            print(" 4 - Three of a Kind")
            print(" 5 - Straight")
            print(" 6 - Flush")
            print(" 7 - Full House")
            print(" 8 - Four of a Kind")
            print(" 9 - Straight Flush")
            print()
            choice = None

            while choice == None:
                try:
                    choice = int(input(" > "))
                except ValueError:
                    print("Invalid Trick")
                    continue
                if choice < 0 or choice > 9:
                    choice == None
                    print("Invalid Trick")
                    continue
            
            high = 0
            for card in table.players[x].cards:
                if card.absValue() > high:
                    high = card.absValue()

            scores.append((x, choice, high))

        ## Payout

        winner = None

        for score in scores:
            if winner == None:
                winner = score
                continue
            if score[1] > winner[1]:
                winner = score
            elif score[1] == winner[1] and score[2] > winner[2]:
                winner = score

        table.checkPot()
        print("Player {} has won {} chips.".format(winner[0] + 1, table.pot))
        
        table.payout(winner[0])

        ## New Game

        choice = None
        while (choice == None):
            print("Play again? (y/n)")
            choice = input(" > ")
            if choice == "n" or choice == "N":
                play = False
            elif choice != "y" or choice != "Y":
                choice = None
                print('Invalid response. Please respond with "y" or "n" only.')
