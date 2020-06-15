# String Library.

# Python has a number of string functions which are in the string library.
# These functions are already built into every single string - we invoke them by appending the function to the string variable.
# These functions do not modify the original string. Instead, they return a new string that has been altered.

greet = "Hello Bob"
print(greet)
zap = greet.lower() # pego a string greet, deixo todos os seus caracterers como letras minusculas e retorno essa nova string.
print(zap)

print("Hello There, Baby".lower())


# The find() method.

# We use this method to check whether a string/char/substring exists inside another string.
# It does not return True or False.
# It returns the index of the first occurrence of the substring inside the string. If we do not find the substring inside the string, we return -1.

fruit = "banana"
pos = fruit.find('na')
print(pos) # it is going to print 2.

zz = fruit.find('z')
print(zz) # it is going to print -1 because we did not find the substring 'z' inside the string 'banana'.
