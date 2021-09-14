"""An exercise in remainders and boolean logic."""

__author__ = "730400384"


# Begin your solution here...
selected_number = int(input("Enter an int: "))
if (selected_number % 2 == 0) and (selected_number % 7 == 0):
    print("TAR HEELS")
else:
    if selected_number % 2 == 0:
        print("TAR")
    else:
        if selected_number % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")