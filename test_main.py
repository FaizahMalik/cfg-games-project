import unittest
from unittest.mock import patch
from main import PlayGame

class TestPlayGame(unittest.TestCase):
    def setUp(self):
        pass

    def test_level_selection(self):
        #arrange
        game = PlayGame()

        #act
        hasLevelSelected = game.level_selection()

        #assert
        self.assertTrue(hasLevelSelected)

    def test_level_selection_will_retry(self):
        game = PlayGame()


