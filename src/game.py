import random
from abc import abstractmethod


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')  # TODO convert these to enum
        ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        return ' \n'.join(map(str, self.deck))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.taken_cards = []
        self.pisti = 0
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)  # add card from deck.deal()

    def __str__(self):
        return ' \n'.join(map(str, self.cards))

    @abstractmethod
    def play(self):
        raise NotImplementedError()

    def value_cards(self):
        self.value += self.pisti * 10
        for card in self.taken_cards:
            # TODO use enums in here
            if card.rank == 'Ace' or card.rank == 'Jack':
                self.value += 1
            elif card.__str__() == 'Two of Clubs':  # TODO do not str method to check equality
                self.value += 2
            elif card.__str__() == 'Ten of Diamonds':
                self.value += 3
        if len(self.taken_cards) > 26:
            self.value += 3


class User(Player):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        cards_to_list = []
        for element in self.cards:
            cards_to_list.append(element.__str__())
        index_cards = list(enumerate(cards_to_list, 1))
        # TODO print this pretty
        while True:
            try:
                chosen_card = int(input("Choose one of them: \n{}".format(index_cards)))
                if len(index_cards) >= chosen_card >= 1:
                    card = self.cards[chosen_card - 1]
                    self.cards.remove(card)
                    return card
                else:
                    print('Enter a valid number between 1-4')  # TODO dynamic input range
            except:
                print('Please enter a number')


class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        # for element in self.cards:
        # if element.rank == last_card.rank:
        # self.cards.remove(element)
        # return element
        # elif element.rank == 'Jack':
        # self.cards.remove(element)
        # return element

        random_card = random.choice(self.cards)
        self.cards.remove(random_card)
        return random_card


class Game:
    def __init__(self, debug):
        self.debug = debug
        self.desk = []
        self.players = self.__get_players_in_random_order()

    @staticmethod
    def __get_players_in_random_order():
        player1 = User('Player1')
        ai = Computer('AI')
        if random.getrandbits(1):
            return [player1, ai]
        else:
            return [ai, player1]

    def __check_cards(self, player):

        if len(self.desk) >= 2:
            if self.desk[-1].rank == self.desk[-2].rank:
                if len(self.desk) == 2:
                    player.pisti += 1
                    print('{} make PISTI'.format(player.name))
                # TODO convert usage to player.add_take_cards(self.desk)
                player.taken_cards.extend(self.desk)
                self.desk = []
            elif self.desk[-1].rank == 'Jack':  # TODO enum
                player.taken_cards.extend(self.desk)
                self.desk = []

    @staticmethod
    def show_player_hand(player):  # TODO remove this
        print("\n-->Player's Hand: ")
        for card in player.cards:
            print(card)

    def desk_check(self, players):
        if self.desk:
            # TODO latest taker should get the remain cards
            players[-1].taken_cards.extend(self.desk)  # TODO player taken cards
            print('Desk is empty')

    def __winner_check(self, players):
        player_dict = {}
        for player in players:
            if self.debug:
                for card in player.taken_cards:
                    print(card)
                print('taken by ---> {}'.format(player.name))
                print(player.value)
            player_dict.setdefault(player.name, player.value)
        print(player_dict)  # TODO print pretty and congrats the winner

    def play(self):
        new_deck = Deck()
        new_deck.shuffle()
        if not game.desk:
            for idx in range(4):
                game.desk.append(new_deck.deal())

        playing = True
        while playing:
            for player in self.players:
                if not player.cards:
                    for idx_cards in range(4):  # TODO create global static variable for this
                        player.add_card(new_deck.deal())
                print('\nIt is the turn of {}'.format(player.name))
                if self.desk:
                    print('\n--The last card on the desk is {} and there are {} cards in desk--'.format(self.desk[-1],
                                                                                                        len(self.desk)))
                else:
                    print('\n-----Desk is empty-----')

                self.show_player_hand(player)
                player_card = player.play()
                self.desk.append(player_card)
                self.__check_cards(player)

                if not new_deck.deck and not player.cards:
                    print("Deck and players' hand is empty")
                    playing = False

        self.desk_check(self.players) # TODO more meaningful name
        print('Now, it is the time to learn who is winner')
        for player in self.players:
            player.value_cards()  # TODO rename this, more meaningful
        self.__winner_check(self.players)  # complete calculation and print the right winner


game = Game(False)
game.play()
