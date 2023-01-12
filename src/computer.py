import random
from player import Player


class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        random_card = random.choice(self.cards)
        self.cards.remove(random_card)
        return random_card

    def test(self, player_card):
        print('{} is chosen'.format(player_card))
