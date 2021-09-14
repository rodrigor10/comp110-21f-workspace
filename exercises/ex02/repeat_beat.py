"""Repeating a beat in a loop."""

__author__ = "730400384"


repeated_word: str = input("What beat do you want to repeat? ")
times: int = int(input("How many times do you want to repeat it? "))
i = 0
wanted_string = " "

if times <= 0:
    print("No beat...")
else:
    while i < times:
        if i == times - 1:
            wanted_string = wanted_string + str(repeated_word)
        else:
            wanted_string = wanted_string + str(repeated_word) + " "
        i = i + 1
    print(wanted_string)