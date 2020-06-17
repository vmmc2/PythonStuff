# LISTS AND STRINGS
# The split() method breaks a string into parts and produces a list of strings.
# We can think of these as words.
# We can access a particular word of loop through all the words.

abc = "A string with five words"
stuff = abc.split()
print(stuff) # ['A', 'string', 'with', 'five', 'words']
print(len(stuff)) # 5
print(stuff[1]) # 'string'
