from classes import Beginner, Medium, Hard

defaultList = ['software', 'list', 'dictionary', 'string', 'tuple', 'programming', 'function', 'class']

if input("Do you wanna play word guesser? y/n: ") == "y":
    username = input("Enter your name: ")
else:
    print("Maybe next time!")
    exit()

if input("Hi, {}. Would you like to use your own custom words? y/n: ".format(username)) == "y":
    customList = input("Please enter the words separated by a comma, e.g. car, plane, ... \n").lower().split(", ")
    game1 = Beginner(username, customList)
else:
    print("You will be using the default list.\nThis is your word:\n")
    game1 = Beginner(username, defaultList)

print(game1.pick_word())

while game1.display_word.replace(' ', '') != game1.chosen_word:
    guess = input("\nEnter your guess: ")
    print(game1.guess_letter(guess))
    if game1.attempts <= 0:
        break

print()
print(" Thanks for playing! ".center(44, "="))
print(f"Your word was {game1.chosen_word}, thanks for playing!")
