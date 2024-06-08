import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        colors = ['Red', 'Blue', 'Green', 'Yellow']
        values = list(range(1, 10)) + ['Taki', 'Stop', '+2', 'Reverse', 'Color Changer', 'Plus']
        deck = [Card(color, value) for color in colors for value in values]
        random.shuffle(deck)
        return deck

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]

    def draw(self):
        return self.cards.pop()