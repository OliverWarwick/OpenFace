class PokerHand:

    # To be used to encapsulate the information about the style of poker hand which is being played.

    def __init__(self, style = None, high = 1, low = 1):

        self.style = style
        self.high = high
        self.low = low