import nltk
from nltk import FreqDist
from nltk.corpus import brown, stopwords
from nltk.stem import WordNetLemmatizer

from collections import Counter

import random

# The Brown corpus (published in 1961) consists of 1M words from American English distributed across 15 genres.
br_words = brown.tagged_words(tagset='universal') # a list of tuples (word, tag): [('The', 'DET'), ('Fulton', 'NOUN'), ...]

# Lemmatize means to use the dictionary form of the word, e.g. cats - cat, knew - know.
lemmatizer = WordNetLemmatizer()

# Stop words are very common words that do not add much to the meaning (articles, pronouns, prepositions, auxiliary verbs).
# We don't want the users to guess such words in our game so we need to filter them from the Brown corpus.
stop_words = stopwords.words('english')

# Part-of-speech (POS) tags in the Brown corpus (tagset='universal')
tags = {"ADJ", "ADV", "NOUN", "VERB"}
# POS tags in WordNetLemmatizer are different.
wn_tags = {"ADJ" : "a", "ADV" : "r", "NOUN" : "n", "VERB" : "v"}

filtered_words = [(lemmatizer.lemmatize(word.lower(), pos = wn_tags[tag]), tag)  # a list of tuples: lemmatized lowercase word and its POS tag
                  for word, tag in br_words
                  if word.isalpha()  # exclude punctuation
                  and
                  word.lower() not in stop_words
                  and
                  tag in tags  # choose only adjectives, adverbs, nouns, and verbs from the Brown corpus
                  ]

# FreqDist (frequency distribution) is used to find the frequency of words within a text. It returns a dictionary of words and their count.
fd = FreqDist(filtered_words)

freq_words = fd.most_common(2000) # a list of 1000 word, tag tuples and their count sorted in the descending order.
# [(('say', 'VERB'), 2755), (('would', 'VERB'), 2714), (('make', 'VERB'), 2312)...]
final_wordlist = [tup for tup, count in freq_words] # a list of tuples: word, tag. Since it is already sorted, we do not need the count anymore.
#[('say', 'VERB'), ('would', 'VERB'), ('make', 'VERB')...]
#print(final_wordlist)


def is_unique_chars(word):
    """Returns True if all letters in the word are unique. Otherwise, returns False."""
    freq = Counter(word)
    if len(freq) == len(word):
        return True
    else:
        return False


def is_palindrome(word):
    """Returns True is the word is a palindrome."""
    return word == word[::-1]


#Examples of tasks (levels)

# Task 1
print("Try to guess the most common noun in American English.")
nouns = [word for word, tag in final_wordlist if tag == 'NOUN']
print(nouns[0])

# Task  2
print("Try to guess the most common adjective in American English.")
adj = [word for word, tag in final_wordlist if tag == 'ADJ']
print(adj[0])

# Task 3
print("Try to guess the most common adverb in American English.")
adv = [word for word, tag in final_wordlist if tag == 'ADV']
print(adv[0])

# Task 3
print("Let's make it more difficult. This time, the word might be a noun, adjective, adverb or verb.")
only_words = [word for word, tag in final_wordlist]
res = random.choice(only_words[:50]) # any from most frequent 50 words
print(res)

# Task 4
print("Can you guess a word where all the letters are different?")
unique = [w for w in only_words if is_unique_chars(w)]
res = random.choice(unique)
print(res)

# Task 5
print("Palindromes are words that read the same backward or forward. Can you guess one?")
palindromes = [w for w in only_words if is_palindrome(w) and len(w) > 1]
res = random.choice(palindromes)
print(res)

# Task 6
print("Try to guess a noun that consists of 10 characters.")
long_nouns = [w for w in nouns if len(w) == 10]
res = random.choice(long_nouns)
print(res)

# Task 7
print("How about an adjective this time? Think twice, it is not the most common one.")
long_adj = [w for w in adj if len(w) > 8]
res = random.choice(long_adj[-10:])
print(long_adj[-10:])

# For other tasks, we can play with the word length, part of speech, is_unique_chars function, how common the word is out of 2000 most common and so on,
# combining these features if we want to make it more difficult.

