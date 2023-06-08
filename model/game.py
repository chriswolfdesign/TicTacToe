from model.board import Board
from model.enums.player_chars import PlayerChars
from model.players.human_player import HumanPlayer


class Game:
    def __init__(self):
        self.first_player = HumanPlayer(PlayerChars.PLAYER_ONE)
        self.second_player = HumanPlayer(PlayerChars.PLAYER_TWO)
        self.current_player = self.first_player
        self.board = Board()

    def play(self):
        while not self.is_game_over():
            self.board.print_board()
            print()  # for spacing
            print(f"Current player: {self.current_player.player_char.value}")
            print()  # for spacing
            self.current_player.make_move(self.board)

            if self.board.has_player_won(self.current_player):
                print(f"Player {self.current_player.player_char.value} has won!")
                break

            if self.board.remaining_squares() == 0:
                print("DRAW!!!!")

            self.swap_players()

    def is_game_over(self):
        return self.board.has_player_won(self.first_player) or self.board.has_player_won(self.second_player) or \
               self.board.remaining_squares() == 0

    def swap_players(self):
        self.current_player = self.second_player if self.current_player == self.first_player else self.first_player
