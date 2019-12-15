# 5 card hand for the back and middle rows
# Take from three card hand and increase the functionality.

from ThreeCardHand import ThreeCardHand
from Card import Card
from Deck import Deck
from PokerHand import PokerHand

class FiveCardHand(ThreeCardHand):

    def __init__(self):
        super(FiveCardHand, self).__init__()
        self.totalCardsPossible = 5

    def hasTwoPair(self):

        hasTwoPair = False
        self.reset()
        self.lineUp()

        # Find a list of all pairs, and from there easy to do high and low.

        pairsList = set()

        for val in self.freq:
            if self.freq[val] == 2:
                pairsList.add(val)

        if len(pairsList) == 2:
            hasTwoPair = True

        # High represents the high pairs and low the lower of the two.

        if hasTwoPair == True:
            self.high = max(pairsList)
            self.low = min(pairsList)
            return PokerHand("Two Pair", self.high, self.low)
        else:
            return None


    def hasFullHouse(self):

        # First check if it has a triple, and then check if it has a pair.
        # High for the triple and low for the pair.

        self.reset()
        self.lineUp()

        threes = self.hasThreeOfKind()
        twos = self.hasOnePair()

        if (threes is not None) and (twos is not None):
            return PokerHand("Full House", threes.high, twos.high)
        else:
            return None

    def hasFourOfKind(self):

        self.reset()
        self.lineUp()
        hasFourOfKind = False

        for val in self.freq:
            if self.freq[val] == 4:
                hasFourOfKind = True
                self.high = val  #Can't have more than one four of kind.

        if hasFourOfKind:
            # Find the remaining card
            self.findRemainingHighest(4)
            return PokerHand("Four of a Kind", self.high, self.low)
        else:
            return None

    def checkSuitsSame(self):

        try:
            suitInQuestion = self.currentHand[0].suit
            for card in self.currentHand:
                if suitInQuestion is not card.suit:
                    return False
            return True

        except Exception:
            return False

    def checkValuesInOrder(self):

        # Set up an array to store the numbers of the cards
        values = []

        # Get the numeric values of the cards.
        for card in self.currentHand:
            values.append(card.getNumericValue())

        if len(values) == 0 or len(values) == 1:
            return True
        else:
            values.sort()
            for i in range(0,len(values)-1):
                if values[i+1] - values[i] != 1:
                    return False
            return True


    def hasFlush(self):

        self.reset()
        self.lineUp()

        if self.checkSuitsSame() and self.numberOfCards == 5:
            # Then need to find the highest, and then the second highest.

            for val in self.freq:
                if self.freq[val] > 0 and val > self.high:
                    self.high = val

            #Once finished, remove then call the remaining routine.

            self.findRemainingHighest(1)
            return PokerHand("Flush", self.high, self.low)
        else:
            return None


    def hasStraight(self):

        self.reset()
        self.lineUp()

        valuesOfCards = set()

        for card in self.currentHand:
            valuesOfCards.add(card.getNumericValue())

        if len(valuesOfCards) == 5:

            valuesOfCards = list(valuesOfCards)

            #Auto orders these so can just check each diff by one.
            for i in range(0,4):
                if valuesOfCards[i] + 1 != valuesOfCards[i+1]:
                    return None

            # If not then this is true, and can return the last element.
            return PokerHand("Straight", valuesOfCards[4])

        return None



    def hasStraightFlush(self):

        self.reset()
        self.lineUp()

        st = self.hasStraight()
        fl = self.hasFlush()

        if st is not None and fl is not None:
            # Find high value
            return PokerHand("Straight Flush", st.high)
        else:
            return None

    def hasRoyalFlush(self):

        self.reset()
        self.lineUp()

        stfl = self.hasStraightFlush()

        if (stfl is not None) and (stfl.high == 14):
            return PokerHand("Royal Flush", 14)
        else:
            return None


    def findHandType(self):

        # Find the best poker hand which is contained in this hand.

        best = None

        if self.hasHighCard() is not None:
            best = self.hasHighCard()
        if self.hasOnePair() is not None:
            best = self.hasOnePair()
        if self.hasTwoPair() is not None:
            best = self.hasTwoPair()
        if self.hasThreeOfKind() is not None:
            best = self.hasThreeOfKind()
        if self.hasStraight() is not None:
            best = self.hasStraight()
        if self.hasFlush() is not None:
            best = self.hasFlush()
        if self.hasFullHouse() is not None:
            best = self.hasFullHouse()
        if self.hasFourOfKind() is not None:
            best = self.hasFourOfKind()
        if self.hasStraightFlush() is not None:
            best = self.hasStraightFlush()
        if self.hasRoyalFlush() is not None:
            best = self.hasRoyalFlush()

        return best


    def evaluateHand(self, handID):

        # Find the hand style, and recover the details.
        backDictOfPoints = {("Straight", 2), ("Flush", 4), ("Full House", 6), ("Four of a Kind", 10), ("Straight Flush", 15), ("Royal Flush", 25)}
        middleDictOfPoints = {("Three of a Kind", 2), ("Straight", 4), ("Flush", 8), ("Full House", 12), ("Four of a Kind", 20), ("Straight Flush", 30), ("Royal Flush", 50)}

        handType = self.findHandType()
        print(handID + ":  " + handType.style)

        if handID == "Back":
            try:
                return backDictOfPoints[handType.style]
            except Exception:
                return 0
        else:
            try:
                return middleDictOfPoints[handType.style]
            except Exception:
                return 0











if  __name__ == "__main__":

    print("He;;p")
    f = FiveCardHand()
    f.currentHand = [Card("Spade", "10"), Card("Spade", "Jack"), Card("Spade", "Queen"), Card("Spade", "King"),
                         Card("Spade", "Ace")]



    # r = f.hasFourOfKind()
    # print(r.high)
    # print(r.low)
    # print(f.hasFlush())
    r = f.hasTwoPair()
    #print(r)
    print(f.scoreRoyalitiesPoints("back"))
    # print(r.low)





