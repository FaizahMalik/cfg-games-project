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

    @staticmethod  # These methods are static so that they can be accessed without requiring an instance of the class.
    def ask_name():
        """Asks the user for their name, and returns it"""
        name = turtle.textinput("WordGuesser", "Hi there! What's your name? ")
        return name

    @staticmethod
    def ask_mode():
        """Asks the user which mode they want to play, returns the mode if it exists.
        If they enter an invalid mode, it will alert the user and ask again (recursively)"""
        game_mode = turtle.textinput("WordGuesser",
                                     f"Which mode would you like to play, {username}? Campaign, or Levels? ").lower().strip()
        if game_mode in ['campaign', 'levels']:
            return game_mode
        else:
            Donatello.turtle_focused_text("Invalid mode! Try again")
            return PlayGame.ask_mode()

    def play_again(self):
        """Asks the user if they want to play again,
        returns true if response is y and returns false otherwise after showing the goodbye screen"""
        if turtle.textinput("WordGuesser", "Do you want to play again? y/n: ").lower().strip() == "y":
            return True
        else:
            Donatello.goodbye_screen()
            return False

    def loading_screen(self, message):
        """Shows the loading screen when called with a specified message"""
        Donatello.turtle_focused_text(message)
        Donatello.turtle_focused_text("Your word will be hidden below. Good luck.")
        turtle.pencolor(45, 83, 98)
        for c in range(4):
            turtle.write("LOADING" + c * " .", move=False, align="center", font=("Courier New", 30, "bold"))
            time.sleep(random.uniform(0.3, 0.8))
            turtle.clear()
        return True

    def run_game(self):
        """Runs the actual game"""
        game1 = self.level(self.username, self.words_list)
        game1.pick_word()
        game1.show_word()
        while game1.display_word.replace(' ', '') != game1.chosen_word:
            guess = turtle.textinput("Turtle Game",
                                     f"Past Guesses: {game1.past_guesses}\n\nEnter your guess: ")
            game1.incorrect_guess(guess)
            if game1.attempts <= 0:
                break
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
        """Runs the level and list selection process.
        The user will be prompted to enter a valid level until one has been provided"""
        self.ask_level()
        while not self.check_level():
            self.ask_level()
        self.set_words_list()
        return True

    def ask_level(self):
        """Asks the user to type which level they want to select and saves it to an attribute"""
        self.selected_level = turtle.textinput("WordGuesser",
                                               f"And which level would you like to play? {'/'.join(self.available_levels.keys())}: ").capitalize().strip()
        return True

    def check_level(self):
        """Checks if the level selected is an available level"""
        if self.selected_level in self.available_levels:
            self.level = self.available_levels[self.selected_level]
            return True
        else:
            Donatello.turtle_focused_text("Not a valid level! Try again.")
            return False

    def ask_if_custom_list(self):
        """Asks the user if they want to use a custom list, checks if the answer == 'y' and returns true or false"""
        self.is_custom_list = turtle.textinput("WordGuesser",
                                               "Do you want to use a custom words list? y/n: ").lower().strip()
        return self.is_custom_list == "y"  # This statement evaluates to True or False, so no need for an if statement.


    def set_words_list(self):
        """Checks if ask_if_custom_list() is True or False and sets the list type and list words accordingly"""
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
        """The loading screen will appear with the specified message and then it runs the game"""
        self.loading_screen(f'You will be using a {self.list_type} list\nwith {self.selected_level} difficulty')
        self.run_game()
        return True


class CampaignMode(PlayGame):  # This is our campaign mode where the user will cycle through a set of tasks
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.level = Beginner  # Beginner difficulty by default.
        self.task_range = (10)

    def display_task(self, string):
        """Displays the given message at the top of the screen"""
        # turtle.pencolor(45, 83, 98)
        turtle.pencolor(45, 83, 98)
        turtle.penup()
        turtle.clear()
        turtle.goto(-150, 280)
        turtle.write(string, move=False, align="center", font=("Courier New", 20, "bold"))
        time.sleep(0.5)
        return True

    def play_campaign(self):
        """Shows the loading screen with a message. Then calls task_cycle()"""
        self.loading_screen(f'You are playing campaign mode')
        self.task_cycle()
        return True

    def task_cycle(self):
        """Cycles through the tasks and runs the game after setting the words_list to the task word,
        and displaying the task message on the Turtle window"""
        for task_num in range(self.task_range):
            task = word_task.get_word_of_task(task_num)  # task = (task given, word to guess)
            self.display_task(f'{task_num+1}. {task[0]}')  # task[0] is where the task instructions are stored
            self.words_list = [task[1]]  # task[1] is where the task answer word is stored
            self.run_game()


def run():
    is_first_play = True
    turtle.ht()  # Hides turtle cursor
    username = ''

    while is_first_play or playthrough.play_again():
        if is_first_play:
            is_first_play = False
            Donatello.welcome_screen()
            username = PlayGame.ask_name()
        mode = PlayGame.ask_mode()
        if mode == 'campaign':
            playthrough = CampaignMode(username)
            playthrough.play_campaign()
        elif mode == 'levels':
            playthrough = LevelsMode(username)
            playthrough.initiate_levels()
            playthrough.play_levels()

if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    run()


# THIS NEEDS TO BE COMMENTED OUT WHEN RUNNING MAIN
#     PlayGame()
#     LevelsMode()
#     CampaignMode()
#     ask_name()
#     ask_mode()
