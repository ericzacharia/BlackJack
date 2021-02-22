from random import shuffle
from card import Card


class Deck:
    """Holds a collection of cards. Contains functionality for shuffling and
    dealing cards."""

    CARD_MAPPING = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
        'Ace': 11
    }

    def __init__(self):
        self.undealt_deck = []
        self.dealt_deck = []

        for card_type, card_value in self.CARD_MAPPING.items():
            self.undealt_deck.append(Card(Card.CLUBS, card_value, card_type))
            self.undealt_deck.append(Card(Card.DIAMONDS, card_value, card_type))
            self.undealt_deck.append(Card(Card.HEARTS, card_value, card_type))
            self.undealt_deck.append(Card(Card.SPADES, card_value, card_type))
        shuffle(self.undealt_deck)

    def deal(self):
        """Removes the top card on the deck and returns it. Also shuffles
        the deck when there are only 13 cards remaining.
        No inputs.
        Outputs: Card object"""
        if self.size == 13:
            self.shuffle()
        dealt_card = self.undealt_deck.pop(0)
        self.dealt_deck.append(dealt_card)
        return dealt_card

    @property
    def size(self):
        return len(self.undealt_deck)

    def shuffle(self):
        """Randomly shuffles all the already dealt cards and places them at
        the bottom of the deck.
        No inputs or outputs."""
        shuffle(self.dealt_deck)
        self.undealt_deck += self.dealt_deck
        self.dealt_deck = []

