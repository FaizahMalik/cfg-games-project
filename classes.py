import random
from draw_turtle import Donatello


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

    def draw(self):
        if self.attempts in self.turtle_drawings:
            for draw_method in self.turtle_drawings[self.attempts]:
                method = getattr(Donatello, draw_method)
                method()
        else:
            print("MISSING KEY")  # <<< FOR TESTING

    def pick_word(self):
        """chooses a random word from given list & returns hidden version of the word"""
        self.chosen_word = random.choice(self.words_list)
        self.display_word = len(self.chosen_word) * "_ "
        Donatello.draw_word(self.display_word)
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

    def check_guess(self, letter):
        """ensures only alphabetical characters present, checks if user guessed whole word and runs process_guess"""
        if not self.sanitize_guess(letter):
            return "No special characters.\n"  # no numbers, special characters or multiple words allowed
        elif self.guess in self.past_guesses:
            return f'\nYou have already guessed the letter "{self.guess}"! Try again.'
        elif self.guess == self.chosen_word:  # they guess the whole word correctly
            self.display_word = self.chosen_word  # process will continue until it reaches ***
        self.past_guesses.append(self.guess)  # adds guessed letter to past guesses
        return self.process_guess()

    def sanitize_guess(self, letter):
        """takes an input, and cleans it, returns false if guess is not exclusively alphabetical"""
        self.guess = letter.lower().strip()
        if not self.guess.isalpha():
            return False
        return True

    def process_guess(self):
        """decides whether self.guess is correct or not"""
        if self.guess in self.chosen_word:
            self.replace_letter()  # replaces display_word with correctly guessed letters

            if self.display_word.replace(' ', '') == self.chosen_word:  # *** guessed all characters
                Donatello.draw_word(self.display_word)
                Donatello.correct_word(self.chosen_word.upper())
                return f"\n{self.display_word}\n\nWell done! The word was {self.chosen_word}.\n"
            else:
                Donatello.draw_word(self.display_word)
                return f"\nCorrect!\n\n{self.display_word}"

        else:
            self.attempts -= 1

            if self.attempts <= 0:
                Donatello.game_lost(self.chosen_word.upper())
                return f"\nWrong guess!\n\nYou ran out of attempts. The word was: {self.chosen_word}. \n"
            else:
                self.draw()
                Donatello.draw_word(self.display_word)
                return f"\nWrong guess! Please try again.\n\n{self.display_word}"


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

