"""Drawing forests in a loop."""

__author__ = "730400384"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

number_of_trees = int(input("Depth: "))
i = 0
trees: str = ""

while i < number_of_trees:
    trees = trees + TREE
    print(trees)
    i = i + 1