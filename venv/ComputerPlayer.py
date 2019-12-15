from FiveCardHand import FiveCardHand
from ThreeCardHand import ThreeCardHand
from Card import Card
from Deck import Deck
from PokerHand import PokerHand
from PlayerHand import PlayerHand
import random

class ComputerPlayer(PlayerHand):


    def __init__(self):
        super(ComputerPlayer, self).__init__()
        self.playerName = "Computer"

    # OVERRIDE - for the computer deciding.


    def findCardToThrowAway(self, cards):
        return 0


    def findHandsWhichHaveSpace(self):

        hands = []

        if self.back.numberOfCards < 5:
            hands.append("Back")
        if self.middle.numberOfCards < 5:
            hands.append("Middle")
        if self.front.numberOfCards < 3:
            hands.append("Front")

        return hands


    def threeCardResponse(self, deal, oppoHand, deck):

        self.numberOfCardsLeftToBeDealt -= 3
        self.printDeal(deal)


        # Throw away the first card.
        deal.pop(0)

        for i in range(0,2):
            choiceOfHand = self.findHandsWhichHaveSpace()
            pick = random.choice(choiceOfHand)

            if pick == "Back":
                self.back.addCard(deal[i])
            elif pick == "Middle":
                self.middle.addCard(deal[i])
            elif pick == "Front":
                self.front.addCard(deal[i])
            else:
                print("MAJOR ERROR")
                # TO DO - ADD IN THE ERROR HERE.

        self.printFullHand()

    def fiveCardResponse(self, deal, oppoHand, deck):

        self.numberOfCardsLeftToBeDealt -= 5
        self.printDeal(deal)

        for i in range(0,5):
            choiceOfHand = self.findHandsWhichHaveSpace()
            pick = random.choice(choiceOfHand)

            if pick == "Back":
                self.back.addCard(deal[i])
            elif pick == "Middle":
                self.middle.addCard(deal[i])
            elif pick == "Front":
                self.front.addCard(deal[i])
            else:
                print("MAJOR ERROR")
                # TO DO - ADD IN THE ERROR HERE.

        self.printFullHand()