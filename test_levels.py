import unittest
from levels import Beginner, Medium, Hard

#TODO put in a test folder?


class TestClasses(unittest.TestCase):

    """instantiates three objects that can be used for testing for all the functions. This function stores the outcome
    of the functions in an object. Otherwise it would reset for each function and the function would have a None object
    to work with which would fail the test. The downside is that they are all dependent on one another working."""
    @classmethod
    def setUpClass(cls):
        cls.l1 = Beginner(username='tester', words_list=['apple'])
        cls.l1.guess = 'a'
        cls.l1.past_guesses = ['a']
        cls.l1.chosen_word = 'apple'
        cls.l1.display_word = '_ _ _ _ _ '

        cls.l2 = Medium(username='tester', words_list=['orange'])
        cls.l2.guess = 'l'
        cls.l2.past_guesses = ['p']
        cls.l2.chosen_word = 'orange'
        cls.l2.display_word = '_ _ _ _ _ _ '

        cls.l3 = Beginner(username='tester2', words_list=['mermaid'])
        cls.l3.guess = 'mermaid'
        cls.l3.chosen_word = 'mermaid'

        cls.l4 = Hard(username='tester', words_list=['unicorn'])
        cls.l4.guess = '#'



    # test that module was successfully imported? can't be run simultaneously as test_incorrect_guess()
    def test_draw(self):
        pass

    def test_pick_word(self):
        self.assertEqual(self.l1.pick_word(), 'apple')
        self.assertEqual(self.l2.pick_word(), 'orange')
        self.assertEqual(self.l4.pick_word(), 'unicorn')
        self.assertEqual(self.l3.pick_word(), 'mermaid')

    def test_show_word(self):
        self.assertEqual(self.l1.show_word(), '_ _ _ _ _ ')
        self.assertEqual(self.l2.show_word(), '_ _ _ _ _ _ ')
        self.assertEqual(self.l3.show_word(), '_ _ _ _ _ _ _ ')
        self.assertEqual(self.l4.show_word(), '_ _ _ _ _ _ _ ')

    def test_replace_letter(self):
        self.assertEqual(self.l1.replace_letter(), 'a _ _ _ _ ')
        self.assertEqual(self.l2.replace_letter(), '_ _ _ _ _ _ ')

    # # can't be run simultaneously as test_incorrect_guess()
    # def test_sanitise_guess(self):
    #     self.assertFalse(self.l4.sanitize_guess(self.l4.guess))
    #     self.assertEqual(self.l1.sanitize_guess(self.l1.guess), 'a')
    #     self.assertEqual(self.l2.sanitize_guess(self.l2.guess), 'l')

    def test_check_guess_if_previous(self):
        self.assertFalse(self.l1.check_guess_if_previous())
        self.assertTrue(self.l2.check_guess_if_previous())

    ## can't be tested simultaneously as test_check_guess_if_previous or test_incorrect_guess
    # def test_add_previous_guess(self):
    #     self.assertEqual(self.l2.add_previous_guess(), ['p', 'l'])
    #     self.assertFalse(self.l1.add_previous_guess())

    ## can't be tested simultaneously as test_display_correct_guess
    # def test_correct_word(self):
    #     self.assertTrue(self.l3.correct_word())
    #     self.assertFalse(self.l1.correct_word())
    #     self.assertFalse(self.l2.correct_word())
    #
    # ## can't be tested simultaneously as test_display_correct_guess
    # def test_correct_guess(self):
    #     self.assertTrue(self.l1.correct_guess())
    #     self.assertFalse(self.l2.correct_guess())

    # # can't be tested simultaneously as test_incorrect_guess()
    # def test_display_correct_guess(self):
    #     self.assertTrue(self.l3.display_correct_guess())
    #     self.assertTrue(self.l1.display_correct_guess())
    #     self.assertFalse(self.l2.display_correct_guess())

    def test_incorrect_guess(self):
        self.assertFalse(self.l4.incorrect_guess(self.l4.guess))
        self.assertEqual(self.l2.incorrect_guess(self.l2.guess), (False, 7))


if __name__ == '__main__':
    unittest.main()

## to run unittests: python -m unittest test/test_hw_session9.py

# try:
# python -m unittest -v test/test_hw_session9.py
# if that doesn't work try:
# cd .. (so you are not in the test folder)
# and then: python -m unittest -v test/test_hw_session9.py

# python -m unittest -v test_levels.py
