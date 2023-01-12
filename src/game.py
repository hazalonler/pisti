import random
from deck import Deck
from computer import Computer
from user import User
from rank import Rank


class Game:
    def __init__(self, debug):
        self.deal_cards_num = 4
        self.debug = debug
        self.desk = []
        self.players = self.__get_players_in_random_order()
        self.last_player_take_cards = None

    @staticmethod
    def __get_players_in_random_order():
        player1 = User('Player1')
        ai = Computer('AI')
        if random.getrandbits(1):
            return [player1, ai]
        else:
            return [ai, player1]

    def __check_player_cards(self, player):
        if len(self.desk) >= 2:
            if self.desk[-1].rank == self.desk[-2].rank:
                if len(self.desk) == 2:
                    player.pisti += 1
                player.add_taken_cards(self.desk)
                self.last_player_take_cards = player
                self.desk = []
            elif self.desk[-1].rank == Rank.JACK:
                player.add_taken_cards(self.desk)
                self.last_player_take_cards = player
                self.desk = []

    def __give_remaining_cards_on_desk(self):
        if self.desk:
            self.last_player_take_cards.add_taken_cards(self.desk)
        print('\nDesk is empty')

    def __check_winner(self):
        player_dict = {}
        winner_score = 0
        winner = None
        for player in self.players:
            if self.debug:
                for card in player.taken_cards:
                    print(card)
                print('taken by ---> {}'.format(player.name))
                print(player.score)
            player_dict.setdefault(player.name, player.score)
            if player.score > winner_score:
                winner_score = player.score
                winner = player.name
        print(player_dict)
        print('CONGRATULATIONS! Winner is {}'.format(winner))

    @staticmethod
    def __play_again():
        while True:
            try:
                ask_play_again = input('Do you want to play? Please enter Y or N: \n')
                if ask_play_again.lower() == 'y':
                    return True
                elif ask_play_again.lower() == 'n':
                    return False
            except:
                print('Please try again!')

    def play(self):
        game_on = True
        while game_on:
            self.__do_play()
            game_on = self.__play_again()

    def __do_play(self):
        deck = Deck()
        deck.shuffle()
        if not game.desk:
            for idx in range(self.deal_cards_num):
                game.desk.append(deck.deal())

        print('\nWelcome to the game!')
        print('The order of player is ')
        for player in self.players:
            print(''.join(player.name))

        playing = True
        while playing:
            for player in self.players:
                if not player.cards:
                    for idx_cards in range(self.deal_cards_num):
                        player.add_card(deck.deal())
                print('-----------------------')
                print('{}'.format(player.name))
                print('ON DESK')
                if self.desk:
                    print('Last Card: {}'.format(self.desk[-1]))
                    print('# of Card: {}\n'.format(len(self.desk)))
                else:
                    print('Last Card: Empty!')
                    print('# of Card: 0\n')

                player_card = player.play()
                player.test(player_card)
                self.desk.append(player_card)
                self.__check_player_cards(player)

                if not deck.deck and not player.cards:
                    if self.debug:
                        print("Deck and players' hand is empty")
                    playing = False

        self.__give_remaining_cards_on_desk()
        for player in self.players:
            player.calc_score_players()
        self.__check_winner()


game = Game(False)
game.play()
