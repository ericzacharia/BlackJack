import tkinter as tk
from tkinter import font
from abc import ABC, abstractmethod
from card import Card
from hand import Hand
from deck import Deck


class GameGUI(ABC):

    def __init__(self, window):
        self._window = window
        self._canvas_width = 1024
        self._canvas_height = 400
        self._canvas = tk.Canvas(window, width=self._canvas_width, height=self._canvas_height)
        self._canvas.pack()
        window.bind("<Key>", self._keyboard_event)

    def _keyboard_event(self, event):
        key = str(event.char)

        if key == 'h':
            self.player_hit()
        elif key == 's':
            self.player_stand()
        elif key == 'r':
            self.reset()

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def player_hit(self):
        pass

    @abstractmethod
    def player_stand(self):
        pass


class BlackJack(GameGUI):
    """Implements a simple version of the BlackJack card game and displays the
    game to the player."""

    def __init__(self, window):
        super().__init__(window)
        self.player_wins = 0
        self.dealer_wins = 0
        self.game_status = 'In Progress...'
        self.in_progress = True
        self.status_color = 'green'
        self.text_font = tk.font.Font(family='Helvetica', size=15, weight='bold')
        Card.load_images()
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def refresh_canvas(self):
        """Method which refreshed the canvas (text and player/dealer cards)
        based on the updated BlackJack attributes.
        No inputs or outputs."""
        self._canvas.delete(tk.ALL)
        self._canvas.create_text(10, 10, anchor=tk.NW, fill='black', font=self.text_font,
                                 text=f'Player Hand Total: {self.player_hand.total}')
        self._canvas.create_text(10, 150, anchor=tk.NW, font=self.text_font, fill='black',
                                 text=f'Dealer Hand Total: {self.dealer_hand.total}')
        self._canvas.create_text(100, 300, anchor=tk.NW, fill=self.status_color, font=self.text_font,
                                 text=f'Game Status: {self.game_status}')
        self._canvas.create_text(10, 330, anchor=tk.NW, fill='black', font=self.text_font,
                                 text=f'Dealer Wins: {self.dealer_wins}')
        self._canvas.create_text(10, 355, anchor=tk.NW, fill='black', font=self.text_font,
                                 text=f'Player Wins: {self.player_wins}')
        self.player_hand.draw(self._canvas, 10, 35)
        self.dealer_hand.draw(self._canvas, 10, 175)

    def reset(self):
        """Restarts the game (resets player/dealer hands, deals two cards for
        the player and dealer, and checks for the edge case of two Aces).
        No inputs or outputs."""
        self.player_hand.reset()
        self.dealer_hand.reset()
        self.player_hand.add(self.deck.deal())
        self.player_hand.add(self.deck.deal())
        self.dealer_hand.add(self.deck.deal())
        self.dealer_hand.add(self.deck.deal())
        # Checking for edge cases where player/dealer (or both) have two aces
        if self.player_hand.total == 22 and self.dealer_hand.total == 22:
            self.status_color = 'red'
            self.game_status = "TIE Game... Press 'r' to start game"
            self.in_progress = False
        elif self.player_hand.total == 22:
            self.status_color = 'red'
            self.game_status = "Dealer WINS... Press 'r' to start game"
            self.dealer_wins += 1
            self.in_progress = False
        elif self.dealer_hand.total == 22:
            self.status_color = 'red'
            self.game_status = "Player WINS... Press 'r' to start game"
            self.player_wins += 1
            self.in_progress = False
        else:
            self.game_status = 'In Progress...'
            self.status_color = 'green'
            self.in_progress = True
        self.refresh_canvas()

    def player_hit(self):
        """Functionality for when a player 'hits'. If the player's total score
        is over 21, the player loses.
        No inputs or outputs."""
        if self.in_progress:
            self.player_hand.add(self.deck.deal())
            if self.player_hand.total > 21:
                self.status_color = 'red'
                self.game_status = "Dealer WINS... Press 'r' to start game"
                self.dealer_wins += 1
                self.in_progress = False
            self.refresh_canvas()

    def player_stand(self):
        """Functionality for when a player 'stands'. The dealer automatically
        draws cards until their total score is 17 or greater. Based on the
        dealer's score, determines who wins.
        No inputs or outputs."""
        if self.in_progress:
            while self.dealer_hand.total < 17:
                self.dealer_hand.add(self.deck.deal())
            if self.dealer_hand.total > 21 or self.dealer_hand.total < self.player_hand.total:
                self.status_color = 'red'
                self.game_status = "Player WINS... Press 'r' to start game"
                self.player_wins += 1
            elif self.player_hand.total == self.dealer_hand.total:
                self.status_color = 'red'
                self.game_status = "TIE Game... Press 'r' to start game"
            else:
                self.status_color = 'red'
                self.game_status = "Dealer WINS... Press 'r' to start game"
                self.dealer_wins += 1
            self.in_progress = False
            self.refresh_canvas()


def main():
    window = tk.Tk()
    window.title("Blackjack")

    game = BlackJack(window)
    game.reset()

    window.mainloop()


if __name__ == "__main__":
    main()
