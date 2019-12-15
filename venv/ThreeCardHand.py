from Deck import Deck
from Card import Card
from PokerHand import PokerHand

class ThreeCardHand:

    def __init__(self):

        self.currentHand = []
        self.numberOfCards = 0
        self.high = 1
        self.low = 1
        self.freq = dict()
        self.totalCardsPossible = 3
        self.finalStyle = None

    def addCard(self, card):

        if self.numberOfCards < self.totalCardsPossible:
            self.currentHand.append(card)
            self.numberOfCards += 1
        else:
            raise Exception("Hand Full.")


    def removeCard(self, card):

        self.currentHand.remove(card)
        self.numberOfCards -= 1

    def reset(self):
        self.high = 1
        self.low = 1
        self.freq = dict()


    def hasHighCard(self):

        self.reset()
        self.lineUp()

        for key in self.freq:
            if self.freq[key] != 0 and key > self.high:
                self.low = self.high
                self.high = key

        return PokerHand("High Card", self.high, self.low)


    def findRemainingHighest(self, previousNumber):

        # Loop through and if any are not the high value but are better than before then use.

        self.freq[self.high] = 0

        for key in self.freq:
            if self.freq[key] != 0 and key > self.low:
                self.low = key

        self.freq[self.high] == previousNumber


    def hasOnePair(self):

        hasPair = False
        self.reset()
        self.lineUp()

        # Check if any of them have value 2 and if higher than the previous, allow to loop as could be two pairs so need the higher.

        for val in self.freq:
            if self.freq[val] == 2 and val > self.high:
                hasPair = True
                self.high = val

        if hasPair:
            self.findRemainingHighest(2)
            return PokerHand("One Pair", self.high, self.low)
        else:
            return None


    def hasThreeOfKind(self):

        # If just 3 cards then check they are all the same.
        hasThreeOfKind = False
        self.reset()
        self.lineUp()

        for val in self.freq: #Can't have two triples.
            if self.freq[val] == 3:
                hasThreeOfKind = True
                self.high = val

        if hasThreeOfKind:
            self.findRemainingHighest(3)
            return PokerHand("Three of a Kind", self.high, self.low)
        else:
            return None


    def lineUp(self):

        for val in [2,3,4,5,6,7,7,8,9,10,11,12,13,14]:

            occurances = 0

            for cards in self.currentHand:
                if cards.getNumericValue() == val:
                    occurances += 1

            self.freq[val] = occurances


    def findHandType(self):

        best = None

        if self.hasHighCard() is not None:
            best = self.hasHighCard()

        if self.hasOnePair() is not None:
            best = self.hasOnePair()

        if self.hasThreeOfKind() is not None:
            best = self.hasThreeOfKind()

        return best


    def evaluateHand(self, handID = "Front"):

        # First get the details of the hand.
        # Royalities as on the wiki page.

        handType = self.findHandType()

        if handType.style == "High Card":
            return 0
        elif handType.style == "One Pair":
            points = handType.high - 5
            if points > 0:
                return points
            else:
                return 0
        elif handType.style == "Three of a Kind":
            points = handType.high + 8
            return points
        else:
            return 0

    def compareRow(self, secondHand):
        # Return 1 is Hand 1 is better, 0 if equal and -1 if hand 2 is better.
        # Possible to uniquely identify every hand just using style / high / low.

        ###
        # However this might not be possible for the 5 card, think about a way to encode card hands.
        # 100000 * style rating  + 1000 * high rating + 10 * low rating. + 0.5 * remaining value. ???
        ###


        handOneType = self.findHandType()
        handTwoType = secondHand.findHandType()
        print(handOneType.style)
        print(handTwoType.style)

        handDictionary = {"High Card": 1, "One Pair": 2, "Three of a Kind": 3}
        print(handDictionary[handOneType.style] > handDictionary[handTwoType.style])

        try:
            if handDictionary[handOneType.style] > handDictionary[handTwoType.style]:
                return 1
            elif handDictionary[handOneType.style] < handDictionary[handTwoType.style]:
                return -1
            else:
                # Equal hands so need to compare by high and low term.
                if handOneType.high > handTwoType.high:
                    return 1
                elif handOneType.high < handTwoType.high:
                    return -1
                else:
                    if handOneType.low > handTwoType.low:
                        return 1
                    elif handOneType.low < handTwoType.low:
                        return -1
                    else:
                        return 0 # All equal in terms of 3 card hand, as can only have high/low and no devivation.

        except Exception:
            # To catch some weird error happening with the type of card not being recorded correctly.
            print("Dunno - error with recording of hand.")




if  __name__ == "__main__":

    print("Starting\n")
    c = Deck()
    c.createNewFullDeck()

    # deal = c.dealFiveCards()
    # t = ThreeCardHand()
    # t.currentHand = deal
    # print(t.lineUp())
    # #print(t.hasHighCard().high)
    # re = t.hasOnePair()
    # if re is not None:
    #     print(re.high)
    #     print(re.low)

    #print(isinstance(c, Deck))
    t = ThreeCardHand()
    s = ThreeCardHand()

    t.currentHand = [Card("Spade", "8"), Card("Diamond", "7"), Card("Spade", "7")]
    s.currentHand = [Card("Spade", "9"), Card("Diamond", "9"), Card("Diamond", "2")]

    print(t.evaluateHand("Front"))
    print(s.evaluateHand("Front"))
    print(t.compareRow(s))


















