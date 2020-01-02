from FiveCardHand import FiveCardHand
from ThreeCardHand import ThreeCardHand
from Card import Card
from Deck import Deck
from PokerHand import PokerHand
from PlayerHand import PlayerHand
import random
import LikelihoodCalculator

class ComputerPlayer(PlayerHand):


    def __init__(self):
        super(ComputerPlayer, self).__init__()
        self.playerName = "Computer"

    # OVERRIDE - for the computer deciding.

    # This function should given the current hand evaluate the expected outcome.

    def evaluateFrontStrategy(self, oppoHand, deck):


        # First check if the hand is full, and if so just evaluate this and give this back as the expected value.
        if len(self.front.currentHand) == 3:

            print("Already full front hand")
            print("Score: " + str(self.front.evaluateHand("Front")))
            return self.front.evaluateHand("Front")


        # If not cycle through the cards in the hand.

        maxFrontEV = 0      # Hold the best expected value.
        bestFrontStrategy = []   # Hold what would bring about this.
        for card in self.front.currentHand:

            # First check the chances to completing a pair of each card
            # Find the probablity of a pair
            #print("Pair Check\n")
            #print("Checking EV of pair for: " + card.value + " " + card.suit)
            chance = LikelihoodCalculator.probOfCollectionOfCard(self, oppoHand, self.front, deck, card, 2)
            #print("Chance: " + str(chance))
            # Find the score of the pair.
            value = LikelihoodCalculator.computeExpectedRoyality(card.getNumericValue(), "One Pair", "Front")
            #print("Value: " + str(value))
            EV = chance * value
            #print("Expected Value: " + str(EV))

            if EV > maxFrontEV:
                maxFrontEV = EV
                bestFrontStrategy = [("One Pair", card.value)]

            # Now check the chance of it being a triple.
            #print("Three of a Kind Check\n")
            #print("Checking EV of Three of a Kind for: " + card.value + " " + card.suit)
            chance = LikelihoodCalculator.probOfCollectionOfCard(self, oppoHand, self.front, deck, card, 3)
            #print("Chance: " + str(chance))
            # Find the score of the pair.
            value = LikelihoodCalculator.computeExpectedRoyality(card.getNumericValue(), "Three of a Kind", "Front")
            #print("Value: " + str(value))
            EV = chance * value
            #print("Expected Value: " + str(EV))

            if EV > maxFrontEV:
                maxFrontEV = EV
                bestFrontStrategy = [("Three of a Kind", card.value)]

        print("Best EV coming from strategy: " + str(bestFrontStrategy))
        return maxFrontEV


    def evaluateStrategy(self, oppoHand, deck, depth):

        if depth == "Middle":
            handInQuestion = self.middle

            if len(self.middle.currentHand) == 5:
                print("Already full middle hand")
                return self.middle.evaluateHand("Middle")

        else:
            handInQuestion = self.back

            if len(self.back.currentHand) == 5:
                print("Already full back hand")
                return self.back.evaluateHand("Back")


        # If not then cycle through the cards each time checking for pair, three of kind etc.
        maxEV = 0
        bestStrategy = []

        for card in handInQuestion.currentHand:

            # Check through the combinations of "Pair", "Two Pair" etc.... each time recording the maxEV as expected.
            #print("Pair Check\n")
            #print("Checking EV of pair for: " + card.value + " " + card.suit)
            chance = LikelihoodCalculator.probOfCollectionOfCard(self, oppoHand, handInQuestion, deck, card, 2)
            #print("Chance: " + str(chance))
            # Find the score of the pair.
            value = LikelihoodCalculator.computeExpectedRoyality(card.getNumericValue(), "One Pair", depth)
            #print("Value: " + str(value))
            EV = chance * value
            #print("Expected Value: " + str(EV))

            if EV > maxEV:
                maxEV = EV
                bestStrategy = [("One Pair", card.value)]

            # Three of a kind check:
            #print("Three of a Kind Check\n")
            #print("Checking EV of Three of a Kind for: " + card.value + " " + card.suit)
            chance = LikelihoodCalculator.probOfCollectionOfCard(self, oppoHand, handInQuestion, deck, card, 3)
            #print("Chance: " + str(chance))
            # Find the score of the pair.
            value = LikelihoodCalculator.computeExpectedRoyality(card.getNumericValue(), "Three of a Kind", depth)
            #print("Value: " + str(value))
            EV = chance * value
            #print("Expected Value: " + str(EV))

            if EV > maxEV:
                maxEV = EV
                bestStrategy = [("Three of a Kind", card.value)]

            # Four of a kind check
            #print("Four of a Check\n")
            #print("Checking EV of Four of a Kind for: " + card.value + " " + card.suit)
            chance = LikelihoodCalculator.probOfCollectionOfCard(self, oppoHand, handInQuestion, deck, card, 4)
            #print("Chance: " + str(chance))
            # Find the score of the pair.
            value = LikelihoodCalculator.computeExpectedRoyality(card.getNumericValue(), "Four of a kind", depth)
            #print("Value: " + str(value))
            EV = chance * value
            #print("Expected Value: " + str(EV))

            if EV > maxEV:
                maxEV = EV
                bestStrategy = [("Four of a Kind", card.value)]


            # Flush Check
            #print("Flush Check\n")
            #print("Checking EV of Flush for: " + card.value + " " + card.suit)
            chance = LikelihoodCalculator.probOfFlush(self, oppoHand, handInQuestion, deck)
            #print("Chance: " + str(chance))
            # Find the score of the pair.
            value = LikelihoodCalculator.computeExpectedRoyality(card.getNumericValue(), "Flush", depth)
            #print("Value: " + str(value))
            EV = chance * value
            #print("Expected Value: " + str(EV))

            if EV > maxEV:
                maxEV = EV
                bestStrategy = [("Flush", card.suit)]

            # TODO
            # Straight Check
            # print("Straight Check")
            # print("Checking EV of Straight for: " + card.value + " " + card.suit)
            # chance = LikelihoodCalculator.probOfStraight(self, oppoHand, handInQuestion, deck)
            # print("Chance: " + str(chance))
            # # Find the score of the pair.
            # value = LikelihoodCalculator.computeExpectedRoyality(card.getNumericValue(), "Straight", depth)
            # print("Value: " + str(value))
            # EV = chance * value
            # print("Expected Value: " + str(EV))
            #
            # if EV > maxEV:
            #     maxEV = EV
            #     bestStrategy = [("Straight", card.value)]

            # TODO
            # #Straight Flush Check
            #
            # print("Straight Flush Check")
            # print("Checking EV of Straight Flush for: " + card.value + " " + card.suit)
            # chance = LikelihoodCalculator.probOfStraightFlush(self, oppoHand, self.middle, deck)
            # print("Chance: " + str(chance))
            # # Find the score of the pair.
            # value = LikelihoodCalculator.computeExpectedRoyality(card.getNumericValue(), "Straight Flush", depth)
            # print("Value: " + str(value))
            # EV = chance * value
            # print("Expected Value: " + str(EV))
            #
            # if EV > maxEV:
            #     maxEV = EV
            #     bestStrategy = [("Straight", card.value, card.suit)]

            # # Royal Flush Check
            #
            # print("Royal Flush")
            # print("Checking EV of Royal Flush for: " + card.value + " " + card.suit)
            # chance = LikelihoodCalculator.probOfRoyalFlush(self, oppoHand, handInQuestion, deck)
            # print("Chance: " + str(chance))
            # # Find the score of the pair.
            # value = LikelihoodCalculator.computeExpectedRoyality(card.getNumericValue(), "Royal Flush", depth)
            # print("Value: " + str(value))
            # EV = chance * value
            # print("Expected Value: " + str(EV))
            #
            # if EV > maxEV:
            #     maxEV = EV
            #     bestStrategy = [("Royal Flush", card.suit)]


            # NOW FOR THE TRICKY ONES
            # For full house and two pair we need two distinct cards to be there in order to use the functions to calculate
            # The likelihood of completeing them.

            # Loop through and find the cards which do not share the same value as the first card and use this to check the two pair
            # and full house chance with them. Allow this for all cards.

            # for otherCard in handInQuestion.currentHand:
            #     if otherCard.value != card.value:
            #
            #         # We are in business so we can use this to then check.
            #         # Two Pair Check
            #
            #         print("Two Pair")
            #         print("Checking EV of Two Pair for: " + card.value + " " + card.suit + " and " + otherCard.value + " " + otherCard.suit)
            #         chance = LikelihoodCalculator.probOfTwoPair(self, oppoHand, handInQuestion, deck, card, otherCard)
            #         print("Chance: " + str(chance))
            #         # Find the score of the pair.
            #         value = LikelihoodCalculator.computeExpectedRoyality(card.getNumericValue(), "Two Pair", depth)
            #         print("Value: " + str(value))
            #         EV = chance * value
            #         print("Expected Value: " + str(EV))
            #
            #         if EV > maxEV:
            #             maxEV = EV
            #             bestStrategy = [("Two Pair", card.value, otherCard.value)]
            #
            #
            #         # Full House Check.
            #         print("Two Pair")
            #         print("Checking EV of Full House for: " + card.value + " " + card.suit + " and " + otherCard.value + " " + otherCard.suit)
            #         chance = LikelihoodCalculator.probOfFullHouse(self, oppoHand, handInQuestion, deck, card, otherCard)
            #         print("Chance: " + str(chance))
            #         # Find the score of the pair.
            #         value = LikelihoodCalculator.computeExpectedRoyality(card.getNumericValue(), "Full House", depth)
            #         print("Value: " + str(value))
            #         EV = chance * value
            #         print("Expected Value: " + str(EV))
            #
            #         if EV > maxEV:
            #             maxEV = EV
            #             bestStrategy = [("Two Pair", card.value, otherCard.value)]

        print("Best EV coming from strategy: " + str(bestStrategy))
        return maxEV











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
        self.printFullHand()
        self.printDeal(deal)

        print("\nFRONT\n")
        frontEV = self.evaluateFrontStrategy(oppoHand, deck)
        print("\nMIDDLE\n")
        middleEV = self.evaluateStrategy(oppoHand, deck, "Middle")
        print("\nBACK\n")
        backEV = self.evaluateStrategy(oppoHand, deck, "Back")
        print("EVs: Front - " + str(frontEV) + "    Middle - " + str(middleEV) + "    Back - " + str(backEV))
        print("Sum of the maxEVs: " + str(frontEV + middleEV + backEV) + "\n\n")

        # So now try each combination of the cards in the available hands to see which gives the best maxEV.

        choiceOfHand = self.findHandsWhichHaveSpace() # This returns "Back", "Middle", "Front" as strings.
        # Have to use the addCard function to do this properly.

        maximumEV = -1           # To ensure we get at least one value.
        indexArray = []
        handArray = []

        for i in range(0,2):
            # So take the card out of the set
            cardsToUse = list(set([0,1,2]) - set([i]))
            for hand in choiceOfHand:
                if hand == "Back":
                    self.back.addCard(deal[i])
                elif hand == "Middle":
                    self.middle.addCard(deal[i])
                elif hand == "Front":
                    self.front.addCard(deal[i])
                else:
                    print("MAJOR ERROR")

                for j in cardsToUse:

                    remainingChoice = self.findHandsWhichHaveSpace()

                    for remHand in remainingChoice:
                        if remHand == "Back":
                            self.back.addCard(deal[j])
                        elif remHand == "Middle":
                            self.middle.addCard(deal[j])
                        elif remHand == "Front":
                            self.front.addCard(deal[j])
                        else:
                            print("MAJOR ERROR")

                        # Now score the element.
                        totalEV = self.evaluateFrontStrategy(oppoHand, deck) + self.evaluateStrategy(oppoHand, deck, "Middle") + self.evaluateStrategy(oppoHand, deck, "Back")
                        if totalEV > maximumEV:
                            totalEV = maximumEV
                            indexArray = [i,j]
                            handArray = [hand,remHand]
                            print("Update: " + str(indexArray) + str(handArray))

                        # Then remove the card as we don't need it any more
                        if remHand == "Back":
                            self.back.removeCard(deal[j])
                        elif remHand == "Middle":
                            self.middle.removeCard(deal[j])
                        elif remHand == "Front":
                            self.front.removeCard(deal[j])
                        else:
                            print("MAJOR ERROR")

                # Then remove the card as we don't need it any more
                if hand == "Back":
                    self.back.removeCard(deal[i])
                elif hand == "Middle":
                    self.middle.removeCard(deal[i])
                elif hand == "Front":
                    self.front.removeCard(deal[i])
                else:
                    print("MAJOR ERROR")

        print("MAX EV ACHEIVED: " + str(maximumEV))







        # THEN JUST ADD THE REST OF THEM.

        for k in range(0,2):
            pick = handArray[k]
            index = indexArray[k]

            if pick == "Back":
                self.back.addCard(deal[index])
            elif pick == "Middle":
                self.middle.addCard(deal[index])
            elif pick == "Front":
                self.front.addCard(deal[index])
            else:
                print("MAJOR ERROR")
                # TO DO - ADD IN THE ERROR HERE.

        # Throw away the first card.
        # AS THEY'LL ONLY BE ONE ELEMENT

        throwAwayArr = list(set([0, 1, 2]) - set(indexArray))
        deal.pop(throwAwayArr[0])

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