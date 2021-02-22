from PIL import ImageTk
import os


class Card:
    """Holds all information on the game's cards."""

    CLUBS = 'clubs'
    DIAMONDS = 'diamonds'
    HEARTS = 'hearts'
    SPADES = 'spades'

    card_images = {}

    def __init__(self, card_suit, card_value, card_type):
        self.card_suit = card_suit
        self.card_value = card_value
        self.card_type = card_type

    @classmethod
    def load_images(cls):
        """Loads all images inside images directory as tk.PhotoImage objects.
        No inputs or outputs."""
        img_directory = os.getcwd() + '/images/'
        image_files = os.listdir(img_directory)
        for image in image_files:
            if image not in ['black_joker.gif', 'red_joker.gif', '.DS_Store']:
                card_name = image.split('.')[0]
                cls.card_images[card_name] = ImageTk.PhotoImage(file=img_directory + image)

    @property
    def value(self):
        return self.card_value

    @property
    def image(self):
        if self.card_type == 'Ace':
            return self.card_images[f'1_of_{self.card_suit}']
        elif self.card_type == 'Jack':
            return self.card_images[f'11_of_{self.card_suit}']
        elif self.card_type == 'Queen':
            return self.card_images[f'12_of_{self.card_suit}']
        elif self.card_type == 'King':
            return self.card_images[f'13_of_{self.card_suit}']
        else:
            return self.card_images[f'{self.value}_of_{self.card_suit}']
