from FiveCardHand import FiveCardHand
from ThreeCardHand import ThreeCardHand
from Card import Card
from Deck import Deck
from PokerHand import PokerHand


class PlayerHand:

    # Should have a back, middle and front row. Can only add to these through the methods in the classes.

    def __init__(self, name = None):

        self.playerName = name

        self.back = FiveCardHand()
        self.middle = FiveCardHand()
        self.front = ThreeCardHand()
        self.discardPile = FiveCardHand()
        self.numberOfCardsLeftToBeDealt = 17
        self.fantasyLand = False

        self.royalitesForHand = 0
        self.comparisionPointsForHand = 0

        self.totalPointsForGame = 0

    def printFullHand(self):

        print("---------- Current Hand ----------")
        print("Front Row: " + self.getHandOutput(self.front.currentHand))
        print("Middle Row: " + self.getHandOutput(self.middle.currentHand))
        print("Back Row: " + self.getHandOutput(self.back.currentHand) + "\n")

    def getHandOutput(self, hand):

        output = ""
        for card in hand:
            output += ("(" + card.value + ", " + card.suit + "), ")
        return output

    def printDeal(self, deal):

        print("-----------   Deal   ------------")
        for i in range(1, len(deal) + 1):
            card = deal[i-1]
            output = "(" + card.value + ", " + card.suit + ")"
            print("Card Number " + str(i) + ": " + output)
        print()

    # This should have 2 external facing methods, threeCardResponse and fiveCardResponse.
    # These, given a deal and the current state of the deck and oppos hand respond.
    # Overwritten function in the computer player class.

    def getResponseAndMove(self, card):

        done = False
        while not done:
            print("Where would you like to place " + "(" + card.value + ", " + card.suit + ")" + ": ")

            # Try used to check that the hand is not full - if it is then prompt user again.
            handWanted = input().upper()
            if handWanted.startswith("F"):
                try:
                    self.front.addCard(card)
                    done = True
                except Exception:
                    print("Hand Full. Try again.")
            if handWanted.startswith("M"):
                try:
                    self.middle.addCard(card)
                    done = True
                except Exception:
                    print("Hand Full. Try again.")
            if handWanted.startswith("B"):
                try:
                    self.back.addCard(card)
                    done = True
                except Exception:
                    print("Hand Full. Try again.")

    def findCardToThrowAway(self, cards):

        done = False
        while not done:
            print("Which card would you like to throw away (1, 2, 3): ")
            cardToThrow = input()
            try:
                discard = cards.pop(int(cardToThrow)-1)
                self.discardPile.addCard(discard)
                done = True
                return cards
            except Exception:
                print("Invalid entry - please try again.")


    # Here deal must be passed, this is the 3 cards which are given by the Play class as an array.
    # deal: List of card types.

    def threeCardResponse(self, deal, oppoHand, deck):

        self.numberOfCardsLeftToBeDealt -= 3
        self.printDeal(deal)

        # Then need to get the player to discard a card.
        # Then with the remaining can just add to whichever pile.

        self.printFullHand()
        self.findCardToThrowAway(deal)
        print("Please enter an input of either Front (F), Middle (M)" +
              " or Back (B) for where you would like to move the card. \n")
        for i in range(0,2):
            self.getResponseAndMove(deal[i])


    # Same method with the 5 card response move.
    def fiveCardResponse(self, deal, oppoHand, deck):

        # Find the deal from the deck and print this out.
        self.numberOfCardsLeftToBeDealt -= 5
        self.printDeal(deal)

        # Depending on the player then print their current Deck.

        self.printFullHand()
        print("Please enter an input of either Front (F), Middle (M)" +
              " or Back (B) for where you would like to move the card. \n")
        for i in range(0,5):
            self.getResponseAndMove(deal[i])


    # Get the score for a hand at the end.
    def scoreRoyalitiesHand(self):

        # Ovewritten methods in both classes for this, so will use the three card play royality for
        # the front hand.

        if self.isHandBust():
            return 0
        else:
            frontScore = self.front.evaluateHand("Front")
            middleScore = self.middle.evaluateHand("Middle")
            backScore = self.back.evaluateHand("Back")
            self.royalitesForHand = sum([frontScore, middleScore, backScore])

            return self.royalitesForHand


    def compareTwoHands(self, handTwo):

        # Account for bust hands, and non-bust hands, by checking first.
        # Account for clean sweeps too now.

        if self.isHandBust() and handTwo.isHandBust():
            return 0
        elif self.isHandBust() and not handTwo.isHandBust():
            return -6
        elif not self.isHandBust() and handTwo.isHandBust():
            return 6
        else:

            frontComp = self.front.compareRow(handTwo.front)
            print("Front: ", frontComp)
            middleComp = self.middle.compareRow(handTwo.middle)
            print("Middle: ", middleComp)
            backComp = self.back.compareRow(handTwo.back)
            print("Back: ", backComp)

            total = frontComp + middleComp + backComp

            if total == 3: # Taking care of the clean sweep.
                total += 3
            if total == -3:
                total -= 3

            self.comparisionPointsForHand = total
            handTwo.comparisionPointsForHand = -total

            return frontComp + middleComp + backComp


    def isHandBust(self):

        # Check that the front is weaker than the middle, and middle weaker than back.
        if self.front.compareRow(self.middle) <= 0 and self.middle.compareRow(self.back) <= 0: # Ugly, but they produce numbers rather than true false, as they could be even.
            return False
        else:
            return True



if  __name__ == "__main__":

    print("Hello")
