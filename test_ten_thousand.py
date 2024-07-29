import unittest
from ten_thousand import TenThousand

class TestTenThousand(unittest.TestCase):
    def setUp(self):
        self.game = TenThousand()

    def test_gets_valid_combinations(self):  
        combinations = self.game.valid_combinations([1, 1, 1, 2, 3, 5, 6])
        self.assertCountEqual(combinations, [
                              (1000, 3), (50, 1), (100, 1), (200, 2), (150, 2), (250, 3), (1050, 4)])

    def test_adds_dice(self):
        self.assertEqual(self.game.player_1_score, 0)
        self.assertEqual(self.game.dice_remaining, 7)
        
        self.game.add_dice((50, 1))
        
        self.assertEqual(self.game.current_score, 50)
        self.assertEqual(self.game.dice_remaining, 6)
        
    def test_setup_next_turn(self):
        self.game.dice_remaining = 4
        self.game.current_score = 100 
        
        self.assertTrue(self.game.is_first_players_turn)
        self.assertEqual(self.game.player_1_score, 0)
        self.assertEqual(self.game.current_score, 100)
        
        self.game.setup_next_turn()
        
        self.assertFalse(self.game.is_first_players_turn)
        self.assertEqual(self.game.player_1_score, 100)
        self.assertEqual(self.game.current_score, 0)
        
