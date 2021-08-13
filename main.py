from classes import Beginner  #, Medium, Hard
import time

# TODO put in function to avoid repetition of code
# DONE rename main.py to main.py

defaultList = ['python']  #, 'software', 'list', 'dictionary', 'string', 'tuple', 'programming', 'function', 'class']

string = "\n" + " WELCOME TO WORDGUESSER ".center(44, "=") + "\n\n"
for char in string:
    print(char, end='')
    time.sleep(.05)

if input("Do you want to play wordguesser? y/n: ").lower().strip() == "y":
    username = input("Enter your name: ")
else:
    print("Maybe next time!")
    exit()

if input("Hi, {}. Would you like to use your own custom words? y/n: ".format(username)) == "y":
    customList = input("Please enter the words separated by a comma, e.g. car, plane, ... \n").lower().split(", ")
    game1 = Beginner(username, customList)
else:
    print(f"You will be using the default list. Your word is hidden below...\n")
    game1 = Beginner(username, defaultList)

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



