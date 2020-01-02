import math
from Card import Card

def nCr(n,r):
    f = math.factorial
    try:
        return f(n) / f(r) / f(n-r)
    except Exception:
        return 0

def numberOfCardsByValueInDeck(ownHand, oppoHand, cardValue):

    # Should be able to add up the number of that card in both hands.
    # Card value is the string rep ie: "Jack", "7".
    # Want to also check our discard pile.

    total = 4
    handList = [ownHand.front, ownHand.middle, ownHand.back, ownHand.discardPile, oppoHand.front, oppoHand.middle,
                oppoHand.back]

    for hand in handList:
        for card in hand.currentHand:
            if card.value == cardValue:
                total -= 1
    #print("Number of " + cardValue + " which are left in the deck: "+ str(total))
    return total

def numberOfCardsBySuitInDeck(ownHand, oppoHand, cardSuit):

    total = 13
    handList = [ownHand.front, ownHand.middle, ownHand.back, ownHand.discardPile, oppoHand.front, oppoHand.middle,
                oppoHand.back]

    for hand in handList:
        for card in hand.currentHand:
            if card.suit == cardSuit:
                total -= 1
    #print("Number of " + cardSuit + " which are left in the deck: "+ str(total))
    return total


def numberOfCardsValueInHand(hand, card):

    total = 0
    for c in hand.currentHand:
        if c.value == card.value:
            total += 1
    return total

def numberOfCardsSuitInHand(hand, card):

    total = 0
    for c in hand.currentHand:
        if c.suit == card.suit:
            total += 1
    return total


def convertHandTypeToRanking(handStyle):

    converter = {("High Card", 1), ("One Pair", 2), ("Two Pair", 3), ("Three of a Kind", 4), ("Straight", 5),
                 ("Flush", 6), ("Full House", 7), ("Straight Flush", 8), ("Four of a Kind", 9), ("Royal Flush", 10)}

    try:
        return converter[handStyle]
    except Exception:
        return 0


# Function to get the expected score of completing a hand, just given the card value and the style
# highCard - Integer 2->2, 10->10, Jack->11
# handStyle - String which is the normal style "One Pair", "Two Pair" etc
# handInQuestion - String again just "Front" ...

def computeExpectedRoyality(highCard, handStyle, handInQuestion):

    if handInQuestion == "Front":

        if handStyle == "One Pair":
            points = highCard - 5
            if points > 0:
                return points
            else:
                return 0

        if handStyle == "Three of a Kind":
            points = highCard + 8
            return points


    elif handInQuestion == "Middle":
        middleDictOfPoints = {"Three of a Kind": 2, "Straight": 4, "Flush": 8, "Full House": 12,
                              "Four of a Kind": 20, "Straight Flush": 30, "Royal Flush": 50}
        try:
            return middleDictOfPoints[handStyle]
        except Exception:
            return 0
    else:
        backDictOfPoints = {"Straight": 2, "Flush": 4, "Full House": 6, "Four of a Kind": 10,
                            "Straight Flush": 15, "Royal Flush": 25}
        try:
            return backDictOfPoints[handStyle]
        except Exception:
            return 0







# ownHand: Players Hand
# oppoHand: Players Hand
# handInQuestion: ThreeCardHand or FiveCardHand
# deck: Deck
# card: Card
# numberOfCardsInCollection: int

# Here collection refers to Pair, Three of Kind, Four of Kind, just specify how many needed.
def probOfCollectionOfCard(ownHand, oppoHand, handInQuestion, deck, card, numberOfCardsInCollection = 2):

    # Create the freq of the cards in the hand.
    handInQuestion.lineUp()

    # Check the number of cards of value the same as the card. If greater then 2 then already have a pair, so return 1.
    try:
        numberOfCardInHand = handInQuestion.freq.get(card.getNumericValue())
        if numberOfCardInHand >= numberOfCardsInCollection:
            return 1
    except Exception:
        print("Error in identifying hand.")

    numberOfThatCardLeftInDeck = numberOfCardsByValueInDeck(ownHand, oppoHand, card.value)
    numberOfCardsNeeded = numberOfCardsInCollection - numberOfCardsValueInHand(handInQuestion, card)
    numberOfCardsInDeck = deck.numberOfCards
    numberOfCardsLeftToDeal = ownHand.numberOfCardsLeftToBeDealt

    # If we did not return from previous then no pair at the moment, so if hand is full or not enough cards to make it,
    # Then should return 0

    if (numberOfCardsNeeded > numberOfThatCardLeftInDeck) or (handInQuestion.numberOfCards + numberOfCardsNeeded > handInQuestion.totalCardsPossible):
        return 0
    else:
        waysToDo = nCr(numberOfThatCardLeftInDeck, numberOfCardsNeeded) * nCr(numberOfCardsInDeck-numberOfThatCardLeftInDeck, numberOfCardsLeftToDeal-numberOfCardsNeeded)
        totalWays = nCr(numberOfCardsInDeck, numberOfCardsLeftToDeal)
        return round(waysToDo / totalWays, 6)


# This requires the extra parameters of the card wanted to use for the triple, and the card wanted for the double.
# cardForTriple of type Card
def probOfFullHouse(ownHand, oppoHand, handInQuestion, deck, cardForTriple, cardForDouble):

    # Get the lineup
    handInQuestion.lineUp()

    # If we have too many cards then return 0 as we can't make a full hosue.
    if probOfCollectionOfCard(ownHand,oppoHand,handInQuestion,deck,cardForTriple,4) == 1 or probOfCollectionOfCard(ownHand,oppoHand,handInQuestion,deck,cardForDouble,3) == 1:
        return 0

    doubleComplete = handInQuestion.freq.get(cardForDouble.getNumericValue()) == 2
    tripleComplete = handInQuestion.freq.get(cardForTriple.getNumericValue()) == 3

    # If we have completed the double, then we just need the chance of completing the triple.
    if doubleComplete:
        return probOfCollectionOfCard(ownHand,oppoHand,handInQuestion,deck,cardForTriple,3)
    elif tripleComplete:
        return probOfCollectionOfCard(ownHand,oppoHand,handInQuestion,deck,cardForDouble,2)
    else:

        # This is the slightly more tricky case as we need to think that out of the remaining cards we need
        # x many of card A, and y many of card B.

        numberOfDoubleCardLeftInDeck = numberOfCardsByValueInDeck(ownHand, oppoHand, cardForDouble.value)
        numberOfTripleCardLeftInDeck = numberOfCardsByValueInDeck(ownHand, oppoHand, cardForTriple.value)

        numberOfDoubleCardsNeeded = 2 - numberOfCardsValueInHand(handInQuestion, cardForDouble)
        numberOfTripleCardsNeeded = 3 - numberOfCardsValueInHand(handInQuestion, cardForTriple)

        numberOfCardsInDeck = deck.numberOfCards
        numberOfCardsLeftToDeal = ownHand.numberOfCardsLeftToBeDealt

        # So here we need so many of Double attempt, and then
        waysToPickDoubles = nCr(numberOfDoubleCardLeftInDeck, numberOfDoubleCardsNeeded)
        waysToPickTriples = nCr(numberOfTripleCardLeftInDeck, numberOfTripleCardsNeeded)
        waysToPickOthers = nCr((numberOfCardsInDeck - numberOfTripleCardLeftInDeck - numberOfDoubleCardLeftInDeck), (numberOfCardsLeftToDeal - numberOfTripleCardsNeeded - numberOfDoubleCardsNeeded))
        totalWays = nCr(numberOfCardsInDeck, numberOfCardsLeftToDeal)

        return round(waysToPickDoubles * waysToPickTriples * waysToPickOthers / totalWays, 6)


        # Double check the probablity calculation is correct.


def probOfFlush(ownHand, oppoHand, handInQuestion, deck):

    # First thing to check is if their is already a flush.
    # If not is it possible.

    if handInQuestion.hasFlush() is not None:
        return 1
    elif not handInQuestion.checkSuitsSame():
        return 0
    else:

        # In this case the hand is partially complete, so we can calculate the probablity.
        if len(handInQuestion.currentHand) > 0:

            suitTryingToGet = handInQuestion.currentHand[0].suit

            numberOfCardsOfSuitLeftInDeck = numberOfCardsBySuitInDeck(ownHand, oppoHand, suitTryingToGet)
            numberOfCardsInDeck = deck.numberOfCards
            numberOfCardsNeededToComplete = 5 - numberOfCardsSuitInHand(handInQuestion, handInQuestion.currentHand[0])
            numberOfCardsLeftToDeal = ownHand.numberOfCardsLeftToBeDealt

            maxAchievable = min(numberOfCardsLeftToDeal, numberOfCardsOfSuitLeftInDeck)

            totalWaysToComplete = 0

            for i in range(0, maxAchievable-numberOfCardsNeededToComplete):

                probOfGettingExactNumber = nCr(numberOfCardsOfSuitLeftInDeck, (numberOfCardsNeededToComplete + i)) * \
                                       nCr(numberOfCardsInDeck-numberOfCardsOfSuitLeftInDeck, numberOfCardsLeftToDeal-(numberOfCardsNeededToComplete + i))
                totalWaysToComplete += probOfGettingExactNumber

            return round(totalWaysToComplete / nCr(numberOfCardsInDeck, numberOfCardsLeftToDeal), 6)
        else:
            return 0
            # COME BACK TO FIX AT SOME POINT - UNSURE HOW TO DO THIS WITH BLANK HAND.


def isCardAvalible(ownHand, oppoHand, card):

    allVisibleCard = []
    hands = [ownHand.front, ownHand.middle, ownHand.back, ownHand.discardPile, oppoHand.front, oppoHand.middle,
     oppoHand.back]

    for h in hands:
        allVisibleCard.append(h)

    # If it is in the visible cards then can not be in the deck.
    return card not in allVisibleCard


def probOfRoyalFlush(ownHand, oppoHand, handInQuestion, deck):

    allowedCards = ["10", "Jack", "Queen", "King", "Ace"]

    # If empty, or has suits are not the same
    if handInQuestion.numberOfCards == 0 or (not handInQuestion.checkSuitsSame()):
        return 0
    else:
        # Check that all cards are allowed
        suit = handInQuestion.currentHand[0].suit
        for card in handInQuestion.currentHand:
            if card.value not in allowedCards:
                return 0
            allowedCards.remove(card.value)

        # Check we can then get the cards which are left.
        for value in allowedCards:
            if not isCardAvalible(ownHand,oppoHand,Card(suit,value)):
                return 0

        # All are available, so can use combinatorial to find actual prob.

        numberOfCardsNeeded = 5 - len(allowedCards)
        numberOfDealsLeft = ownHand.numberOfCardsLeftToBeDealt

        return nCr(numberOfDealsLeft, numberOfCardsNeeded) / nCr(deck.numberOfCards, numberOfDealsLeft)



################################################################################################################
#######################################################################################################################

def probOfStraight(ownHand, oppoHand, handInQuestion, deck):

    # Check first if their are cards, and if they are in order.

    if handInQuestion.numberOfCards == 0 or not handInQuestion.checkValuesInOrder():
        return 0
    else:

        # TO DO

        return 0.01


# Also need to implement the Straight Flush option.


#####################################################################################################################################

def probOfTwoPair(ownHand, oppoHand, handInQuestion, deck, cardOne, cardTwo):

    # Find the distinct types of cards.

    handInQuestion.lineUp()
    numberOfCardsInDeck = deck.numberOfCards
    numberOfCardsLeftToDeal = ownHand.numberOfCardsLeftToBeDealt

    try:
        numberOfCardOneInHand = handInQuestion.freq.get(cardOne.getNumericValue())
        numberOfCardTwoInHand = handInQuestion.freq.get(cardTwo.getNumericValue())
        if numberOfCardOneInHand >= 2 and numberOfCardTwoInHand >= 2:
            return 1
        elif numberOfCardOneInHand >= 2 and numberOfCardTwoInHand < 2:
            numberOfThatCardLeftInDeck = numberOfCardsByValueInDeck(ownHand, oppoHand, cardTwo.value)
            numberOfCardsNeeded = 2 - numberOfCardTwoInHand

            waysToDo = nCr(numberOfThatCardLeftInDeck, numberOfCardsNeeded) * nCr(
                numberOfCardsInDeck - numberOfThatCardLeftInDeck, numberOfCardsLeftToDeal - numberOfCardsNeeded)

            totalWays = nCr(numberOfCardsInDeck, numberOfCardsLeftToDeal)
            return round(waysToDo / totalWays, 6)
        elif numberOfCardOneInHand < 2 and numberOfCardTwoInHand >= 2:
            numberOfThatCardLeftInDeck = numberOfCardsByValueInDeck(ownHand, oppoHand, cardOne.value)
            numberOfCardsNeeded = 2 - numberOfCardTwoInHand
            waysToDo = nCr(numberOfThatCardLeftInDeck, numberOfCardsNeeded) * nCr(
                numberOfCardsInDeck - numberOfThatCardLeftInDeck, numberOfCardsLeftToDeal - numberOfCardsNeeded)

            totalWays = nCr(numberOfCardsInDeck, numberOfCardsLeftToDeal)
            return round(waysToDo / totalWays, 6)
        else:
            # ----------------------
            # TODO.
            # ----------------------
            return 0
    except Exception:
        return 0












