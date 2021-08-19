import unittest
from main import level_selection, initiate_game, play_again, loading_screen, run_game, play_hangman, play_campaign


class TestMain(unittest.TestCase):
    """Instantiating a test object before every test case which can be used to ensure function executes correctly."""

    def test_play_again(self):
        self.assertTrue(play_again('tester'))

if __name__ == '__main__':
    unittest.main()

# cd .. (so you are not in the test folder)
# then try

# python -m unittest -v test_turtle_window.py
