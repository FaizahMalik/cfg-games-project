import unittest
from main import PlayGame

class TestPlayGame(unittest.TestCase):
    def setUp(self):
        self.test = PlayGame()

    def test_level_selection(self):
        self.assertTrue(self.test.level_selection())


if __name__ == '__main__':
    unittest.main()