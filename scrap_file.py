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

my_list = ['whatever', 'huh', 'huh', 'huh', 'whatever', 'huh', 'heya', '444']

indices = [i for i, "whatever" in enumerate(my_list)]

print(indices)

print(my_list)

print(len(indices))