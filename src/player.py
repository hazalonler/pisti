from abc import abstractmethod
from rank import Rank
from suit import Suit


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.taken_cards = []
        self.pisti = 0
        self.score = 0

    def add_card(self, card):
        self.cards.append(card)  # add card from deck.deal()

    def __str__(self):
        return ' \n'.join(map(str, self.cards))

    @abstractmethod
    def play(self):
        raise NotImplementedError()

    def add_taken_cards(self, desk):
        self.taken_cards.extend(desk)

    def test(self, player_card):
        pass

    def calc_score_players(self):
        self.score += self.pisti * 10
        for card in self.taken_cards:
            if card.rank == Rank.ACE or card.rank == Rank.JACK:
                self.score += 1
            elif card.rank == Rank.TWO and card.suit == Suit.CLUBS:
                self.score += 2
            elif card.rank == Rank.TEN and card.suit == Suit.DIAMONDS:
                self.score += 3
        if len(self.taken_cards) > 26:
            self.score += 3




