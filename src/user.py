from player import Player


class User(Player):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        while True:
            try:
                self.__enum_cards()
                chosen_card = int(input("Choose one of them: \n"))
                if len(self.cards) >= chosen_card >= 1:
                    card = self.cards[chosen_card - 1]
                    self.cards.remove(card)
                    return card
                else:
                    print('Enter a valid number between 1-{}'.format(len(self.cards)))
            except:
                print('Please enter a number')

    def __enum_cards(self):
        for idx_card, name_card in enumerate(self.cards, 1):
            print("{}. {}".format(idx_card, name_card))

