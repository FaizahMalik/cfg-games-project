import random
from draw_turtle import TurtleDrawing

Donatello = TurtleDrawing()


# DONE split pick_word() into two functions, pick_word() and show_word()
# DONE replace_letter() returns self.display_word
# DONE sanitise_guess() returns False if there are special characters and self.guess if it was a letter.
# DONE split check_guess() and process_guess() into check_guess_if_previous(), add_previous_guess(), correct_word(),
# correct_guess(), display_correct_guess() and incorrect_guess()
# DONE instantiated Donatello in classes.py rather than draw_turtle.py


class Level:  # main parent class
    def __init__(self, username, words_list):
        self.chosen_word = None
        self.display_word = None
        self.attempts = None
        self.guess = None
        self.past_guesses = []
        self.username = username
        self.words_list = words_list
        self.turtle_drawings = {}

    def draw(self):  # helper function to incorrect_guess()
        if self.attempts in self.turtle_drawings:
            for draw_method in self.turtle_drawings[self.attempts]:
                method = getattr(Donatello, draw_method)
                method()
        else:
            print("MISSING KEY")  # <<< FOR TESTING

    def pick_word(self):
        """chooses a random word from given list"""
        self.chosen_word = random.choice(self.words_list)
        return self.chosen_word

    def show_word(self):
        """Returns hidden version of the word"""
        self.display_word = len(self.chosen_word) * "_ "
        return self.display_word

    def replace_letter(self):  # helper function to correct_guess()
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
        return self.display_word

    def sanitize_guess(self, letter):  # helper function to incorrect_guess()
        """takes an input, and cleans it, returns false if guess is not exclusively alphabetical"""
        self.guess = letter.lower().strip()
        if not self.guess.isalpha():
            print("No special characters.\n")  # no numbers, special characters or multiple words allowed
            return False
        # if type != str raise assert
        return self.guess

    def check_guess_if_previous(self):  # is a helper function to add_previous_guess()
        """checks whether the letter has already been guessed"""
        if self.guess in self.past_guesses:
            return False
        else:
            return True

    def add_previous_guess(
            self):  # relies on the results from check_guess_if_previous() | helper function to incorrect_guess()
        """If check_guess_if_previous() returns True, the letter is added to the list of self.past_guesses"""
        if self.check_guess_if_previous():
            self.past_guesses.append(self.guess)  # adds guessed letter to past guesses
            return self.past_guesses
        else:
            print(f'\nYou have already guessed the letter "{self.guess}"! Try again.')
            return False

    def correct_word(self):  # is a helper function to display_correct_guess()
        """checks if the the guess is equal to the chosen word, if yes it returns True and the full word"""
        if self.guess == self.chosen_word:  # they guess the whole word correctly
            self.display_word = self.chosen_word  # process will continue until it reaches ***
            return True, self.display_word
        else:
            return False

    def correct_guess(self):  # relies on the results from replace_letter() | helper function to display_correct_guess()
        """checks if guess exists in self.chosen_word, if so it calls the replaces_letter() function to replace
        letter """
        if self.guess in self.chosen_word:
            self.replace_letter()  # replaces display_word with correctly guessed letters
            return True
        else:
            return False

    def display_correct_guess(
            self):  # relies on the results from correct_word() and correct_guess() | helper function to incorrect_guess()
        """Displays the word or a letter if the guess was correct."""
        if self.correct_word():  # *** guessed all characters
            print(f"\n{self.display_word}\n\nWell done! The word was {self.chosen_word}.\n")
            return True, self.display_word
        elif self.correct_guess():
            print(f"\nCorrect!\n\n{self.display_word}")
            return True, self.display_word
        else:
            return False

    def incorrect_guess(self,
                        letter):  # relies on sanitise_guess, add_previous_guess(), display_correct_guess() & draw()
        """checks if guess is incorrect. If so self.attempts are added and incorrect messages are displayed."""
        if not self.sanitize_guess(letter):  # ensures that it is alphabetical input
            return False
        if not self.add_previous_guess():  # ensures that it hasn't already been guessed
            return False
        if not self.display_correct_guess():  # ensures that it is not a correct guess
            self.attempts -= 1

            if self.attempts <= 0:
                print(f"\nWrong guess!\n\nYou ran out of attempts. The word was: {self.chosen_word}. \n")
                return False
            else:
                self.draw()
                print(f"\nWrong guess! Please try again.\n\n{self.display_word}")
                return False, self.attempts


class Beginner(Level):  # this is our beginner level class

    def __init__(self, username, words_list):
        super().__init__(username, words_list)
        self.attempts = 9
        self.turtle_drawings = {
            8: ["draw_body"],
            7: ["draw_head"],
            6: ["draw_leg1", "draw_leg2"],
            5: ["draw_leg3", "draw_leg4"],
            4: ["draw_tail"],
            3: ["draw_back_middle"],
            2: ["draw_back_line"],
            1: ["draw_eyes"]
        }


class Medium(Level):  # this is our medium-difficulty subclass
    def __init__(self, username, words_list):
        super().__init__(username, words_list)
        self.attempts = 8
        self.turtle_drawings = {
            7: ["draw_body", "draw_head"],
            6: ["draw_leg1", "draw_leg2"],
            5: ["draw_leg3", "draw_leg4"],
            4: ["draw_tail"],
            3: ["draw_back_middle"],
            2: ["draw_back_line"],
            1: ["draw_eyes"]
        }


class Hard(Level):  # this is our beast mode subclass
    def __init__(self, username, words_list):
        super().__init__(username, words_list)
        self.attempts = 7
        self.turtle_drawings = {
            6: ["draw_body", "draw_head"],
            5: ["draw_leg1", "draw_leg2"],
            4: ["draw_leg3", "draw_leg4"],
            3: ["draw_tail", "draw_back_middle"],
            2: ["draw_back_line"],
            1: ["draw_eyes"]
        }

# test = Hard('v', ['python'])
# # #
# print(test.pick_word())
# print(test.show_word())
#
# print(test.sanitize_guess('l'))
# print(test.add_previous_guess())
# print(test.add_previous_guess())
# print(test.replace_letter())
# print(test.correct_word())
# print(test.display_correct_guess())
# test.incorrect_guess()

# DONE resize turtle screen
# DONE reorganise turtle drawing function
# DONE animate welcome and goodbye messages
# DONE show number of attempts
# DONE don't draw when user has already attempted a letter
# DONE show letters already guessed
# DONE split up and simplify methods
# DONE delete unnecessary __init__ attributes in subclasses
# DONE get rid of self. part in TurtleDrawing initialisation
# TODO check if guess is equal to word, then only allow 1 character inputs


# import random
# from draw_turtle import Donatello
#
#
# class Level:  # main parent class
#     def __init__(self, username, words_list):
#         self.chosen_word = None
#         self.display_word = None
#         self.attempts = None
#         self.guess = None
#         self.past_guesses = []
#         self.username = username
#         self.words_list = words_list
#         self.turtle_drawings = {}
#
#     def draw(self):
#         if self.attempts in self.turtle_drawings:
#             for draw_method in self.turtle_drawings[self.attempts]:
#                 method = getattr(Donatello, draw_method)
#                 method()
#         else:
#             print("MISSING KEY")  # <<< FOR TESTING
#
#     def pick_word(self):
#         """chooses a random word from given list & returns hidden version of the word"""
#         self.chosen_word = random.choice(self.words_list)
#         self.display_word = len(self.chosen_word) * "_ "
#         return self.display_word
#
#     def replace_letter(self):
#         """replaces _ with the guessed letter wherever that letter appears in the word"""
#         self.display_word = self.display_word.replace(' ', '')
#         new_display_word = ''
#
#         for i in range(0, len(self.chosen_word)):
#             if self.chosen_word[i] == self.guess or self.display_word[i] != '_':
#                 new_display_word += self.chosen_word[i]
#             else:
#                 new_display_word += '_'
#             new_display_word += ' '
#
#         self.display_word = new_display_word
#
#     def check_guess(self, letter):
#         """ensures only alphabetical characters present, checks if user guessed whole word and runs process_guess"""
#         if not self.sanitize_guess(letter):
#             return "No special characters.\n"  # no numbers, special characters or multiple words allowed
#         elif self.guess in self.past_guesses:
#             return f'\nYou have already guessed the letter "{self.guess}"! Try again.'
#         elif self.guess == self.chosen_word:  # they guess the whole word correctly
#             self.display_word = self.chosen_word  # process will continue until it reaches ***
#         self.past_guesses.append(self.guess)  # adds guessed letter to past guesses
#         return self.process_guess()
#
#     def sanitize_guess(self, letter):
#         """takes an input, and cleans it, returns false if guess is not exclusively alphabetical"""
#         self.guess = letter.lower().strip()
#         if not self.guess.isalpha():
#             return False
#         return True
#
#     def process_guess(self):
#         """decides whether self.guess is correct or not"""
#         if self.guess in self.chosen_word:
#             self.replace_letter()  # replaces display_word with correctly guessed letters
#
#             if self.display_word.replace(' ', '') == self.chosen_word:  # *** guessed all characters
#                 return f"\n{self.display_word}\n\nWell done! The word was {self.chosen_word}.\n"
#             else:
#                 return f"\nCorrect!\n\n{self.display_word}"
#
#         else:
#             self.attempts -= 1
#
#             if self.attempts <= 0:
#                 return f"\nWrong guess!\n\nYou ran out of attempts. The word was: {self.chosen_word}. \n"
#             else:
#                 self.draw()
#                 return f"\nWrong guess! Please try again.\n\n{self.display_word}"
#
#
# class Beginner(Level):  # this is our beginner level class
#
#     def __init__(self, username, words_list):
#         super().__init__(username, words_list)
#         self.attempts = 9
#         self.turtle_drawings = {
#             8: ["draw_body"],
#             7: ["draw_head"],
#             6: ["draw_leg1", "draw_leg2"],
#             5: ["draw_leg3", "draw_leg4"],
#             4: ["draw_tail"],
#             3: ["draw_back_middle"],
#             2: ["draw_back_line"],
#             1: ["draw_eyes"]
#         }
#
#
#
# class Medium(Level):  # this is our medium-difficulty subclass
#     def __init__(self, username, words_list):
#         super().__init__(username, words_list)
#         self.attempts = 8
#         self.turtle_drawings = {
#             7: ["draw_body", "draw_head"],
#             6: ["draw_leg1", "draw_leg2"],
#             5: ["draw_leg3", "draw_leg4"],
#             4: ["draw_tail"],
#             3: ["draw_back_middle"],
#             2: ["draw_back_line"],
#             1: ["draw_eyes"]
#         }
#
#
# class Hard(Level):  # this is our beast mode subclass
#     def __init__(self, username, words_list):
#         super().__init__(username, words_list)
#         self.attempts = 7
#         self.turtle_drawings = {
#             6: ["draw_body", "draw_head"],
#             5: ["draw_leg1", "draw_leg2"],
#             4: ["draw_leg3", "draw_leg4"],
#             3: ["draw_tail", "draw_back_middle"],
#             2: ["draw_back_line"],
#             1: ["draw_eyes"]
#         }
