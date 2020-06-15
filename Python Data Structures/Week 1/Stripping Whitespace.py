# Sometimes we want to take a string and remove whitespaces at the beginning or/and at the end of the string.
# In order to do so, we have some methods that we can use: lstrip(), rstrip(), strip().
# lstrip() removes whitespaces at the left.
# rstrip() removes whitespaces at the right.
# strip() removes whitespaces at both left and right (removes whitespaces at both beginning and ending of the string).

greet = "     Hello Bob  "
print(greet)

greet1 = greet.lstrip()
print(greet1) # "Hello Bob  "

greet2 = greet.rstrip()
print(greet2) # "     Hello Bob "

greet3 = greet.strip()
print(greet3) # "Hello Bob"
