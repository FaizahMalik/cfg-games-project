from levels import Beginner, Medium, Hard
import time


# DONE rename main.py to main.py
# DONE put script into two functions - welcome_message() & play_hangman to avoid repeating code if player
# wants to play again
# DONE Added the option to play again
# TODO reset turtle so drawing starts over again


def welcome_message():
    string = "\n" + " WELCOME TO WORDGUESSER ".center(44, "=") + "\n\n"
    for char in string:
        print(char, end='')
        time.sleep(.05)

    if input("Do you want to play wordguesser? y/n: ").lower().strip() == "y":
        username = input("Enter your name: ")
        play_hangman(Beginner, username)
        return username
    else:
        print("Maybe next time!")
        exit()


def play_hangman(level, username):

    defaultList = ['python']  #, 'software', 'list', 'dictionary', 'string', 'tuple', 'programming', 'function', 'class']

    if input("Hi, {}. Would you like to use your own custom words? y/n: ".format(username)) == "y":
        customList = input("Please enter the words separated by a comma, e.g. car, plane, ... \n").lower().split(", ")
        game1 = level(username, customList)
    else:
        print(f"You will be using the default list. Your word is hidden below...\n")
        game1 = level(username, defaultList)

    game1.pick_word()
    print(game1.show_word())

    while game1.display_word.replace(' ', '') != game1.chosen_word:
        guess = input(f"\nAttempts left: {game1.attempts}\nPast Guesses: {game1.past_guesses}\n\nEnter your guess: ")
        game1.incorrect_guess(guess)
        if game1.attempts <= 0:
            break

    string = "\n" + " THANKS FOR PLAYING! ".center(44, "=") + "\n\n"
    for char in string:
        print(char, end='')
        time.sleep(.05)

    ## POTENTIAL CODE TO ALLOW USER TO PLAY AGAIN??####
    # if input("Do you want to play again? y/n: ").lower().strip() == "y":
    #     user_level = input("Which level would you like to play? Beginner/Medium/Hard/Wildcard: ").capitalize().strip()
    #     available_levels = {
    #         'Beginner': Beginner,
    #         'Medium': Medium,
    #         'Hard': Hard
    #         # 'Wildcard': Wildcard
    #     }
    #
    #     if user_level in available_levels:
    #         level = available_levels[user_level]
    #     else:
    #         print("Level does not exist.")
    #     play_hangman(level, username)
    # else:
    #     print("Maybe next time!")
    #     exit()

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


# from classes import Beginner, Medium, Hard
# import time
#
# defaultList = ['python']  #, 'software', 'list', 'dictionary', 'string', 'tuple', 'programming', 'function', 'class']
#
# string = "\n" + " WELCOME TO WORDGUESSER ".center(44, "=") + "\n\n"
# for char in string:
#     print(char, end='')
#     time.sleep(.05)
#
# if input("Do you want to play wordguesser? y/n: ").lower().strip() == "y":
#     username = input("Enter your name: ")
# else:
#     print("Maybe next time!")
#     exit()
#
# if input("Hi, {}. Would you like to use your own custom words? y/n: ".format(username)) == "y":
#     customList = input("Please enter the words separated by a comma, e.g. car, plane, ... \n").lower().split(", ")
#     game1 = Hard(username, customList)
# else:
#     print(f"You will be using the default list. Your word is hidden below...\n")
#     game1 = Hard(username, defaultList)
#
# game1.pick_word()
# print(game1.show_word())
#
# while game1.display_word.replace(' ', '') != game1.chosen_word:
#     guess = input(f"\nAttempts left: {game1.attempts}\nPast Guesses: {game1.past_guesses}\n\nEnter your guess: ")
#     game1.incorrect_guess(guess)
#     if game1.attempts <= 0:
#         break
#
# string = "\n" + " THANKS FOR PLAYING! ".center(44, "=") + "\n\n"
# for char in string:
#     print(char, end='')
#     time.sleep(.05)



