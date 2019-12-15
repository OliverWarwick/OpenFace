from Deck import Deck
from Card import Card
from PokerHand import PokerHand

class ThreeCardHand:

    def __init__(self):

        self.currentHand = []
        self.numberOfCards = 0
        self.high = 1
        self.low = 1
        self.importantCards = []
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
        self.importantCards = []


    def hasHighCard(self):

        self.reset()
        self.lineUp()

        # If the hand just has a high card then just record all the cards which are present, order then and these
        # are the important cards.

        for key in self.freq:
            for i in range(0,self.freq[key]): # Add the number of times this occurs.
                self.importantCards.append(key)

        self.importantCards.sort(reverse=True)

        return PokerHand("High Card", self.importantCards)


    def hasOnePair(self):

        hasPair = False
        self.reset()
        self.lineUp()

        # First check if there is a card which appears twice.

        for val in self.freq:
            if self.freq[val] == 2:
                hasPair = True
                self.importantCards.append(val)
        self.importantCards.sort(reverse=True)

        if hasPair: # Then loop through again to find the remaining card.
            extraCards = []
            for val in self.freq:
                if val not in self.importantCards: # So check its not the card we are considering, and then add in.
                    for i in range(0, self.freq[val]):
                        extraCards.append(val) # No need to sort the list now, as pair is given prescidence.
            extraCards.sort(reverse=True)

            return PokerHand("One Pair", self.importantCards + extraCards)
        else:
            return None


    def hasThreeOfKind(self):

        # If just 3 cards then check they are all the same.
        hasThreeOfKind = False
        self.reset()
        self.lineUp()

        for val in self.freq: # Can't have two triples.
            if self.freq[val] == 3:
                hasThreeOfKind = True
                self.importantCards.append(val)

        if hasThreeOfKind:  # Then loop through again to find the remaining card.
            extraCards = []
            for val in self.freq:
                if val not in self.importantCards:
                    for i in range(0, self.freq[val]):
                        extraCards.append(val)  # No need to sort the list now, as pair is given prescidence.
            extraCards.sort(reverse=True)
            return PokerHand("Three of a Kind", self.importantCards + extraCards)
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

        # Also included the other card types for the 5 card checks.
        handDictionary = {"High Card": 1, "One Pair": 2, "Two Pair": 3, "Three of a Kind": 4, "Straight": 5, "Flush": 6,
                          "Full House": 7, "Four of a Kind": 8, "Straight Flush": 9, "Royal Flush": 10}

        try:
            # First check if there is a clear winner, if not then we have to break it down to the cards themselves.
            if handDictionary[handOneType.style] > handDictionary[handTwoType.style]:
                return 1
            elif handDictionary[handOneType.style] < handDictionary[handTwoType.style]:
                return -1
            else:
                # Now they have the same style, so we can cycle through the cards checking at each stage.
                for i in range(0, min(len(handOneType.importantCards), len(handTwoType.importantCards))):
                    if handOneType.importantCards[i] > handTwoType.importantCards[i]:
                        return 1
                    if handOneType.importantCards[i] < handTwoType.importantCards[i]:
                        return -1

                # Having reached the end of this the hands must be exactly equal, hence return 0
                return 0

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


















