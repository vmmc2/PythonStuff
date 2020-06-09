# Try and Except

# It is used to surround a dangerous piece of code.
# If the code inside the "try" block works - the "except" is skipped.
# If the code inside the "try" block fails - it goes to the "except" section.

# Take a look at the example below to see how it works:

astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1 #se der problema no bloco "try", eu venho para ca.
print("First:", istr)

astr2 = "123"
try:
    istr2 = int(astr2)
except:
    istr2 = -2
print("Second " + str(istr2))
