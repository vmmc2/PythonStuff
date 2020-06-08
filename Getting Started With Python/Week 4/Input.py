# Input in Python

# We can instruct Python to pause and read data from the user using the input() function.
# The input() function returns a string (str).
# Take a look at the example below:

name = input("Who are you?")
print("Hi, my name is: ", name)

# Simple Exercise:
# European Floor: 0
# USA Floor: 1
eufloor = input("In which floor you are at?")
usfloor = int(eufloor) + 1
print("US Floor is: ", usfloor)
