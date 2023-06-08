import unittest

from model.enums.player_chars import PlayerChars
from model.game import Game


class GameTest(unittest.TestCase):
    def test_constructor(self):
        game = Game()
        self.assertEqual(game.first_player.player_char, PlayerChars.PLAYER_ONE)
        self.assertEqual(game.second_player.player_char, PlayerChars.PLAYER_TWO)
        self.assertEqual(game.first_player, game.current_player)

    def test_swap_players_swap_from_first_to_second(self):
        game = Game()
        self.assertEqual(game.first_player, game.current_player)
        game.swap_players()
        self.assertEqual(game.second_player, game.current_player)

    def test_swap_players_swap_from_second_to_first(self):
        game = Game()
        game.swap_players()
        self.assertEquals(game.second_player, game.current_player)
        game.swap_players()
        self.assertEqual(game.first_player, game.current_player)


if __name__ == '__main__':
    unittest.main()
