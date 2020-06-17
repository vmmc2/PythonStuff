# LISTS VS STRINGS
# -> Strings are immutable - we cannot change the content of a string.
# We must make a new string to make any change.
# -> Lists are mutable - we can change an element of a list using the index
# operator.

# USING THE RANGE FUNCTION
# -> The range() function returns a list of numbers that range from zero
# to one less than the parameter.
# -> We can construct an index loop using for and an integer iterator.

def list_range_example(number):
    print(range(number)) # [0, 1, 2, 3, ..., number - 1]
    war_potentials = ['Ichigo', 'Aizen', 'Kenpachi', 'Urahara', 'Ichibei']
    print(range(len(war_potentials)))

def main():
    lotto = [2, 14, 26, 41, 63]
    print(lotto)
    lotto[2] = 28 # Now the list is: [2, 14, 28, 41, 63]
    print(lotto)
    list_range_example(4)

if __init__ == "__main__":
    main()
