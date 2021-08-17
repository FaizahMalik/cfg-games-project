import random
from word_picker import word_task
from turtle_window import Donatello


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
        try:
            for draw_method in self.turtle_drawings[self.attempts]:
                method = getattr(Donatello, draw_method)
                method()
        except KeyError:
            print(KeyError, "missing key in self.turtle_drawings")


    def pick_word(self):
        """chooses a random word from given list"""
        self.chosen_word = random.choice(self.words_list)
        return self.chosen_word

    def show_word(self):
        """Returns hidden version of the word"""
        self.display_word = len(self.chosen_word) * "_ "
        Donatello.draw_word(self.display_word)
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
            Donatello.turtle_text("No special characters or numbers")  # no numbers, special characters or multiple words allowed
            return False
        # TODO if type != str raise assert
        return self.guess

    def check_guess_if_previous(self):  # is a helper function to add_previous_guess()
        """checks whether the letter has already been guessed"""
        if self.guess in self.past_guesses:
            return False
        else:
            return True

    def add_previous_guess(self):
        # relies on the results from check_guess_if_previous() | helper function to incorrect_guess()
        """If check_guess_if_previous() returns True, the letter is added to the list of self.past_guesses"""
        if self.check_guess_if_previous():
            self.past_guesses.append(self.guess)  # adds guessed letter to past guesses
            return self.past_guesses
        else:
            Donatello.turtle_text(f"You've already guessed '{self.guess}'!")
            return False

    def correct_guess(self):  # relies on the results from replace_letter() | helper function to display_correct_guess()
        """checks if guess exists in self.chosen_word, if so it calls the replaces_letter() function to replace
        letter """
        if len(self.guess) == 1:
            if self.guess in self.chosen_word:
                self.replace_letter()  # replaces display_word with correctly guessed letters
                return True
        return False

    def correct_word(self):  # is a helper function to display_correct_guess()
        """checks if the the guess is equal to the chosen word, if yes it returns True and the full word"""
        if self.guess == self.chosen_word:  # they guess the whole word correctly
            self.display_word = self.chosen_word  # process will continue until it reaches ***
            return True, self.display_word
        else:
            return False

    def guessed_word(self):
        """checks if the total of the guesses is equal to the chosen word, if yes it returns True and the full word"""
        if self.correct_guess():
            if self.display_word.replace(' ','') == self.chosen_word:
                self.display_word = self.chosen_word  # process will continue until it reaches ***
                return True, self.display_word
        else:
            return False

    def display_correct_guess(
            self):  # relies on the results from correct_word() and correct_guess() | helper function to incorrect_guess()
        """Displays the word or a letter if the guess was correct."""
        if self.correct_word():  # *** guessed all characters
            Donatello.draw_word(self.display_word)
            Donatello.turtle_focused_text(f"Well done, the word was '{self.chosen_word.upper()}'")
            Donatello.turtle_focused_text(" YOU WIN! ".center(40, "*"))
            return True, self.display_word
        elif self.guessed_word():
            Donatello.draw_word(self.display_word)
            Donatello.turtle_focused_text(f"Well done, the word was '{self.chosen_word.upper()}'")
            Donatello.turtle_focused_text(" YOU WIN! ".center(40, "*"))
            return True, self.display_word
        elif self.correct_guess():
            Donatello.turtle_text(f"Correct guess! Attempts left: {self.attempts}")
            Donatello.draw_word(self.display_word)
            return True, self.display_word
        else:
            return False

    def incorrect_guess(self, letter):  # relies on sanitise_guess, add_previous_guess(), display_correct_guess() & draw()
        """checks if guess is incorrect. If so self.attempts are added and incorrect messages are displayed."""
        if not self.sanitize_guess(letter):  # ensures that it is alphabetical input
            return False
        if not self.add_previous_guess():  # ensures that it hasn't already been guessed
            return False
        if not self.display_correct_guess():  # ensures that it is not a correct guess
            self.attempts -= 1

            if self.attempts <= 0:
                Donatello.turtle_text(f"Wrong guess! Attempts left: {self.attempts}")
                Donatello.turtle_focused_text(f"Oh no! You ran out of attempts. The word was '{self.chosen_word.upper()}'")
                return False
            else:
                Donatello.turtle_text(f"Wrong guess! Attempts left: {self.attempts}")
                self.draw()
                Donatello.draw_word(self.display_word)
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

class Campaign(Level):
    def __init__(self, username):
        super(Campaign, self).__init__(username, words_list=[0])
        self.attempts = 8
        self.task_number = 11
        self.turtle_drawings = {
            7: ["draw_body", "draw_head"],
            6: ["draw_leg1", "draw_leg2"],
            5: ["draw_leg3", "draw_leg4"],
            4: ["draw_tail"],
            3: ["draw_back_middle"],
            2: ["draw_back_line"],
            1: ["draw_eyes"]
        }

    def task_picker(self):
        return word_task.get_word_of_task(self.task_number)

    def next_task(self):
        # try:
        assert 1 <= self.task_number <= 10
        # except AssertionError:
        #     print("That task does not exist!")
        # else:
        #     self.task_number += 1




            # Donatello
            # turtle.write(task[0], move=False, align="center",
            #              font=("Courier New", 20, "bold"))
            # game1 = level(username, [task[1]])
            #
            # game1.pick_word()
            # print(game1.show_word())
            #
            # while game1.display_word.replace(' ', '') != game1.chosen_word:
            #     guess = turtle.textinput("Turtle Game",
            #                              f"\nAttempts left: {game1.attempts}\nPast Guesses: {game1.past_guesses}\n\nEnter your guess: ")
            #     game1.incorrect_guess(guess)
            #     if game1.status == 'Lost':
            #         break

username = 'person'
game2 = Campaign(username)


print(game2.task_picker())
print(game2.next_task())
print(game2.next_task())
print(game2.task_picker())
print(game2.next_task())
print(game2.task_picker())
print(game2.next_task())
print(game2.task_picker())
print(game2.next_task())


