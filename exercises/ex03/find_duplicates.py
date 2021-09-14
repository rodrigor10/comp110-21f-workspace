"""Finding duplicate letters in a word."""

__author__ = "730400384"

word = input("Enter a word: ")
length_of_word = int(len(word))
i = 0
final_decision = False

while i < length_of_word:
    first_character = word[i]
    x = i + 1
    while x < length_of_word:
        second_character = word[x]
        x = x + 1
        if first_character == second_character:
            final_decision = True
    i = i + 1
print("Found duplicate: " + str(final_decision))