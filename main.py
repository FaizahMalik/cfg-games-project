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
        self.words_list = None

    def play_again(self):
        if turtle.textinput("WordGuesser", "Do you want to play again? y/n: ").lower().strip() == "y":
            return True
        else:
            return False

    def loading_screen(self, message):
        Donatello.turtle_focused_text(message)
        Donatello.turtle_focused_text(
            "Your word will be hidden below. Good luck.")  # , move=False, align="center", font=("Courier New", 30, "bold"))
        turtle.pencolor(45, 83, 98)
        for c in range(4):
            turtle.write("LOADING" + c * " .", move=False, align="center", font=("Courier New", 30, "bold"))
            time.sleep(random.uniform(0.3, 0.8))
            turtle.clear()
        return True

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
        return True


class LevelsMode(PlayGame):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.selected_level = None
        self.available_levels = {
            'Beginner': Beginner,
            'Medium': Medium,
            'Hard': Hard
        }
        self.is_custom_list = None
        self.list_type = None

    def initiate_levels(self):
        self.ask_level()
        self.check_level()
        self.set_words_list()
        return True

    def ask_level(self):
        self.selected_level = turtle.textinput("WordGuesser",
                                               f"And which level would you like to play? {'/'.join(self.available_levels.keys())}: ").capitalize().strip()
        return True

    def check_level(self):
        if self.selected_level in self.available_levels:
            self.level = self.available_levels[self.selected_level]
            return True
        else:
            Donatello.turtle_focused_text("Not a valid level! Try again.")
            return self.ask_level()

    def ask_if_custom_list(self):
        self.is_custom_list = turtle.textinput("WordGuesser",
                                               "Do you want to use a custom words list? y/n: ").lower().strip()
        if self.is_custom_list == "y":
            return True
        else:
            return False

    def set_words_list(self):
        if self.ask_if_custom_list():
            self.list_type = 'custom'
            self.words_list = turtle.textinput("WordGuesser",
                                               "Please enter the words separated by a comma, e.g. car, plane, ... \n").lower().split(
                ", ")
            return False
        else:
            self.list_type = 'default'
            self.words_list = list(word_task.only_words)
            return True

    def play_levels(self):
        self.loading_screen(f'You will be using a {self.list_type} list\nwith {self.selected_level} difficulty')
        self.run_game()
        return True


class CampaignMode(PlayGame):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.level = Beginner

    def play_campaign(self):
        self.loading_screen(f'You are playing campaign mode')
        for task_num in range(1, 11):
            task = word_task.get_word_of_task(task_num)  # task = (task given, word to guess)
            Donatello.turtle_text(task[0], (-220, 325))
            self.words_list = [task[1]]
            self.run_game()


def ask_name():
    name = turtle.textinput("WordGuesser", "Hi there! What's your name? ")
    return name


def ask_mode():
    game_mode = turtle.textinput("WordGuesser",
                                 f"Which mode would you like to play, {name}? Campaign, or Levels? ").lower().strip()
    if game_mode in ['campaign', 'levels']:
        return game_mode
    return ask_mode()


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
# THIS NEEDS TO BE COMMENTED OUT WHEN RUNNING MAIN
#     PlayGame()
#     LevelsMode()
#     CampaignMode()
#     ask_name()
#     ask_mode()

# THIS NEEDS TO BE COMMENTED OUT WHEN TESTING
    is_first_play = True
    keep_playing = False
    turtle.ht()

while is_first_play or playthrough.play_again():
    if is_first_play:
        is_first_play = False
        Donatello.welcome_screen()
        name = ask_name()
    mode = ask_mode()
    if mode == 'campaign':
        playthrough = CampaignMode(name)
        playthrough.play_campaign()
    elif mode == 'levels':
        playthrough = LevelsMode(name)
        playthrough.initiate_levels()
        playthrough.play_levels()
