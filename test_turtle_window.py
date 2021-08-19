import unittest
from turtle_window import TurtleWindow


class TestTurtleWindow(unittest.TestCase):
    """Instantiating a test object before every test case which can be used to ensure function executes correctly."""

    def setUp(self):
        self.raphael = TurtleWindow()

    """Clears the turtle window after every test case to ensure a clean screen for the next test case."""

    def tearDown(self):
        self.raphael.clear_window()

    def test_draw_word(self):
        self.assertTrue(self.raphael.draw_word('_ _ _ _'))

    def test_welcome_screen(self):
        self.assertTrue(self.raphael.welcome_screen())

    def test_goodbye_screen(self):
        self.assertTrue(self.raphael.goodbye_screen())

    def test_turtle_text(self):
        self.assertTrue(self.raphael.turtle_text('p'))
        self.assertTrue(self.raphael.turtle_text('#'))

    def test_turtle_focused_text(self):
        self.assertTrue(self.raphael.turtle_focused_text('p'))
        self.assertTrue(self.raphael.turtle_focused_text('test'))

    def test_draw_body(self):
        self.assertTrue(self.raphael.draw_body())

    def test_draw_head(self):
        self.assertTrue(self.raphael.draw_head())

    def test_draw_leg1(self):
        self.assertTrue(self.raphael.draw_leg1())

    def test_draw_leg2(self):
        self.assertTrue(self.raphael.draw_leg2())

    def test_draw_leg3(self):
        self.assertTrue(self.raphael.draw_leg3())

    def test_draw_leg4(self):
        self.assertTrue(self.raphael.draw_leg4())

    def test_draw_tail(self):
        self.assertTrue(self.raphael.draw_tail())

    def test_draw_back_middle(self):
        self.assertTrue(self.raphael.draw_back_middle())

    def test_draw_back_line(self):
        self.assertTrue(self.raphael.draw_back_line())

    def test_draw_eyes(self):
        self.assertTrue(self.raphael.draw_eyes())


if __name__ == '__main__':
    unittest.main()

# cd .. (so you are not in the test folder)
# then try

# python -m unittest -v test_turtle_window.py
