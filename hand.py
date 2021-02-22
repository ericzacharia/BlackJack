import tkinter as tk


class Hand:
    """Holds a collection of cards."""

    def __init__(self):
        self.cards = []

    def reset(self):
        """Clears collection of cards.
        No inputs or outputs."""
        self.cards = []

    def add(self, card):
        """Adds a card to the collection of cards.
        Inputs: Card object (card)
        No outputs."""
        self.cards.append(card)

    @property
    def total(self):
        sum_values = 0
        for card in self.cards:
            sum_values += card.card_value
        return sum_values

    def draw(self, canvas, start_x, start_y):
        """Draws the hand of cards on to the canvas starting at the location
        specified by start_x and start_y. Draws the cards horizontally along
        the x-axis.
        Inputs: Canvas Object (canvas), Integers (start_x, start_y)"""
        card_space = 0
        for card in self.cards:
            canvas.create_image(start_x + card_space, start_y, anchor=tk.NW, image=card.image)
            card_space += 85
