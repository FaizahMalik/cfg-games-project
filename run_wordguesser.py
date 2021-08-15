# from classes import Beginner  #, Medium, Hard
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
#     game1 = Beginner(username, customList)
# else:
#     print(f"You will be using the default list. Your word is hidden below...\n")
#     game1 = Beginner(username, defaultList)
#
# print(game1.pick_word())
#
# while game1.display_word.replace(' ', '') != game1.chosen_word:
#     guess = input(f"\nAttempts left: {game1.attempts}\nPast Guesses: {game1.past_guesses}\n\nEnter your guess: ")
#     print(game1.check_guess(guess))
#     if game1.attempts <= 0:
#         break
#
# string = "\n" + " THANKS FOR PLAYING! ".center(44, "=") + "\n\n"
# for char in string:
#     print(char, end='')
#     time.sleep(.05)


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


import time
import turtle
from classes import Hard

turtle.ht()
screen = turtle.getscreen()
screen.setup(width=700, height=700)

defaultList = ['python']  #, 'software', 'list', 'dictionary', 'string', 'tuple', 'programming', 'function', 'class']

turtle.write("\n" + " WELCOME TO WORDGUESSER ".center(44, "=") + "\n\n", move=False, align="center", font=("Arial", 20, "normal"))
# for char in string:
#     turtle.write(char + '', move=False, align="left", font=("Arial", 8, "normal"))
#     time.sleep(.05)
time.sleep(2)

if turtle.textinput("Turtle Game", "Do you want to play wordguesser? y/n: ").lower().strip() == "y":
    username = turtle.textinput("Turtle Game", "Enter your name: ")
else:
    turtle.clear()
    turtle.write("Maybe next time... \n", move=False, align="center", font=("Arial", 15, "normal"))
    time.sleep(2)
    exit()

if turtle.textinput("Turtle Game", "Hi, {}. Would you like to use your own custom words? y/n: ".format(username)) == "y":
    customList = turtle.textinput("Turtle Game", "Please enter the words separated by a comma, e.g. car, plane, ... \n").lower().split(", ")
    game1 = Hard(username, customList)
else:
    turtle.clear()
    turtle.penup()
    turtle.goto(-100,0)
    turtle.write(f"You will be using the default list", move=False, align="center", font=("Arial", 15, "normal"))
    time.sleep(2)
    turtle.clear()
    turtle.write(f"Your word will be hidden below...\n Good luck!", move=False, align="center",font=("Arial", 15, "normal"))
    time.sleep(2.5)
    turtle.clear()
    game1 = Hard(username, defaultList)
print(game1.pick_word())


while game1.display_word.replace(' ', '') != game1.chosen_word:
    guess = turtle.textinput("Turtle Game", f"\nAttempts left: {game1.attempts}\nPast Guesses: {game1.past_guesses}\n\nEnter your guess: ")
    print(game1.check_guess(guess))
    if game1.attempts <= 0:
        break

screen.clear()

time.sleep(3)
turtle.write("\n" + " THANKS FOR PLAYING! ".center(44, "=") + "\n\n",move=False, align="center", font=("Arial", 15, "normal"))
time.sleep(3)
# for char in string:
#     print(char, end='')
#     time.sleep(.05)



