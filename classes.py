import random
from draw_turtle import Donatello


class Level:  # main parent class
    def __init__(self, username, words_list):
        self.username = username
        self.words_list = words_list


class Beginner(Level):  # this is our beginner level class

    def __init__(self, username, words_list):
        super().__init__(username, words_list)
        self.chosen_word = None
        self.display_word = None
        self.attempts = 9  # could be modified according to difficulty lvl
        self.past_guesses = None  # not implemented, but could be used to warn user if they have guessed a letter twice
        self.guess = None
        # self.difficulty = 0
        # self.password = 0

    def pick_word(self):
        """chooses a random word from given list & returns hidden version of the word"""
        self.chosen_word = random.choice(self.words_list)
        self.display_word = len(self.chosen_word) * "_ "
        return self.display_word

    def replace_letter(self):
        """replaces _ with the guessed letter wherever that letter appears in the word"""
        self.display_word = self.display_word.replace(' ', '')
        new_display_word = ''

        for i in range(0, len(self.chosen_word)):
            if self.chosen_word[i] == self.guess or self.display_word[i] != '_':
                new_display_word += self.chosen_word[i]
            else:
                new_display_word += '_'
            new_display_word += ' '

        self.display_word = new_display_word

    def sanitize_guess(self, letter):
        self.guess = letter.lower().strip()
        if self.guess.isAlpha():
            return True
        else:
            return False

    def draw(self):
        if self.attempts == 8:
            Donatello.draw_body()
        elif self.attempts == 7:
            Donatello.draw_head()
        elif self.attempts == 6:
            Donatello.draw_leg1()
            Donatello.draw_leg2()
        elif self.attempts == 5:
            Donatello.draw_leg3()
            Donatello.draw_leg4()
        elif self.attempts == 4:
            Donatello.draw_tail()
        elif self.attempts == 3:
            Donatello.draw_back_middle()
        elif self.attempts == 2:
            Donatello.draw_back_line()
        elif self.attempts == 1:
            Donatello.draw_eyes()

    def guess_letter(self):
        """takes an input (letter or word), and decides whether it is correct or not"""
        if self.guess == self.chosen_word:  # they guess the whole word correctly
            self.display_word = self.chosen_word  # process will continue until it reaches ***

        if self.guess in self.chosen_word:
            self.replace_letter()  # replaces display_word with correctly guessed letters

            if self.display_word.replace(' ', '') == self.chosen_word:  # *** guessed all characters
                return f"\n{self.display_word}\n\nWell done! The word was {self.chosen_word}.\n"
            else:
                return f"\nCorrect! \n\n{self.display_word}"

        elif self.attempts <= 0:
            return "Run out of guesses, the word was: {}. \n".format(self.chosen_word)  # run out of guesses
        else:
            self.attempts -= 1
            self.draw()
            return f"\nWrong guess! Please try again.\n\n{self.display_word}"


class Medium(Level):  # this is our medium-difficulty subclass
    def __init__(self, username, words_list):
        super().__init__(username, words_list)
        self.chosen_word = None
        self.display_word = None
        self.attempts = 8
        self.past_guesses = None
        self.guess = None
        # self.difficulty = 0
        # self.password = 0


class Hard(Level):  # this is our beast mode subclass
    def __init__(self, username, words_list):
        super().__init__(username, words_list)
        self.chosen_word = None
        self.display_word = None
        self.attempts = 7
        self.past_guesses = None
        self.guess = None
        # self.difficulty = 0
        # self.password = 0
