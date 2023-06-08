from model.players.human_player import HumanPlayer


class HumanCLIPlayer(HumanPlayer):
    def __init__(self, player_char):
        super().__init__(player_char)

    def make_move(self, board):
        valid_move = False

        while not valid_move:
            row = int(input("Row: "))
            col = int(input("Col: "))

            valid_move = board.make_move(row, col, self)

            if not valid_move:
                print("Illegal move -- try again")
