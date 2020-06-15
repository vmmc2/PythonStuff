def number_of_vogals(text):
    dictionary = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letter in text:
        if letter == 'a':
            dictionary[letter] += 1
        elif letter == 'e':
            dictionary[letter] += 1
        elif letter == 'i':
            dictionary[letter] += 1
        elif letter == 'o':
            dictionary[letter] += 1
        elif letter == 'u':
            dictionary[letter] += 1
    return dictionary
    
def main():
    x = 'banana'
    answer = number_of_vogals(x)
    print(x)


if __init__ == "__main__":
    main()
