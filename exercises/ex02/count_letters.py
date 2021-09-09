"""Counting letters in a string."""

__author__ = "730400384"


# Begin your solution here...
searched_letter = str(input("What letter do you want to search for?: "))
word_entered = str(input("Enter a word: "))
i = 0
length_of_word = int(len(word_entered))
amount_of_letters = 0

while i < length_of_word:
    if searched_letter == word_entered[i]:
        amount_of_letters = amount_of_letters + 1
    i = i + 1
print("Count: " + str(amount_of_letters))