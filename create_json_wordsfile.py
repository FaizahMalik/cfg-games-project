from nltk import FreqDist
from nltk.corpus import brown, stopwords
from nltk.stem import WordNetLemmatizer

import json

# The Brown corpus (published in 1961) consists of 1M words from American English distributed across 15 genres.
br_words = brown.tagged_words(tagset='universal')

# Lemmatize means to use the dictionary form of the word, e.g. cats - cat, knew - know.
lemmatizer = WordNetLemmatizer()

# Stop words are very common words that do not add much to the meaning (articles,
# pronouns, prepositions, auxiliary verbs). We don't want the users to guess such
# words in our game so we need to filter them from the Brown corpus.
stop_words = stopwords.words('english')

# Part-of-speech (POS) tags in the Brown corpus (tagset='universal')
tags = {"ADJ", "ADV", "NOUN", "VERB"}
# POS tags in WordNetLemmatizer are different.
wn_tags = {"ADJ": "a", "ADV": "r", "NOUN": "n", "VERB": "v"}

filtered_words = [(lemmatizer.lemmatize(word.lower(), pos=wn_tags[tag]), tag)
                  # a list of tuples: lemmatized lowercase word and its POS tag
                  for word, tag in br_words
                  if word.isalpha()  # exclude punctuation
                  and word.lower() not in stop_words
                  and tag in tags  # choose only adjectives, adverbs, nouns, and verbs from the Brown corpus
                  ]

# FreqDist (frequency distribution) is used to find the frequency of words within a text.
# It returns a dictionary of words and their count.
fd = FreqDist(filtered_words)

freq_words = fd.most_common(5000) # a list of 5000 word, tag tuples and their count sorted in the descending order.
# [(('would', 'VERB'), 2714), (('make', 'VERB'), 2312)...]

final_wordlist = [tup for tup, count in freq_words if len(tup[0]) > 3 ]
# a list of tuples: word, tag. Since it is already sorted, we do not need the count anymore.

with open("words_list.json", "w") as file:
  res = json.dumps(final_wordlist)
  file.write(res)
