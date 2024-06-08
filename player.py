class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_cards(self, deck, num_cards):
        self.hand.extend(deck.deal(num_cards))

    def play_card(self, card):
        self.hand.remove(card)
        return card