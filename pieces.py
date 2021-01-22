import random
random.seed()

## General Tabletop Pieces

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def absValue(self):
        return self.suit * 13 + self.value

class Pile: 
    def __init__(self, isDeck = False):
        self.cards = []
        if isDeck:
            for v in range(1, 14):
                for s in range(0, 4):
                    self.cards.append(Card(s, v))
    
    def addTop(self, card):
        self.cards.append(card)

    def draw(self):
        return self.cards.pop()

    def pick(self, i):
        return self.cards.pop(i)

    def shuffle(self):
        hold = []
        for i in range(0, len(self.cards)):
            hold.append(self.cards.pop(random.randrange(0, len(self.cards))))
        self.cards = hold


class Die:
    def __init__(self, max = 6):
        self.max = max
        self.value = 0

    def roll(self):
        self.value = random.randrange(1, self.max + 1)

class Player(Pile):
    def __init__(self, startingChips = 0):
        Pile.__init__(self, False)
        self.chips = startingChips
        self.bet = 0
        self.isFolded = False
    
    def play(self, i):
        return self.pick(i)

## Poker    

class Table:
    def __init__(self, numPlayers, startingChips = 100):
        self.players = [Player(startingChips) for i in range(0, numPlayers)]
        self.pot = 0

    def checkPot(self):
        self.pot = 0
        for player in self.players:
            self.pot += player.bet

    def payout(self, winner):
        winnings = 0
        for player in self.players:
            player.chips -= player.bet
            winnings += player.bet
            player.bet = 0
        self.players[winner].chips += winnings
    
    def topBet(self):
        top = 0
        for player in self.players:
            if player.bet > top:
                top = player.bet
        return top


## Yahtzee

class yahtzeeSS: ## Score Sheet
    def __init__(self):
        ## Upper Half
        self.upper = [None for i in range(0,6)]
        ## Lower Half
        self.threeKind  = None
        self.fourKind   = None
        self.fullHouse  = None
        self.sStraight  = None
        self.lStraight  = None
        self.chance     = None
        self.yahtzee    = None
    
    def upperSum(self):
        total = 0
        for x in self.upper:
            if x != None:
                total += x
        return total

    def total(self):
        total = self.upperSum()

        if total >= 63:
            total += 35
        
        if self.threeKind != None:
            total += self.threeKind
        if self.fourKind != None:
            total += self.fourKind
        if self.fullHouse != None:
            total += self.fullHouse
        if self.sStraight != None:
            total += self.sStraight
        if self.lStraight != None:
            total += self.lStraight
        if self.chance != None:
            total += self.chance
        if self.yahtzee != None:
            total += self.yahtzee 

        return total

    def display(self):
        bonus = None
        if self.upperSum() >= 63:
            bonus = 35

        print(",------------Score Card------------,")
        print("| Upper Half                       |")
        print("}-----------------,----------------{")
        print("| Aces            | {:<14} |".format(str(self.upper[0])))
        print("| Twos            | {:<14} |".format(str(self.upper[1])))
        print("| Threes          | {:<14} |".format(str(self.upper[2])))
        print("| Fours           | {:<14} |".format(str(self.upper[3])))
        print("| Fives           | {:<14} |".format(str(self.upper[4])))
        print("| Sixes           | {:<14} |".format(str(self.upper[5])))
        print("| Bonus           | {:<14} |".format(str(bonus)))
        print("}-----------------'----------------{")
        print("| Lower Half                       |")
        print("}-----------------,----------------{")
        print("| Three of a Kind | {:<14} |".format(str(self.threeKind)))
        print("| Four of a Kind  | {:<14} |".format(str(self.fourKind)))
        print("| Full House      | {:<14} |".format(str(self.fullHouse)))
        print("| Small Straight  | {:<14} |".format(str(self.sStraight)))
        print("| Large Straight  | {:<14} |".format(str(self.lStraight)))
        print("| Chance          | {:<14} |".format(str(self.chance)))
        print("| Yahtzee         | {:<14} |".format(str(self.yahtzee)))
        print("}-----------------+----------------{")
        print("| Total           | {:<14} |".format(self.total()))
        print("'-----------------'----------------'")
