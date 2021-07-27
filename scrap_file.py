# num = 8
#
# while num < 12:
#     print("hi")
#     num += 2
#
# print(num)

# word = "hello"
#
# listLetters = list(word)
#
# print(listLetters)

# string = "nUMber"
#
# if string.isalpha():
#     print(string.lower())
# else:
#     print("NOPE")

# string = "  the Game "
#
# print(string.strip())
# print(string)

# my_list = ['whatever', 'hi', '7', 'huh', 'hiya', 'whatever', '444']
#
# my_string = 'words55wordswords'
#
# indices = [j for j, x in enumerate(my_string) if x == "5"]
#
# print(indices)
#
# print(my_list)
#
# print(len(indices))


# my_string = '  worDDs55 wordswords  '
#
# if "s" in my_string:
#     print("indeed")
#
# wow = my_string.lower().strip()
#
# print(wow)


def pick_word(word):
    hidden_word = len(word) * "_ "
    print(word)
    return hidden_word

print(pick_word('hiii'))