class PokerHand:

    # To be used to encapsulate the information about the style of poker hand which is being played.
    # Important cards used to hold the important rankings which are containing in the hand, i.e, how good the pair is etc.
    # This can only be used when comparing two hands of the same style:
    # e.g: 2 hands each with 2 pair: [12,3,6] = [Queen,Queen,3,3,6] and [12,5,7] = [Queen, Queen, 5, 5, 7] so we can just compare term by term.
    # e.g: 4 of kind hand: [3,7] = [3,3,3,3,7]
    # e.g: Flush we care about all the cards so should read [12,7,6,3,2] as no need to be continous, thus can compare card by card again.

    def __init__(self, style = None, cardNumbers = []):

        self.style = style
        self.importantCards = cardNumbers