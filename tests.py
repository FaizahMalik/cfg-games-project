import unittest
from src.run_wordguesser.py import validate_pin_code, validate_withdrawal_amount, log_in


class TestHangman(unittest.TestCase):

    # test if pick_word() chooses a word from the list given
    # mock?
    def test_word_is_in_list(self):
        expected = True
        result = validate_pin_code(pin="0000")
        self.assertEqual(expected, result)

    # test whether underscore is replaced by letter
    def test_underscore_is_replaced(self):
        expected = True
        result = validate_pin_code(pin="0000")
        self.assertEqual(expected, result)

    # test that input is a letter
    def test_input_is_letter(self):
        pass

    # IF WE HAVE TIME
    # test if exception is raised if input is not a letter
    def test_if_exception_is_raised_if_input_is_not_letter(self):
        input = 1
        with self.assertRaises(Exception):
            validate_withdrawal_amount(input)

    # test to ensure that word is hidden
    def test_word_is_hidden(self):
        pass

    # test while loop breaks
    def test_if_while_loop_breaks(self):
        pass

    # test if turtle is drawing when answer is incorrect
    def test_if_incorrect_answer_draws_turtle(self):
        pass

    # test if number of attempts is reduced when answer is incorrect
    def test_if_attempts_is_reduced(self):
        pass



if __name__ == '__main__':
    unittest.main()

## to run unittests: python -m unittest test/test_hw_session9.py

# try:
# python -m unittest -v test/test_hw_session9.py
# if that doesn't work try:
# cd .. (so you are not in the test folder)
# and then: python -m unittest -v test/test_hw_session9.py