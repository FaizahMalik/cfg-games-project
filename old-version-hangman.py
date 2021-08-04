
from functions import hide_word, random_word, play

name = input("What is your name? ")
print("Hey {}, let's play hangman! The computer will choose a word first".format(name))

words = ['python', 'software', 'list', 'dictionary', 'string', 'tuple', 'programming', 'function', 'class']

answer = random_word(words)
word_preview = hide_word(answer)

print(word_preview)

play(answer)
