from ThreeCardHand import ThreeCardHand
from FiveCardHand import FiveCardHand
from Card import Card

def threeCardTest():

    test3 = ThreeCardHand()
    print("\nTests for 3 card hand.\n")

    # High Card

    test3.currentHand = [Card("Heart", "9"), Card("Diamond", "7"), Card("Heart", "8")]
    result3 = test3.hasHighCard()
    print("Test Correct high card: ", result3.high == 9)

    test3.currentHand = [Card("Heart", "8"), Card("Diamond", "7"), Card("Heart", "10")]
    result3 = test3.hasHighCard()
    print("Test Correct high card and next best: ", result3.high == 10 and result3.low == 8)

    # One Pair

    test3.currentHand = [Card("Heart", "Ace"), Card("Diamond", "7"), Card("Heart", "Ace")]
    result3 = test3.hasOnePair()
    print("Test Correct one pair with first and last cards: ", result3 is not None)

    test3.currentHand = [Card("Heart", "5"), Card("Diamond", "7"), Card("Heart", "7")]
    result3 = test3.hasOnePair()
    print("Test Correct one pair with last two cards: ", result3 is not None)

    test3.currentHand = [Card("Heart", "5"), Card("Diamond", "6"), Card("Heart", "7")]
    result3 = test3.hasOnePair()
    print("Test Correct one pair with split cards: ", result3 is None)

    test3.currentHand = [Card("Heart", "5"), Card("Diamond", "5"), Card("Heart", "7")]
    result3 = test3.hasOnePair()
    print("Test Correct one pair with highest value otherwise: ", result3.low == 7 and result3.high == 5)

    test3.currentHand = [Card("Heart", "7"), Card("Diamond", "Ace"), Card("Heart", "7")]
    result3 = test3.hasOnePair()
    print("Test Correct pairs with highest value otherwise with ace: ", result3.low == 14)

    # Three of Kind

    test3.currentHand = [Card("Heart", "7"), Card("Diamond", "7"), Card("Spade", "7")]
    result3 = test3.hasThreeOfKind()
    print("Test Correct Three of kind: ", result3.high == 7)

    test3.currentHand = [Card("Heart", "7"), Card("Diamond", "Ace"), Card("Heart", "7")]
    result3 = test3.hasThreeOfKind()
    print("Test Correct No Three of kind: ", result3 is None)



def fiveCardTest():

    test5 = FiveCardHand()
    test5.numberOfCards = 5
    print("\nTests for 5 card hand.\n")

    # High Card

    test5.currentHand = [Card("Heart", "6"), Card("Diamond", "Ace"), Card("Heart", "7"), Card("Diamond", "5"),
                         Card("Shade", "7")]
    result5 = test5.hasHighCard()
    print("Test for high card: ", result5.high == 14, result5.low == 7)

    # One Pair

    test5.currentHand = [Card("Heart", "6"), Card("Diamond", "Ace"), Card("Heart", "7"), Card("Diamond", "5"),
                         Card("Shade", "7")]
    result5 = test5.hasOnePair()
    print("Test for one pair with singles: ", result5.high == 7, result5.low == 14)


    test5.currentHand = [Card("Heart", "6"), Card("Diamond", "4"), Card("Heart", "7"), Card("Diamond", "6"),
                         Card("Shade", "7")]
    result5 = test5.hasOnePair()
    print("Test for one pair with two distinct pairs", result5.high == 7, result5.low == 6)

    # Three of Kind

    test5.currentHand = [Card("Heart", "7"), Card("Diamond", "Ace"), Card("Heart", "7"), Card("Diamond", "5"),
                         Card("Shade", "7")]
    result5 = test5.hasThreeOfKind()
    print("Test Correct Three of kind: ", result5.high == 7)

    test5.currentHand = [Card("Heart", "7"), Card("Diamond", "Ace"), Card("Heart", "7"), Card("Diamond", "5"),
                         Card("Shade", "6")]
    result5 = test5.hasThreeOfKind()
    print("Test No Three of kind: ", result5 is None)

    test5.currentHand = [Card("Heart", "7"), Card("Diamond", "Jack"), Card("Heart", "7"), Card("Diamond", "5"),
                         Card("Shade", "7")]
    result5 = test5.hasThreeOfKind()
    print("Test Three of kind: ", result5.high == 7, result5.low == 11)

    # Two Pair

    test5.currentHand = [Card("Heart", "7"), Card("Diamond", "Jack"), Card("Heart", "7"), Card("Diamond", "5"),
                         Card("Shade", "5")]
    result5 = test5.hasTwoPair()
    print("Test for two pair: ", result5.high == 7, result5.low == 5)

    test5.currentHand = [Card("Heart", "6"), Card("Diamond", "Jack"), Card("Heart", "7"), Card("Diamond", "5"),
                         Card("Shade", "5")]
    result5 = test5.hasTwoPair()
    print("Test for two pair: ", result5 is None)

    # Full House

    test5.currentHand = [Card("Heart", "7"), Card("Diamond", "Jack"), Card("Heart", "7"), Card("Diamond", "5"),
                     Card("Shade", "5")]
    result5 = test5.hasFullHouse()
    print("Test for full house negative: ", result5 is None)

    test5.currentHand = [Card("Heart", "7"), Card("Diamond", "5"), Card("Heart", "7"), Card("Diamond", "5"),
                     Card("Shade", "5")]
    result5 = test5.hasFullHouse()
    print("Test for full house positive: ", result5.high == 5, result5.low == 7)

    # Full House

    test5.currentHand = [Card("Heart", "7"), Card("Diamond", "7"), Card("Heart", "7"), Card("Diamond", "5"),
                   Card("Shade", "7")]
    result5 = test5.hasFourOfKind()
    print("Test for four of kind positive: ", result5.high == 7, result5.low == 5)

    test5.currentHand =[Card("Heart", "7"), Card("Diamond", "4"), Card("Heart", "7"), Card("Diamond", "5"),
                          Card("Shade", "7")]
    result5 = test5.hasFourOfKind()
    print("Test for four of kind negative: ", result5 is None)

    # Flush

    test5.currentHand = [Card("Heart", "3"), Card("Heart", "7"), Card("Heart", "6"), Card("Heart", "5"),
                          Card("Heart", "Jack")]
    result5 = test5.hasFlush()
    print("Test for flush positive: ", result5.high == 11, result5.low == 7)

    test5.currentHand = [Card("Spade", "3"), Card("Heart", "7"), Card("Heart", "6"), Card("Heart", "5"),
                          Card("Heart", "Jack")]
    result5 = test5.hasFlush()
    print("Test for flush Negative first: ", result5 is None)

    test5.currentHand = [Card("Spade", "3"), Card("Spade", "7"), Card("Spade", "6"), Card("Heart", "5"),
                         Card("Heart", "Jack")]
    result5 = test5.hasFlush()
    print("Test for flush Negative couple: ", result5 is None)

    # Straight

    test5.currentHand = [Card("Spade", "4"), Card("Spade", "7"), Card("Spade", "6"), Card("Heart", "5"),
                         Card("Heart", "8")]
    result5 = test5.hasStraight()
    print("Test for straight Positive: ", result5.high == 8)

    test5.currentHand = [Card("Spade", "3"), Card("Spade", "7"), Card("Spade", "6"), Card("Heart", "5"),
                         Card("Heart", "3")]
    result5 = test5.hasStraight()
    print("Test for straight Negative with pair: ", result5 is None)

    test5.currentHand = [Card("Spade", "3"), Card("Spade", "7"), Card("Spade", "6"), Card("Heart", "5"),
                         Card("Heart", "Jack")]
    result5 = test5.hasStraight()
    print("Test for straight Negative with distinct: ", result5 is None)

    # Straight Flush

    test5.currentHand = [Card("Spade", "4"), Card("Spade", "7"), Card("Spade", "6"), Card("Spade", "5"),
                         Card("Spade", "8")]
    result5 = test5.hasStraightFlush()
    print("Test for Straight Flush Positive: ", result5.high == 8)

    test5.currentHand = [Card("Spade", "3"), Card("Spade", "7"), Card("Spade", "6"), Card("Heart", "5"),
                         Card("Heart", "Jack")]
    result5 = test5.hasStraightFlush()
    print("Test for Straight Flush Negative with distinct: ", result5 is None)

    test5.currentHand = [Card("Spade", "3"), Card("Spade", "7"), Card("Spade", "6"), Card("Heart", "5"),
                         Card("Heart", "Jack")]
    result5 = test5.hasStraightFlush()
    print("Test for Straight Flush Negative with distinct: ", result5 is None)

    # Royal Flush

    test5.currentHand = [Card("Spade", "10"), Card("Spade", "Jack"), Card("Spade", "Queen"), Card("Spade", "King"),
                         Card("Spade", "Ace")]
    result5 = test5.hasRoyalFlush()
    print("Test for Royal Flush Positive: ", result5.style == "Royal Flush" , result5.high == 14)

    test5.currentHand = [Card("Spade", "3"), Card("Spade", "7"), Card("Spade", "6"), Card("Spade", "5"),
                         Card("Spade", "8")]
    result5 = test5.hasRoyalFlush()
    print("Test for Royal Flush Negative: ", result5 is None)


def bestHandTest():

    hand = ThreeCardHand()

    hand.currentHand = [Card("Heart", "8"), Card("Diamond", "7"), Card("Heart", "10")]
    result = hand.findHandType()
    print("Test for best hand: ", result.style == "High Card")

    hand.currentHand = [Card("Heart", "8"), Card("Diamond", "8"), Card("Heart", "10")]
    result = hand.findHandType()
    print("Test for best hand: ", result.style == "One Pair")

    hand.currentHand = [Card("Heart", "8"), Card("Diamond", "8"), Card("Spade", "8")]
    result = hand.findHandType()
    print("Test for best hand: ", result.style == "Three of a Kind")

    handFive = FiveCardHand()

    handFive.currentHand = [Card("Spade", "3"), Card("Spade", "7"), Card("Spade", "6"), Card("Heart", "5"),
                         Card("Heart", "4")]
    result = handFive.findHandType()
    print("Test 5 card best hand: ", result.style == "Straight")

    handFive.currentHand = [Card("Spade", "3"), Card("Spade", "7"), Card("Spade", "6"), Card("Spade", "5"),
                            Card("Spade", "4")]
    result = handFive.findHandType()
    print("Test 5 card best hand: ", result.style == "Straight Flush")

    handFive.currentHand = [Card("Spade", "4"), Card("Spade", "4"), Card("Spade", "4"), Card("Heart", "5"),
                            Card("Heart", "4")]
    result = handFive.findHandType()
    print("Test 5 card best hand: ", result.style == "Four of a Kind")


def comparingRowsThreeRowTests():

    hand1 = ThreeCardHand()
    hand2 = ThreeCardHand()

    hand1.currentHand = [Card("Spade", "8"), Card("Diamond", "7"), Card("Spade", "7")]
    hand2.currentHand = [Card("Diamond", "8"), Card("Diamond", "7"), Card("Spade", "7")]
    result = hand1.compareRow(hand2)
    print("Test for same hands give 0: ", result == 0)

    hand1.currentHand = [Card("Spade", "Ace"), Card("Diamond", "Ace"), Card("Spade", "7")]
    hand2.currentHand = [Card("Diamond", "8"), Card("Diamond", "7"), Card("Spade", "7")]
    result = hand1.compareRow(hand2)
    print("Test for better first hand gives 1: ", result == 1)

    hand1.currentHand = [Card("Spade", "8"), Card("Diamond", "8"), Card("Spade", "7")]
    hand2.currentHand = [Card("Diamond", "8"), Card("Diamond", "9"), Card("Spade", "9")]
    result = hand1.compareRow(hand2)
    print("Test for better second hand gives -1: ", result == -1)

    hand1.currentHand = [Card("Spade", "8"), Card("Diamond", "8"), Card("Spade", "7")]
    hand2.currentHand = [Card("Diamond", "8"), Card("Diamond", "8"), Card("Spade", "6")]
    result = hand1.compareRow(hand2)
    print("Test for better first hand on high gives 1: ", result == 1)

    hand1.currentHand = [Card("Spade", "8"), Card("Diamond", "8"), Card("Spade", "8")]
    hand2.currentHand = [Card("Diamond", "8"), Card("Diamond", "8"), Card("Spade", "8")]
    result = hand1.compareRow(hand2)
    print("Test for triples gives the equal: ", result == 0)

    # This test will fail - need to fix (importantValues array to store the high / low and other things which are needed in order to compltetely compare hands)

    hand1.currentHand = [Card("Spade", "10"), Card("Diamond", "8"), Card("Spade", "7")]
    hand2.currentHand = [Card("Diamond", "10"), Card("Diamond", "8"), Card("Spade", "3")]
    result = hand1.compareRow(hand2)
    print("Test for better first hand gives 1: (Expected to fail) ", result == 1)











if __name__ == "__main__":

    #threeCardTest()
    #fiveCardTest()
    #bestHandTest()
    comparingRowsThreeRowTests()







