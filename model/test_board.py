import unittest

from model.board import Board
from model.enums.player_chars import PlayerChars
from model.players.human_cli_player import HumanCLIPlayer


class BoardTest(unittest.TestCase):
    def test_constructor(self):
        board = Board()
        self.assertEqual(board.SIZE, 3)
        self.assertEqual(len(board.board), 3)
        self.assertEqual(len(board.board[0]), 3)

    def test_make_move_legal_move(self):
        player = HumanCLIPlayer(PlayerChars.PLAYER_ONE)
        board = Board()
        self.assertTrue(board.make_move(1, 1, player))
        self.assertEqual(board.board[1][1], player.player_char)

    def test_make_move_already_made(self):
        board = Board()
        player_one = HumanCLIPlayer(PlayerChars.PLAYER_ONE)
        player_two = HumanCLIPlayer(PlayerChars.PLAYER_TWO)
        self.assertTrue(board.make_move(1, 1, player_one))
        self.assertEqual(board.board[1][1], player_one.player_char)
        self.assertFalse(board.make_move(1, 1, player_two))
        self.assertEqual(board.board[1][1], player_one.player_char)

    def test_make_move_row_too_low(self):
        board = Board()
        player = HumanCLIPlayer(PlayerChars.PLAYER_TWO)
        self.assertFalse(board.make_move(-1, 1, player))

    def test_make_move_row_too_high(self):
        board = Board()
        player = HumanCLIPlayer(PlayerChars.PLAYER_ONE)
        self.assertFalse(board.make_move(3, 1, player))

    def test_make_move_col_too_low(self):
        board = Board()
        player = HumanCLIPlayer(PlayerChars.PLAYER_TWO)
        self.assertFalse(board.make_move(1, -1, player))

    def test_make_move_col_too_high(self):
        board = Board()
        player = HumanCLIPlayer(PlayerChars.PLAYER_ONE)
        self.assertFalse(board.make_move(1, 3, player))

    def test_has_player_won_by_rows_has_won_by_first_row(self):
        board = Board()
        player = HumanCLIPlayer(PlayerChars.PLAYER_TWO)
        board.make_move(0, 0, player)
        board.make_move(0, 1, player)
        board.make_move(0, 2, player)
        self.assertTrue(board.has_player_won(player))

    def test_has_player_won_by_rows_has_not_won(self):
        board = Board()
        player = HumanCLIPlayer(PlayerChars.PLAYER_ONE)
        board.make_move(0, 0, player)
        board.make_move(0, 1, player)
        self.assertFalse(board.has_player_won(player))

    def test_has_player_won_by_cols_won_by_last_col(self):
        board = Board()
        player = HumanCLIPlayer(PlayerChars.PLAYER_TWO)
        board.make_move(0, 2, player)
        board.make_move(1, 2, player)
        board.make_move(2, 2, player)
        self.assertTrue(board.has_player_won(player))

    def test_has_player_won_by_diagonals_won_by_main_diagonal(self):
        board = Board()
        player = HumanCLIPlayer(PlayerChars.PLAYER_ONE)
        board.make_move(0, 0, player)
        board.make_move(1, 1, player)
        board.make_move(2, 2, player)
        self.assertTrue(board.has_player_won(player))

    def test_has_player_won_by_diagonals_won_by_inverse_diagonal(self):
        board = Board()
        player = HumanCLIPlayer(PlayerChars.PLAYER_TWO)
        board.make_move(2, 0, player)
        board.make_move(1, 1, player)
        board.make_move(0, 2, player)
        self.assertTrue(board.has_player_won(player))

    def test_has_player_won_player_has_not_won(self):
        board = Board()
        player = HumanCLIPlayer(PlayerChars.PLAYER_ONE)
        board.make_move(0, 0, player)
        board.make_move(2, 2, player)
        board.make_move(0, 2, player)
        board.make_move(2, 0, player)
        self.assertFalse(board.has_player_won(player))

    def test_remaining_squares_empty_board(self):
        board = Board()
        self.assertEqual(board.remaining_squares(), board.SIZE**2)

    def test_remaining_squares_some_squares_taken(self):
        board = Board()
        player = HumanCLIPlayer(PlayerChars.PLAYER_TWO)
        board.make_move(0, 0, player)
        board.make_move(1, 1, player)
        board.make_move(1, 2, player)
        board.make_move(2, 0, player)
        self.assertEqual(board.remaining_squares(), board.SIZE**2 - 4)

    def test_remaining_squares_all_squares_taken(self):
        board = Board()
        player = HumanCLIPlayer(PlayerChars.PLAYER_ONE)
        for i in range(board.SIZE):
            for j in range(board.SIZE):
                board.make_move(i, j, player)
        self.assertEqual(board.remaining_squares(), 0)


if __name__ == '__main__':
    unittest.main()
