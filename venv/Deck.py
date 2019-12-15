# Deck class which contains an array of Card objects.

from Card import Card
import random

class Deck:

    def __init__(self):

        # Should have a counter for the number of cards

        self.numberOfCards = 0
        self.cards = []

    def createNewFullDeck(self):

        Suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
        Values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        for s in Suits:
            for v in Values:
                self.cards.append(Card(s,v))

        self.numberOfCards = 52
        self.shuffle()


    #Shuffle the array of current cards.
    def shuffle(self):

        random.shuffle(self.cards)

    def dealFiveCards(self):

        # Do I need this with the except statement??????

        topFive = None

        try:
            topFive = self.cards[0:5]
            self.cards = self.cards[5:]
            self.numberOfCards -= 5

        except Exception:
            # Throw new error for to few cards
            # Need to look into how to throw an error in python.
            print("Too few cards")

        return topFive

    def dealThreeCards(self):

        topThree = None

        try:
            topThree = self.cards[0:3]
            self.cards = self.cards[3:]
            self.numberOfCards -= 3

        except Exception:
            print("Too few cards")

        return topThree


    def printDeck(self):

        print("Start of deck")
        for card in self.cards:
            print(card.value)
        print("End of deck")




if __name__ == '__main__':

    # Create new deck

    c = Deck()
    c.createNewFullDeck()
    c.dealFiveCards()
    c.dealFiveCards()
    c.dealThreeCards()
    c.printDeck()

    print(c.numberOfCards)






