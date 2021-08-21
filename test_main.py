import unittest
from main import PlayGame, LevelsMode, CampaignMode, ask_mode, ask_name
from levels import Beginner


class TestPlayGame(unittest.TestCase):
    def setUp(self):
        self.test = PlayGame()
        # self.level = Beginner
        # self.test.username = 'V'
        # self.test.words_list = ['test']
        self.test.game1 = Beginner('v', ['car'])

    """Turtle will ask for input twice."""

    def test_play_again(self):
        # type y
        self.assertTrue(self.test.play_again())
        # type n
        self.assertFalse(self.test.play_again())

    def test_loading_screen(self):
        self.assertTrue(self.test.loading_screen('This is a test.'))


# PROBLEMS TO TEST
# def test_run_game(self):
#     self.assertTrue(self.test.run_game())

class TestLevelsMode(unittest.TestCase):
    def setUp(self):
        self.test2 = LevelsMode('V')
        self.test2.selected_level = 'Beginner'

    """For testing type beginner or medium or hard, type y or n, type car"""
    # def test_initiate_levels(self):
    #     self.assertTrue(self.test2.initiate_levels())

    """First type y and car, when prompted a second time type n"""

    def test_set_words_list(self):
        self.assertFalse(self.test2.set_words_list())
        self.assertTrue(self.test2.set_words_list())

    # Difficult to test
    def test_play_levels(self):
        pass


    ## HELPER FUNCTIONS - can't be tested with test_initiate_levels ##

    """Type beginner, medium or hard"""
    # def test_ask_level(self):
    #     self.assertTrue(self.test2.ask_level())
    #
    # def test_check_level(self):
    #     self.assertTrue(self.test2.check_level())
    #
    # """Type y and then n"""
    # can't be tested with set_words_list()
    # def test_ask_if_custom(self):
    #     self.assertTrue(self.test2.ask_if_custom_list())
    #     self.assertFalse(self.test2.ask_if_custom_list())


class TestCampaignMode(unittest.TestCase):
    def setUp(self):
        self.test3 = CampaignMode('V')

    # DIFFICULT TO TEST
    def test_play_campaign(self):
        pass


class TestMain(unittest.TestCase):

## Not working at the moment
    # def test_ask_mode(self):
    #     self.assertEqual(ask_mode(), 'campaign')

    ## HELPER FUNCTION - can't be run with ask_mode()
    """type test"""
    def test_ask_name(self):
        self.assertEqual(ask_name(), 'test')


if __name__ == '__main__':
    unittest.main()

# cd .. (so you are not in the test folder)
# then try

# python -m unittest -v test_main.py