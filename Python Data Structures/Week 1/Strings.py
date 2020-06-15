# String Data Type

# A string is a sequence of characters.
# A string literal uses single-quotes or double-quotes: 'Hello World' or "Hello World".
# For strings, '+' means concatenate.
# When a string contains numbers, it is still a string.
# We can convert a string containing numbers into a number by using the function int()

def main():
    fruit = 'banana'
    letter = fruit[1]
    print(letter) # it is going to print 'a'
    
    x = 3
    w = fruit[x - 1]
    print(w) # it is going to print 'n'
    
    vegetable = 'lettuce'
    size = len(vegetable) # to get the length/size of the string, we can use a built-in function called: len()
    print(size)
    
    #Printing every single letter/character inside a string.
    for letter in vegetable:
        print(letter) # this piece of code is going to print all characters (line per line) that are inside the string vegetable.



if __init__ == "__main__":
    main()
