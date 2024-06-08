from deck import Deck
from player import Player

class Game:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.discard_pile = []
        self.current_player_index = 0
        self.direction = 1
        self.current_color = None

    def start_game(self):
        for player in self.players:
            player.draw_cards(self.deck, 8)
        self.discard_pile.append(self.deck.draw())
        self.current_color = self.discard_pile[-1].color

    def next_turn(self):
        self.current_player_index = (self.current_player_index + self.direction) % len(self.players)

    def play_turn(self, player, card):
        if card.color == self.current_color or card.value == self.discard_pile[-1].value or card.value == 'Color Changer':
            self.discard_pile.append(player.play_card(card))
            if card.value == 'Color Changer':
                self.current_color = self.get_new_color()  # You need to implement this method
            else:
                self.current_color = card.color
            self.handle_special_card(card)
            self.next_turn()
        else:
            raise ValueError("Invalid card played")

    def handle_special_card(self, card):
        if card.value == 'Stop':
            self.next_turn()
        elif card.value == '+2':
            self.players[self.current_player_index].draw_cards(self.deck, 2)
            self.next_turn()
        elif card.value == 'Reverse':
            self.direction *= -1
        elif card.value == 'Plus':
            pass  # Allow player to play another card
        elif card.value == 'Taki':
            pass  # Allow player to play as many cards of the same color as they want
