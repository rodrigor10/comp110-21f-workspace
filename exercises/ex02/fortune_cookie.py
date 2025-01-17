"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730400384"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 

from random import randint
x = int((randint(1, 100)))

print("Your fortune cookie says...")
if x < 25:
    print("Good things are headed your way!!!")
else:
    if x < 50:
        print("Your test grade will come back with a really high score.")
    else:
        if x <= 75:
            print("A special person will come into your life very soon.")
        else:
            print("Danger is headed your way.")

print("Now, go spread positive vibes!")