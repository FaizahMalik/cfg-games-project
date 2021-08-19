import random
from levels import Beginner, Medium, Hard
import time
import turtle
from turtle_window import Donatello
from word_picker import word_task

class PlayGame:
    def __init__(self):
        self.username = None
        self.level = None
        self.selected_level = None
        self.words_list = None
        self.available_levels = {
            'Beginner': Beginner,
            'Medium': Medium,
            'Hard': Hard,
            'Campaign': 'Campaign'
        }

    def level_selection(self):
        selected_level = turtle.textinput("WordGuesser",
                                      f"Which level would you like to play, {self.username}? {'/'.join(self.available_levels.keys())}: ").capitalize().strip()

        self.selected_level = selected_level
        if selected_level == 'Campaign':
            self.level = Beginner
            return True
        elif selected_level in self.available_levels:
            self.level = self.available_levels[selected_level]
            return True
        else:
            Donatello.turtle_focused_text("Not a valid level! Try again.")
            return self.level_selection()

    def start_game(self):
        if self.selected_level is None:
            raise Exception('Level is not defined')

        if self.selected_level == 'Campaign':
            self.play_campaign()
        else:
            self.play_hangman()


    def initiate_game(self):
        Donatello.welcome_screen()
        self.username = turtle.textinput("WordGuesser", "Hi there! What's your name? ")
        self.level_selection()


    def play_again(self):
        if turtle.textinput("WordGuesser", "Do you want to play again? y/n: ").lower().strip() == "y":
            self.level_selection()
        else:
            Donatello.turtle_focused_text("Maybe next time!")
            Donatello.goodbye_screen()
            time.sleep(1.5)
            exit(0)


    def loading_screen(self, message):
        turtle.clear()
        turtle.pencolor(45, 83, 98)
        turtle.write(message, move=False, align="center", font=("Courier New", 30, "bold"))
        time.sleep(2)
        turtle.clear()
        turtle.write("Your word will be hidden below. Good luck.", move=False, align="center",
                     font=("Courier New", 30, "bold"))
        time.sleep(2)
        turtle.clear()
        for c in range(4):
            turtle.write("LOADING" + c * " .", move=False, align="center", font=("Courier New", 30, "bold"))
            time.sleep(random.uniform(0.3, 0.8))
            turtle.clear()


    def run_game(self):
        game1 = self.level(self.username, self.words_list)
        game1.pick_word()
        game1.show_word()
        while game1.display_word.replace(' ', '') != game1.chosen_word:
            guess = turtle.textinput("Turtle Game",
                                     f"Past Guesses: {game1.past_guesses}\n\nEnter your guess: ")
            game1.incorrect_guess(guess)
            if game1.attempts <= 0:
                break
        turtle.clear()


    def play_hangman(self):
        turtle.ht()
        self.words_list = list(word_task.only_words)
        if turtle.textinput("WordGuesser", "Do you want to use a custom words list? y/n: ") == "y":
            self.words_list = turtle.textinput("WordGuesser",
                                         "Please enter the words separated by a comma, e.g. car, plane, ... \n").lower().split(", ")
            list_type = 'custom'
        else:
            list_type = 'default'
        self.loading_screen(f'You will be using a {list_type} list')
        self.run_game()
        self.play_again()


    def play_campaign(self):
        self.loading_screen('You are playing campaign mode')
        for task_num in range(1, 11):
            task = word_task.get_word_of_task(task_num)
            turtle.ht()
            turtle.penup()
            turtle.goto(-220, 325)
            turtle.pencolor(45, 83, 98)
            turtle.write(task[0], move=False, align="center",
                         font=("Courier New", 20, "bold"))
            self.words_list = [task[task_num]]
            self.run_game()
        self.play_again()


if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   playthrough = PlayGame()
   playthrough.initiate_game()
   playthrough.start_game()


