from pieces import *

def warn():
    print("This will result in a score of Zero. Score anyway? (y/n)")
    print()
    choice = None
    while True:
        choice = input(" > ")
        print()
        if choice == "y" or choice == "Y":
            return True
        elif choice == "n" or choice == "N":
            return False
        else:
            print("Invalid input. Respond with 'y' or 'n.'")
            print()


def Yahtzee(numPlayers):
    players = [(yahtzeeSS(), i) for i in range(1, numPlayers + 1)]

    dice = [[Die(), True] for i in range(0, 6)]

    ## Gameplay

    for turn in range(0, 13):
        for player in players:
            print("Player {}, it's your turn.".format(player[1]))
            print("Press enter to continue.")
            input()

            player[0].display()
            print()

            ## Rolling

            for die in dice:
                die[1] = True

            for round in range(1,4):
                for die in dice:
                    if die[1]:
                        die[0].roll()

                print("Roll {}".format(round))
                print(",-1-,-2-,-3-,-4-,-5-,")
                print("| {} | {} | {} | {} | {} |".format(dice[0][0].value, dice[1][0].value, dice[2][0].value, dice[3][0].value, dice[4][0].value))
                print("'-{}-'-{}-'-{}-'-{}-'-{}-'".format(int(dice[0][1]), int(dice[1][1]), int(dice[2][1]), int(dice[3][1]), int(dice[4][1])))
                print()
                if round != 3:
                    choice = None
                    print("If you would like to toggle a die, enter it's number. If you wish to proceed, type 0.")
                    print("(A locked die will have a 0 underneath it. An unlocked die will have a 1 underneath.)")
                    while choice != 0:
                        try:
                            choice = int(input(" > "))
                        except ValueError:
                            print("That's not a valid die. Please try again.")
                            continue

                        if choice == 0:
                            pass
                        elif choice < 6 and choice > 0:
                            dice[choice - 1][1] = not dice[choice - 1][1]
                        else:
                            print("That's not a valid die. Please try again.")
                        print()
                else:
                    print("Press enter to continue.")
                    input()
            
            ## Scoring

            scored = False
            choice = None

            while not scored:
                player[0].display()
                print()
                print("How would you like to score?")
                print(" 01 - Aces")
                print(" 02 - Twos")
                print(" 03 - Threes")
                print(" 04 - Fours")
                print(" 05 - Fives")
                print(" 06 - Sixes")
                print(" 11 - Three of a Kind")
                print(" 12 - Four of a Kind")
                print(" 13 - Full House")
                print(" 14 - Small Straight")
                print(" 15 - Large Straight")
                print(" 77 - Chance")
                print(" 99 - Yahtzee")
                print()
                try:
                    choice = int(input(" > "))
                except ValueError:
                    print("Invalid category.")
                    print()
                    continue


                print()

                score = 0
                if choice == 1:                      ## Aces
                    if player[0].upper[0] != None:
                        print("This category is already full.")
                        print()
                    for die in dice:
                        if die[0].value == 1:
                            score += 1
                    if score == 0:
                        if not warn():
                            continue
                    player[0].upper[0] = score
                    scored = True

                elif choice == 2:                   ## Twos
                    if player[0].upper[1] != None:
                        print("This category is already full.")
                        print()
                    for die in dice:
                        if die[0].value == 2:
                            score += 2
                    if score == 0:
                        if not warn():
                            continue
                    player[0].upper[1] = score
                    scored = True

                elif choice == 3:                   ## Threes
                    if player[0].upper[2] != None:
                        print("This category is already full.")
                        print()
                    for die in dice:
                        if die[0].value == 3:
                            score += 3
                    if score == 0:
                        if not warn():
                            continue
                    player[0].upper[2] = score
                    scored = True

                elif choice == 4:                   ## Fours
                    if player[0].upper[3] != None:
                        print("This category is already full.")
                        print()
                    for die in dice:
                        if die[0].value == 4:
                            score += 4
                    if score == 0:
                        if not warn():
                            continue
                    player[0].upper[3] = score
                    scored = True

                elif choice == 5:                   ## Fives
                    if player[0].upper[4] != None:
                        print("This category is already full.")
                        print()
                    for die in dice:
                        if die[0].value == 5:
                            score += 5
                    if score == 0:
                        if not warn():
                            continue
                    player[0].upper[4] = score
                    scored = True

                elif choice == 6:                   ## Sixes
                    if player[0].upper[5] != None:
                        print("This category is already full.")
                        print()
                    for die in dice:
                        if die[0].value == 3:
                            score += 3
                    if score == 0:
                        if not warn():
                            continue
                    player[0].upper[5] = score
                    scored = True
                
                elif choice == 11:                  ## Three of a Kind
                    if player[0].threeKind != None:
                        print("This category is already full.")
                        print()
                    values = [dice[i][0].value for i in range(0,5)]
                    for value in values:
                        if values.count(value) >= 3:
                            score = sum(values)
                    if score == 0:
                        if not warn():
                            continue
                    player[0].threeKind = score
                    scored = True
                
                elif choice == 12:                  ## Four of a Kind
                    if player[0].fourKind != None:
                        print("This category is already full.")
                        print()
                    values = [dice[i][0].value for i in range(0,5)]
                    for value in values:
                        if values.count(value) >= 4:
                            score = sum(values)
                    if score == 0:
                        if not warn():
                            continue
                    player[0].fourKind = score
                    scored = True
                elif choice == 13:                  ## Full House
                    if player[0].fullHouse != None:
                        print("This category is already full.")
                        print()
                    values = [dice[i][0].value for i in range(0,5)]
                    two = False
                    three = False
                    for value in values:
                        if values.count(value) == 3:
                            three = True
                        elif values.count(value) == 2:
                            two = True
                    if two and three:
                        score = 25
                    if score == 0:
                        if not warn():
                            continue
                    player[0].fullHouse = score
                    scored = True

                elif choice == 14:                  ## Small Straight
                    if player[0].sStraight != None:
                        print("This category is already full.")
                        print()
                    values = [dice[i][0].value for i in range(0,5)]
                    values.sort()
                    high = 1
                    streak = 1
                    prev = None
                    for value in values:
                        if prev == None:
                            prev = value
                        elif prev + 1 == value:
                            streak += 1
                            prev = value
                            if streak > high:
                                high = streak
                        elif prev != value:
                            streak = 1
                    if high >= 4:
                        score = 30
                    if score == 0:
                        if not warn():
                            continue
                    player[0].sStraight = score
                    scored = True

                elif choice == 15:                  ## Large Straight
                    if player[0].lStraight != None:
                        print("This category is already full.")
                        print()
                    values = [dice[i][0].value for i in range(0,5)]
                    values.sort()
                    high = 1
                    streak = 1
                    prev = None
                    for value in values:
                        if prev == None:
                            prev = value
                        elif prev + 1 == value:
                            streak += 1
                            prev = value
                            if streak > high:
                                high = streak
                        elif prev != value:
                            streak = 1
                    if high >= 5:
                        score = 40
                    if score == 0:
                        if not warn():
                            continue
                    player[0].lStraight = score
                    scored = True

                elif choice == 77:                  ## Chance
                    if player[0].chance != None:
                        print("This category is already full.")
                        print()
                    values = [dice[i][0].value for i in range(0,5)]
                    score = sum(values)
                    if score == 0:
                        if not warn():
                            continue
                    player[0].chance = score
                    scored = True

                elif choice == 99:                  ## Yahtzee
                    if player[0].yahtzee != None:
                        print("This category is already full.")
                        print()
                    values = [dice[i][0].value for i in range(0,5)]
                    if values.count(values[0]) == 5:
                        score = 50
                    if score == 0:
                        if not warn():
                            continue
                    player[0].yahtzee = score
                    scored = True

                else:
                    print("Invalid category.")
                    print()
            
            if turn == 12:
                print("Player {}, your final score is {}.".format(player[1], player[0].total()))
                player[0].display()
                print("Press enter to continue.")
                input()

    winner = None  
    for player in players:
        if winner == None:
            winner = player
            continue
        if player[0].total() > winner[0].total():
            winner = player

    print()
    print("And the winner is...!")
    print("Player {}! With {} points. Congratulations!")
    print("Press enter to return to game selection.")
    input()



