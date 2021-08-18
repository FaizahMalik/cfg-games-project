import random
from levels import Beginner, Medium, Hard
import time
import turtle
from turtle_window import Donatello
import json
from word_picker import word_task


# global level

with open("words_list.json", "r") as json_file:
    final_words_list = json.load(json_file)
    defaultList = [word for word, tag in final_words_list]

# defaultList = ['python']

def level_selection(username):
    # global username
    user_level = turtle.textinput("WordGuesser",
                                  f"Which level would you like to play, {username}? Beginner/Medium/Hard/Campaign: ").capitalize().strip()
    available_levels = {
        'Beginner': Beginner,
        'Medium': Medium,
        'Hard': Hard,
        'Campaign': 'Campaign'
    }
    if user_level == 'Beginner' or user_level == 'Medium' or user_level == 'Hard':
        level = available_levels[user_level]
        play_hangman(level, username)
    elif user_level == 'Campaign':
        play_campaign(username)
    else:
        Donatello.turtle_focused_text("Not a valid level! Try again.")
        return level_selection(username)

def initiate_game():
    Donatello.welcome_screen()
    # turtle.ht()
    username = turtle.textinput("WordGuesser", "Hi there! What's your name? ")
    level_selection(username)

def play_again(username):
    if turtle.textinput("WordGuesser", "Do you want to play again? y/n: ").lower().strip() == "y":
        level_selection(username)
    else:
        Donatello.turtle_focused_text("Maybe next time!")
        time.sleep(2)
        exit(0)

def play_hangman(level, username):
    turtle.reset()
    turtle.ht()
    wordList = defaultList
    if turtle.textinput("WordGuesser", "Do you want to use a custom words list? y/n: ") == "y":
        wordList = turtle.textinput("WordGuesser", "Please enter the words separated by a comma, e.g. car, plane, ... \n").lower().split(", ")
        list_type = 'custom'
    else:
        list_type = 'default'
    turtle.clear()
    turtle.pencolor(45, 83, 98)
    turtle.write(f"You will be using a {list_type} list", move=False, align="center", font=("Courier New", 30, "bold"))
    time.sleep(2)
    turtle.clear()
    turtle.write("Your word will be hidden below. Good luck.", move=False, align="center", font=("Courier New", 30, "bold"))
    time.sleep(2)
    turtle.clear()
    for c in range(4):
        turtle.write("LOADING" + c * " .", move=False, align="center", font=("Courier New", 30, "bold"))
        time.sleep(random.uniform(0.3, 0.8))
        turtle.clear()
    game1 = level(username, wordList)
    game1.pick_word()
    game1.show_word()
    while game1.display_word.replace(' ', '') != game1.chosen_word:
        guess = turtle.textinput("WordGuesser", f"Past Guesses: {game1.past_guesses}\n\nEnter your guess: ")
        game1.incorrect_guess(guess)
        if game1.attempts <= 0:
            break


def play_campaign(username):
    for task_num in range(1, 3):
        task = word_task.get_word_of_task(task_num)
        turtle.ht()
        turtle.penup()
        turtle.goto(-350, 350)
        turtle.pencolor(45, 83, 98)
        turtle.write(task[0], move=False, align="center",font=("Courier New", 30, "bold"))
        game1 = Beginner(username, [task[1]])
        game1.pick_word()
        print(game1.show_word())
        while game1.display_word.replace(' ', '') != game1.chosen_word:
            guess = turtle.textinput("Turtle Game",
                                     f"\nAttempts left: {game1.attempts}\nPast Guesses: {game1.past_guesses}\n\nEnter your guess: ")
            game1.incorrect_guess(guess)
            if game1.attempts <= 0:
                break
        turtle.clear()

        #     if game1.status == 'Lost':
        #         break
        # if game1.status == 'Lost':  # thanks for playing
        #     break


    # #CODE FOR CAMPAIGN MODE
    # while game1.display_word.replace(' ', '') != game1.chosen_word:
    #     guess = turtle.textinput("WordGuesser", f"Past Guesses: {game1.past_guesses}\n\nEnter your guess: ")
    #     game1.incorrect_guess(guess)

    play_again(username)

initiate_game()

