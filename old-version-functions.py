import random


def random_word(list):
    word = random.choice(list)
    return word


def hide_word(string):
    hidden = '_ ' * len(string)
    return hidden


def display_word(string, list):
    display = ''
    for i in string:
        if i in list:
            display += i
            display += ' '
        else:
            display += '_ '
    return display


def play(word):
    tries = 6
    guessed_letters = []
    while tries > 0:
        guess = str(input("You have {} tries left. Guess a letter: ".format(tries)).lower())
        if guess in word:
            guessed_letters += guess
            print("Correct!")
            word_display = display_word(word, guessed_letters)
            print(word_display)
            if word_display.replace(' ', '') == word:
                print("Well done, you have guessed the word!")
                break
        else:
            print("Wrong!")
            tries -= 1
    else:
        print("Game Over! You have run out of guesses, the correct word was '{}'.".format(word))


