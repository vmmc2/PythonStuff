# DICTIONARIES
# -> Lists index their entries on the position in the list.
# -> Dictionaries are like bags: no order.
# -> So we index the things we put in the dictionary with a "lookup tag".
# -> Dictionaries are mutable (just as lists).

# These are two different ways of creating a dictionary.
purse = dict()
another_map = {}

purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
purse['dale'] = None
print(purse['candy'])
print(purse['dale'])
print(purse)
purse['candy'] += 2
print(purse)
