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
        self.mode = None


    def initiate_game(self):
        Donatello.welcome_screen()


    def ask_username(self):
        self.username = turtle.textinput("WordGuesser", "Hi there! What's your name? ")
        return self.username

    def ask_mode(self):
        self.mode = turtle.textinput("WordGuesser",
                                "Which mode would you like to play? Campaign, or Levels? ").lower().strip()
        return self.mode

    def selected_mode_exists(self):
        return self.mode in ['campaign', 'levels']

    def ask_mode_again(self):
        if not self.selected_mode_exists():
            self.ask_mode()

    def play_again(self):
        return turtle.textinput("WordGuesser", "Do you want to play again? y/n: ").lower().strip() == "y"


    def loading_screen(self, message):
        Donatello.turtle_focused_text(message)
        Donatello.turtle_focused_text("Your word will be hidden below. Good luck.")  #, move=False, align="center", font=("Courier New", 30, "bold"))
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



class LevelsMode(PlayGame):
    def __init__(self):
        super().__init__()
        self.selected_level = None
        self.available_levels = {
            'Beginner': Beginner,
            'Medium': Medium,
            'Hard': Hard
        }
        self.is_custom_list = None

    def ask_level(self):
        self.selected_level = turtle.textinput("WordGuesser",
                                      f"Which level would you like to play, {self.username}? {'/'.join(self.available_levels.keys())}: ").capitalize().strip()

    def check_level(self):
        if self.selected_level in self.available_levels:
            self.level = self.available_levels[self.selected_level]
            return True
        else:
            Donatello.turtle_focused_text("Not a valid level! Try again.")
            return self.ask_level()
        
        
    def check_if_custom_list(self):
        return turtle.textinput("WordGuesser", "Do you want to use a custom words list? y/n: ").lower().strip() == "y"

        
    def set_words_list(self):
        if self.check_if_custom_list():
            self.list_type = 'custom'
            self.words_list = turtle.textinput("WordGuesser",
                                               "Please enter the words separated by a comma, e.g. car, plane, ... \n").lower().split(", ")
        else:
            self.list_type = 'default'
            self.words_list = list(word_task.only_words)
            
    def play_levels(self):
        self.loading_screen(f'You will be using a {self.list_type} list\nwith {self.selected_level} difficulty')
        self.run_game()


class CampaignMode(PlayGame):
    def __init__(self):
        super().__init__()
        self.level = 'Campaign'

    def play_campaign(self):
        self.loading_screen(f'You are playing {self.level} mode')
        for task_num in range(1, 11):
            task = word_task.get_word_of_task(task_num)  # task = (task given, word to guess)
            Donatello.turtle_text(task[0], (-220, 325))
            self.words_list = [task[1]]
            self.run_game()



if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    playthrough = PlayGame()
    is_first_play = True

    Donatello.welcome_screen()
    playthrough.ask_username()
    playthrough.ask_mode()
    username = turtle.textinput("WordGuesser", "Hi there! What's your name? ")
    mode = turtle.textinput("WordGuesser", "Which mode would you like to play? Campaign, or Levels? ").lower().strip()

    if mode == 'levels':
        pass
    elif mode == 'campaign':
        pass
    else:





    def start_game(self):
        if self.selected_level is None:
            raise Exception('Level is not defined')

        if self.selected_level == 'Campaign':
            self.play_campaign()
        else:
            self.play_levels()



    while is_first_play or playthrough.play_again():
        is_first_play = False
        playthrough.initiate_game()
        playthrough.start_game()

    Donatello.turtle_focused_text("Maybe next time!")
    Donatello.goodbye_screen()
    time.sleep(1.5)



