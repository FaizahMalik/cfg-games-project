import random

# if it's a user, there can be a subclass, and if guest, then just use main base class, or use separate guest child class

# option to manually add random words
# userWords = input("please enter your list of words seperated by commas. e.g. car, plant, ... \n")
# userWordsList = userWords.split(",")
# print(userWordsList)

# random word list
wordsList = ['hello', 'how', 'are', 'you', 'doing']


class WordGuesser:
    def __init__(self, username, words_list):
        self.words_list = words_list
        self.username = username  # not implemented
        self.chosen_word = None
        self.hidden_word = None
        self.attempts = 9
        self.past_guesses = None  # not implemented
        self.guess = None
        # self.difficulty = 0
        # self.password = 0

    def custom_list(self):
        # could add function to allow user to input their own list as a string
        pass

    def pick_word(self):
        self.chosen_word = random.choice(self.words_list)
        self.hidden_word = len(self.chosen_word) * "_ "
        return self.chosen_word

    # def hide_word(self):  # hide word return show to user
    #     self.hidden_word = len(self.chosen_word) * "_ "
    #     return self.hidden_word

    # def input_letter(self, letter):
    #     letter = letter.strip()
    #     self.guess = letter.lower()
    #     if self.guess.isalpha():  # Could allow numbers too for a higher difficulty level
    #         self.attempts += 1  # could move attempt count plus to guess_letter
    #         return self.guess
    #     else:
    #         return False  # if it's false, then tell the user INVALID, TRY AGAIN


    def guess_letter(self, letter):
        self.guess = letter.lower().strip()

        if not self.guess.isalpha():  # Could allow numbers too for a higher difficulty level
            return "No special characters"  # no numbers or special characters allowed

        if self.attempts <= 0:
            return "Run out of guesses"  # run out of guesses

        self.attempts -= 1

        if self.guess in self.chosen_word:
            occurrences = [j for j, x in enumerate(self.chosen_word) if x == self.guess]
            for i in range(0, len(occurrences)):
                # self.split_word.index(self.guess)
                split_hidden_word = list(self.hidden_word)
                split_hidden_word[occurrences[i]] = self.guess
            return "Correct!!"


            # find index where that letter is, check first how many times that letter appears
            # replace hidden word with the correctly guessed letter(s)
        else:
            return "Wrong guess"  # wrong guess, tell user try again OR end game if max attempts reached



game1 = WordGuesser('player1', wordsList)

game1.guess_letter()




        # while self.attempts < 10:
        #
        #     self.attempts += 1







# take user letter guesses - make sure to convert them to lowercase.
#       Special characters not allowed. Display error message and let them try again

# check if user inputs are correct

# if correct, make word appear in the hidden word in the correct position

# if wrong, subract 1 from number of tries


def wrong_guess():
    pass


def correct_guess():
    pass


# when number of tries reaches 0, reveal word


