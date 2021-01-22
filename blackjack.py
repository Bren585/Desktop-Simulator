from pieces import *
from poker import treat

def showHand(player, dealer, hide = True):
    pSuits = [player.cards[i].suit for i in range(0, len(player.cards))]
    pValues = [player.cards[i].value for i in range(0, len(player.cards))]
    treat(pValues, pSuits, len(player.cards))
    dSuits = [dealer.cards[i].suit for i in range(0, len(dealer.cards))]
    dValues = [dealer.cards[i].value for i in range(0, len(dealer.cards))]
    treat(dValues, dSuits, len(dealer.cards))

    out = ""
    for i in range(0, len(dealer.cards)):
        out += ",-----, "
    print(out)
    out = ""
    for i in range(0, len(dealer.cards)):
        if not (i == 1 and hide):
            out += "|{:<2}   | ".format(dValues[i])
        else:
            out += "|     | "
    print(out)
    out = ""
    for i in range(0, len(dealer.cards)):
        if not (i == 1 and hide):
            out += "|  {}  | ".format(dSuits[i])
        else:
            out += "|     | "
    print(out)
    out = ""
    for i in range(0, len(dealer.cards)):
        if not (i == 1 and hide):
            out += "|   {:>2}| ".format(dValues[i])
        else:
            out += "|     | "
    print(out)
    out = ""
    for i in range(0, len(dealer.cards)):
        out += "'-----' "
    print(out)
    if not hide:
        return
    out = ""
    print()
    for i in range(0, len(player.cards)):
        out += ",-----, "
    print(out)
    out = ""
    for i in range(0, len(player.cards)):
        out += "|{:<2}   | ".format(pValues[i])
    print(out)
    out = ""
    for i in range(0, len(player.cards)):
        out += "|  {}  | ".format(pSuits[i])
    print(out)
    out = ""
    for i in range(0, len(player.cards)):
        out += "|   {:>2}| ".format(pValues[i])
    print(out)
    out = ""
    for i in range(0, len(player.cards)):
        out += "'-----' "
    print(out)
    out = ""


def sumPile(p):
    total = 0
    for card in p.cards:
        if card.value > 1 and card.value < 11:
            total += card.value
        elif card.value > 10:
            total += 10
        elif card.value == 1:
            if total >= 11:
                total += 1
            else:
                total += 11
    return total

def Blackjack(numPlayers):
    players = []
    for i in range(0, numPlayers):
        players.append(Player())
    
    dealer = Player()

    deck = Pile(True)
    deck.shuffle()

    for player in players:
        player.addTop(deck.draw())
        player.addTop(deck.draw())
    
    dealer.addTop(deck.draw())
    dealer.addTop(deck.draw())

    turn = 1
    for player in players:
        print("Player {}, it's your turn.".format(turn))
        turn += 1
        print("Press enter to continue.")
        input()

        stand = False
        blackjack = True
        while not stand:
            showHand(player, dealer)
            print("Your current total is {}.".format(sumPile(player)))
            print()

            if sumPile(player) == 21 and blackjack:
                print("You got a blackjack.")
                print()
                stand = True
                continue
            else:
                blackjack = False

            if sumPile(player) > 21:
                print("You busted.")
                print()
                stand = True
                continue

            print("How will you play?")
            print(" 1 - Hit")
            print(" 2 - Stand")
            print()

            choice = None
            while choice == None:
                try:
                    choice = int(input(" > "))
                except ValueError:
                    print("Invalid option.")
                    continue
                if choice == 1:
                    player.addTop(deck.draw())
                elif choice == 2:
                    print("You stood at {}.".format(sumPile(player)))
                    print()
                    stand = True
                else:
                    print("Invalid option.")
                    choice = None

    print("Press enter to continue.")
    input()
    print("It's the dealer's turn.")
    print()
    stand = False
    blackjack = True
    while not stand:
        showHand(players[0], dealer, False)
        print()

        if sumPile(dealer) == 21 and blackjack:
            print("The dealer got a blackjack.")
            stand = True
            continue
        else:
            blackjack = False
        
        if sumPile(dealer) > 21:
            print("The dealer busts.")
            stand = True
        elif sumPile(dealer) >= 17:
            print("The dealer stands at {}.".format(sumPile(dealer)))
            stand = True
        else:
            print("The dealer hits at {}.".format(sumPile(dealer)))
            dealer.addTop(deck.draw())
        print("Press enter to continue.")
        input()
    
    dScore = sumPile(dealer)
    if dScore > 21:
        dScore = 0
    
    scores = [sumPile(players[i]) for i in range(0, numPlayers)]
    for x in range(0, numPlayers):
        if scores[x] > 21:
            scores[x] = 0
    
    print()
    player = 0
    for score in scores:
        player += 1
        if score > dScore:
            print("Player {} beat the dealer with a score of {}.".format(player, score))
        else:
            print("Player {} lost to the dealer with a score of {}.".format(player, score))
            print()
    
    print("Press enter to return to game selection.")
    input()
    

