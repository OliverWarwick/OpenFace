# One play of open face, return UNKNOWN ATM
from PlayerHand import PlayerHand
from ComputerPlayer import ComputerPlayer
from Deck import Deck
from Card import Card
import LikelihoodCalculator
import time


class Play:

    # Constructor for two human players.
    def __init__(self, namePlayerOne = "Default", namePlayerTwo = "Default"):

        if namePlayerOne != "Default" and namePlayerTwo != "Default":
            self.playerOne = PlayerHand(namePlayerOne)
            self.playerTwo = PlayerHand(namePlayerTwo)
        elif namePlayerOne != "Default" and namePlayerTwo == "Default":
            self.playerOne = PlayerHand(namePlayerOne)
            self.playerTwo = ComputerPlayer()
        else:
            self.playerOne = ComputerPlayer()
            self.playerTwo = ComputerPlayer()
        self.deck = Deck()
        self.deck.createNewFullDeck()
        self.currentPlayer = 1



    # Complete a 5 card deal.
    def completeFiveCardTurn(self):
        print("\n\n" + self.playerOne.playerName + " Turn " + "(Player 1)\n\n")
        dealOne = self.deck.dealFiveCards()
        self.playerOne.fiveCardResponse(dealOne, self.playerTwo, self.deck)
        print("\n\n")

        print(self.playerTwo.playerName + " Turn " + "(Player 2)\n\n")
        dealTwo = self.deck.dealFiveCards()
        self.playerTwo.fiveCardResponse(dealTwo, self.playerOne, self.deck)
        print("\n\n")


    # Complete a 3 card deal.
    def completeThreeCardTurn(self):
        print("\n\n" + self.playerOne.playerName + " Turn " + "(Player 1)\n\n")
        dealOne = self.deck.dealThreeCards()
        self.playerOne.threeCardResponse(dealOne, self.playerTwo, self.deck)
        print("\n\n")

        print(self.playerTwo.playerName + " Turn " + "(Player 2)\n\n")
        dealTwo = self.deck.dealThreeCards()
        self.playerTwo.threeCardResponse(dealTwo, self.playerOne, self.deck)
        print("\n\n")




    # Standard game play routine.

    def playHand(self):

        if self.playerOne.fantasyLand and not self.playerTwo.fantasyLand:
            # TODO
            pass
        elif self.playerTwo.fantasyLand and not self.playerOne.fantasyLand:
            # TODO
            pass
        elif self.playerOne.fantasyLand and self.playerTwo.fantasyLand:
            # TODO
            pass
        else:
            # Normal style of game play.
            print("First Round - 5 cards.")
            self.completeFiveCardTurn()
            print("Second Round - 3 cards.")
            self.completeThreeCardTurn()
            print("Third Round - 3 cards.")
            self.completeThreeCardTurn()
            print("Fourth Round - 3 cards.")
            self.completeThreeCardTurn()
            print("Final Round - 3 cards.")
            self.completeThreeCardTurn()

        # Evaluate the points for royalties and then for the comparision picture.

        # .evaluateHand() returns an array containing the front/middle/back score. To access the actual score, just reference the self.player.royalitiesForHand

        print("Finished Play - evaluating scores.")
        scorePlayerOne = self.playerOne.scoreRoyalitiesHand()
        print("Player One Scores: " + str(scorePlayerOne))

        scorePlayerTwo = self.playerTwo.scoreRoyalitiesHand()
        print("Player Two Scores: " + str(scorePlayerTwo))

        comparisionPoints = self.playerOne.compareTwoHands(self.playerTwo)
        print("Comparision points: ", comparisionPoints)

        # Sort out the points totals for the game.
        self.playerOne.totalPointsForGame += ((self.playerOne.royalitesForHand-self.playerTwo.royalitesForHand) + comparisionPoints)
        self.playerTwo.totalPointsForGame += ((self.playerTwo.royalitesForHand-self.playerOne.royalitesForHand) - comparisionPoints)

        print("Player 1 current points: ", self.playerOne.totalPointsForGame)
        print("Player 2 current points: ", self.playerTwo.totalPointsForGame)




def runNManyTrials(n):
    # maxScorePlayerOne = 0
    # maxScorePlayerTwo = 0
    # bestHandPlayerOne = PlayerHand()
    # bestHandPlayerTwo = PlayerHand()
    s = []

    for i in range(0, n):
        p = Play()
        p.playHand()
        s.append(p.playerOne.totalPointsForGame)


        # if p.playerOne.scoreForHand > maxScorePlayerOne:
        #     maxScorePlayerOne = p.playerOne.scoreForHand
        #     bestHandPlayerOne.front = p.playerOne.front
        #     bestHandPlayerOne.middle = p.playerOne.middle
        #     bestHandPlayerOne.back = p.playerOne.back
        # if p.playerTwo.scoreForHand > maxScorePlayerTwo:
        #     maxScorePlayerTwo = p.playerTwo.scoreForHand
        #     bestHandPlayerTwo.front = p.playerTwo.front
        #     bestHandPlayerTwo.middle = p.playerTwo.middle
        #     bestHandPlayerTwo.back = p.playerTwo.back

    # print("---------------------------------------------------------")
    # print("FINISHED: ")
    #
    # print("Player 1")
    # print(maxScorePlayerOne)
    # bestHandPlayerOne.printFullHand()
    #
    # print("Player 2")
    # print(maxScorePlayerTwo)
    # bestHandPlayerTwo.printFullHand

    return s



if  __name__ == "__main__":


    # scores = []

    # for i in range(0,50):
    #     s = runNManyTrials(5)
    #     scores.append(s)
    #
    # print(scores)

    p = Play()
    p.playHand()


























