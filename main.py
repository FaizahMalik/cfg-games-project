import random

from levels import Beginner, Medium, Hard
import time
import turtle
from draw_turtle import Donatello
import json

# DONE rename main.py to main.py
# DONE put script into two functions - welcome_message() & play_hangman to avoid repeating code if player
# wants to play again
# DONE Added the option to play again
# TODO reset turtle so drawing starts over again

turtle.ht()
screen = turtle.getscreen()
screen.colormode(255)
screen.setup(width=700, height=700)
turtle.bgcolor(87, 217, 255)


# with open("words_list.json", "r") as json_file:
#     final_words_list = json.load(json_file)
#     defaultList = [word for word, tag in final_words_list]

defaultList = ['python']

def welcome_message():
    Donatello.welcome_screen()
    if turtle.textinput("Turtle Game", "Do you want to play wordguesser? y/n: ").lower().strip() == "y":
        turtle.clear()
        username = turtle.textinput("Turtle Game", "Enter your name: ")
        # game_mode = turtle.textinput("Which mode would you like to play? Beginner, Medium or Hard?)
        user_level = turtle.textinput("Turtle Game", "Which level would you like to play? Beginner/Medium/Hard: ").capitalize().strip()
        available_levels = {
            'Beginner': Beginner,
            'Medium': Medium,
            'Hard': Hard
        }
        if user_level in available_levels:
            level = available_levels[user_level]
            play_hangman(level, username)
            print(level)
            return username
        else:
            # turtle.textinput("Turtle Game", "Which level would you like to play? Beginner/Medium/Hard: ")
            print("Level does not exist.")
            return False
    else:
        turtle.clear()
        turtle.write("That's too bad. Maybe next time? ):", move=False, align="center", font=("Courier New", 20, "bold"))
        time.sleep(4)
        exit()


def play_hangman(level, username):
    if turtle.textinput("Turtle Game", "Hi, {}. Would you like to use your own custom words? y/n: ".format(username)) == "y":
        customList = turtle.textinput("Turtle Game", "Please enter the words separated by a comma, e.g. car, plane, ... \n").lower().split(", ")
        game1 = level(username, customList)
    else:
        turtle.clear()
        turtle.pencolor(38, 70, 83)
        turtle.write(f"You will be using the default list", move=False, align="center", font=("Courier New", 20, "bold"))
        time.sleep(2)
        turtle.clear()
        turtle.write("Your word will be hidden below. Good luck.", move=False, align="center", font=("Courier New", 20, "bold"))
        time.sleep(2)
        turtle.clear()
        for c in range(4):

            turtle.write("LOADING" + c * " .", move=False, align="center", font=("Courier New", 20, "bold"))
            time.sleep(random.uniform(0.3, 0.8))
            turtle.clear()
        game1 = level(username, defaultList)
# TODO TITLE SCREEN
    game1.pick_word()
    print(game1.show_word())

    while game1.display_word.replace(' ', '') != game1.chosen_word:
        # TODO if the word is python and I guess "py" i cry a tad
        guess = turtle.textinput("Turtle Game", f"\nAttempts left: {game1.attempts}\nPast Guesses: {game1.past_guesses}\n\nEnter your guess: ")
        game1.incorrect_guess(guess)
        if game1.attempts <= 0:
            break


    screen.clear()
    screen.colormode(255)
    turtle.bgcolor(87, 217, 255)
    time.sleep(3)
    turtle.write("\n" + " THANKS FOR PLAYING! ".center(44, "="),  move=False, align="center", font=("Courier New", 20, "bold"))
    time.sleep(3)

    # POTENTIAL CODE TO ALLOW USER TO PLAY AGAIN??####
    if turtle.textinput("Turtle Game", "Do you want to play again? y/n: ").lower().strip() == "y":
        user_level = turtle.textinput("Turtle Game", "Which level would you like to play? Beginner/Medium/Hard: ").capitalize().strip()
        available_levels = {
            'Beginner': Beginner,
            'Medium': Medium,
            'Hard': Hard
        }

        if user_level in available_levels:
            level = available_levels[user_level]
        else:
            print("Level does not exist.")
        play_hangman(level, username)
    else:
        print("Maybe next time!")
        exit()


# turtle.ht()
# screen = turtle.getscreen()
# screen.setup(width=700, height=700)
#
#
# def welcome_message():
#     turtle.write("\n" + " WELCOME TO WORDGUESSER ".center(44, "=") + "\n\n", move=False, align="center",
#                  font=("Arial", 20, "normal"))
#     time.sleep(2)
#
#     if turtle.textinput("Turtle Game", "Do you want to play wordguesser? y/n: ").lower().strip() == "y":
#         username = turtle.textinput("Turtle Game", "Enter your name: ")
#         play_hangman(Beginner, username)
#         return username
#     else:
#         turtle.clear()
#         turtle.write("Maybe next time... \n", move=False, align="center", font=("Arial", 15, "normal"))
#         time.sleep(2)
#         exit()
#
#
# def play_hangman(level, username):
#
#     defaultList = ['python']  #, 'software', 'list', 'dictionary', 'string', 'tuple', 'programming', 'function', 'class']
#
#     if turtle.textinput("Turtle Game", "Hi, {}. Would you like to use your own custom words? y/n: ".format(username)) == "y":
#         customList = turtle.textinput("Turtle Game", "Please enter the words separated by a comma, e.g. car, plane, ... \n").lower().split(", ")
#         game1 = level(username, customList)
#     else:
#         turtle.clear()
#         turtle.penup()
#         turtle.goto(-25, 0)
#         turtle.write(f"You will be using the default list", move=False, align="center", font=("Arial", 15, "normal"))
#         time.sleep(2)
#         turtle.clear()
#         turtle.write(f"Your word will be hidden below.\nGood luck!", move=False, align="right", font=("Arial", 20, "normal"))
#         # for i in range(15):
#         #     turtle.write("\r" + ('=' * (i + 1)) + " THANKS FOR PLAYING! " + ('=' * (i + 1)), move=False, align="center", font=("Arial", 15, "normal"))
#         #     time.sleep(0.12)
#         time.sleep(2.5)
#         turtle.clear()
#         game1 = level(username, defaultList)
#
#     game1.pick_word()
#     print(game1.show_word())
#
#     while game1.display_word.replace(' ', '') != game1.chosen_word:
#         guess = turtle.textinput("Turtle Game", f"\nAttempts left: {game1.attempts}\nPast Guesses: {game1.past_guesses}\n\nEnter your guess: ")
#         game1.incorrect_guess(guess)
#         if game1.attempts <= 0:
#             break
#
#     screen.clear()
#     time.sleep(3)
#     turtle.write("\n" + " THANKS FOR PLAYING! ".center(44, "=") + "\n\n", move=False, align="center", font=("Arial", 15, "normal"))
#     time.sleep(3)



welcome_message()


### ALTERNATIVE MESSAGES:
#
# for i in range(15):
#     print("\r" + ('=' * (i + 1)), end='' + " THANKS FOR PLAYING! " + ('=' * (i + 1)))
#     time.sleep(0.12)
#
# print("\n" + " THANKS FOR PLAYING! ".center(44, "="))
#
# for i in range(15):
#     print("\r" + ('=' * (i + 1)), end='' + " WELCOME TO WORDGUESSER " + ('=' * (i + 1)))
#     time.sleep(0.09)
# print("\n\n")
#
# print("\n" + " WELCOME TO WORDGUESSER ".center(44, "=") + "\n")




