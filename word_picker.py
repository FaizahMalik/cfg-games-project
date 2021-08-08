from collections import Counter
import random
import json

class WordPicker:

    def __init__(self):
        """Reads from the words_list.json file (5000 most common words from the Brown corpus)
         and creates a list of lists [word, POS tag] and a list of only words."""
        with open("words_list.json", "r") as json_file:
            final_words_list = json.load(json_file)
        self.all_words = final_words_list
        self.only_words = [word for word, tag in self.all_words]

    def get_freq_pos(self, pos):
        """Creates a list of frequent words belonging to a chosen part of speech: either nouns, adjectives, adverbs or verbs."""
        return [word for word, tag in self.all_words if tag == pos]

    def is_unique_chars(self, word):
        """Returns True if all letters in the word are unique. Otherwise, returns False."""
        freq = Counter(word)
        if len(freq) == len(word):
            return True
        else:
            return False

    def is_palindrome(self, word):
        """Returns True is the word is a palindrome. Otherwise, returns False."""
        return word == word[::-1]

    def get_word_of_task(self, task_num):
        """Accepts the number of the task as an integer (from 1 to 10) and returns a tuple:
        (message_for_the_user, word_to_guess)"""
        if task_num == 1:
            message = "Let's start the game! Try to guess the most common noun in American English."
            word_to_guess = self.get_freq_pos("NOUN")[0]

        elif task_num == 2:
            message = "Try to guess a common adjective in American English."
            common_adj = [w for w in self.get_freq_pos("ADJ")[:100] if 10 > len(w) > 6]
            word_to_guess = random.choice(common_adj)

        elif task_num == 3:
            message = "Let's make it more difficult. This time, the word might be a noun, adverb or verb."
            any_word = [w for w, tag in self.all_words[:300] if 10 > len(w) > 7 and tag != "ADJ" and not self.is_unique_chars(w)]
            word_to_guess = random.choice(any_word)

        elif task_num == 4:
            message = "Palindromes are words that read the same backward or forward. Can you guess one?"
            palindromes = [w for w in set(self.only_words) if self.is_palindrome(w) and 10 > len(w) > 1]
            word_to_guess = random.choice(palindromes)

        elif task_num == 5:
            message = "Can you guess a word where all the letters are different?"
            unique = [w for w in self.only_words if self.is_unique_chars(w) and len(w) == 7]
            word_to_guess = random.choice(unique)

        elif task_num == 6:
            message = "Try to guess a noun that consists of 9 unique characters."
            unique_nouns = [w for w in self.get_freq_pos("NOUN") if len(w) == 9 and self.is_unique_chars(w)]
            word_to_guess = random.choice(unique_nouns)

        elif task_num == 7:
            message = "How about an adjective? Think twice, it is not the most common one."
            long_adj = [w for w in self.get_freq_pos("ADJ")[-110:] if len(w) == 9]
            word_to_guess = random.choice(long_adj)

        elif task_num == 8:
            message = "A less frequent noun, verb or adverb. What will you get this time?"
            rare_words = [w for w, tag in self.all_words if 10 > len(w) > 7 and tag != "ADJ"]
            word_to_guess = random.choice(rare_words[-50:])

        elif task_num == 9:
            message = "How well do you know adverbs? Can you guess a long one?"
            long_adv = [w for w in self.get_freq_pos("ADV") if len(w) == 10]
            word_to_guess = random.choice(long_adv)

        elif task_num == 10:
            message = "You've worked hard but there's one more task left. It's time for action, so guess a verb."
            long_verb = [w for w in self.get_freq_pos("VERB") if len(w) == 10]
            word_to_guess = random.choice((long_verb))

        return (message, word_to_guess)



