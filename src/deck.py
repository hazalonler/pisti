import random
from rank import Rank
from suit import Suit
from card import Card


class Deck:
    def __init__(self):
        self.deck = []
        for suit in Suit:
            for rank in Rank:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        return ' \n'.join(map(str, self.deck))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
