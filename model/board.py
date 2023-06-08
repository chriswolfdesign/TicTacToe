from model.enums.player_chars import PlayerChars


class Board:
    def __init__(self):
        self.SIZE = 3
        self.board = []

        for i in range(self.SIZE):
            self.board.append([PlayerChars.EMPTY] * self.SIZE)

    def make_move(self, row, col, player):
        if row < 0 or row >= self.SIZE:
            return False
        if col < 0 or col >= self.SIZE:
            return False
        if self.board[row][col] != PlayerChars.EMPTY:
            return False
        self.board[row][col] = player.player_char
        return True

    def has_player_won(self, player):
        return self.has_player_won_by_rows(player) or \
               self.has_player_won_by_cols(player) or \
               self.has_player_won_by_diagonals(player)

    def has_player_won_by_rows(self, player):
        for i in range(self.SIZE):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player.player_char:
                return True
        return False

    def has_player_won_by_cols(self, player):
        for i in range(self.SIZE):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player.player_char:
                return True
        return False

    def has_player_won_by_diagonals(self, player):
        return self.board[0][0] == self.board[1][1] == self.board[2][2] == player.player_char or \
               self.board[2][0] == self.board[1][1] == self.board[0][2] == player.player_char

    def print_board(self):
        for row in self.board:
            print(f"[{row[0].value}] [{row[1].value}] [{row[2].value}]")

    def remaining_squares(self):
        remaining = 0

        for row in self.board:
            for tile in row:
                if tile == PlayerChars.EMPTY:
                    remaining += 1

        return remaining
