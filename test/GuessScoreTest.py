import unittest
from src.GuessScore import GuessScore
from src.Player import Player


class TestGuessScore(unittest.TestCase):

    def setUp(self):
        self.playerPoetl = Player(2544,2003,1,1,"Lakers","Akron","SF")
        self.game = GuessScore()

    def test_correct_guess(self):
        self.assertEqual(self.game.score_guess("python", "python"), 10, "The score should be 10 for a correct guess")

    def test_incorrect_guess(self):
        self.assertEqual(self.game.score_guess("python", "java"), 0, "The score should be 0 for an incorrect guess")

if __name__ == '__main__':
    unittest.main()