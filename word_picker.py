from collections import Counter
import random
import json


class WordPicker:

    def __init__(self):
        """Reads from the words_list.json file (5000 most common words from the Brown corpus)
         and creates a list of lists [word, POS tag] and a set of only words."""
        with open("words_list.json", "r") as json_file:
            final_words_list = json.load(json_file)
        self.all_words = final_words_list
        self.only_words = set([word for word, tag in self.all_words])
        self.message = None
        self.word_to_guess = None

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
            self.message = "Lets start! Try guess the most common noun:"
            self.word_to_guess = self.get_freq_pos("NOUN")[0]

        elif task_num == 2:
            self.message = "Guess an adjective this time:"
            common_adj = [w for w in self.get_freq_pos("ADJ")[:100] if 10 > len(w) > 6]
            self.word_to_guess = random.choice(common_adj)

        elif task_num == 3:
            self.message = "Great work! How about an adverb?:"
            adverb = [w for w, tag in self.all_words[:1500] if
                      8 > len(w) > 5 and tag == "ADV" and not self.is_unique_chars(w)]
            self.word_to_guess = random.choice(adverb)

        elif task_num == 4:
            self.message = "Hmmm, a palindrome perhaps?:"
            palindromes = [w for w in self.only_words if self.is_palindrome(w) and 10 > len(w) > 1]
            self.word_to_guess = random.choice(palindromes)

        elif task_num == 5:
            self.message = "This is a word with all unique letters:"
            unique = [w for w in self.only_words if self.is_unique_chars(w) and len(w) == 7]
            self.word_to_guess = random.choice(unique)

        elif task_num == 6:
            self.message = "Now we got a verb with all unique characters:"
            unique_verbs = [w for w in self.get_freq_pos("VERB") if 7 <= len(w) <= 9 and self.is_unique_chars(w)]
            self.word_to_guess = random.choice(unique_verbs)

        elif task_num == 7:
            self.message = "You got this! Another adjective this time:"
            long_adj = [w for w in self.get_freq_pos("ADJ")[-110:] if len(w) == 9]
            self.word_to_guess = random.choice(long_adj)

        elif task_num == 8:
            self.message = "Is it a noun or is it a verb?! Who knows!:"
            rare_noun_verb = [w for w, tag in self.all_words if 9 >= len(w) > 6 and tag not in {"ADJ", "ADV"}]
            self.word_to_guess = random.choice(rare_noun_verb[-50:])

        elif task_num == 9:
            self.message = "You're close to the end! Try an adverb:"
            long_adv = [w for w in self.get_freq_pos("ADV") if len(w) == 9]
            self.word_to_guess = random.choice(long_adv)

        elif task_num == 10:
            self.message = "Well done! One last task, guess a verb:"
            long_verb = [w for w in self.get_freq_pos("VERB") if len(w) == 10]
            self.word_to_guess = random.choice((long_verb))

        return (self.message, self.word_to_guess)


word_task = WordPicker()
