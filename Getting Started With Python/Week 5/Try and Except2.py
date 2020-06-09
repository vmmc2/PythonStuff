def main():
    rawstr = input("Enter a positive number: ")
    try:
        istr = int(rawstr)
    except:
        istr = -1
    if istr >= 0:
        print("Good job! You entered a number!")
    else:
        print("You did not enter a number!")



if __init__ == "__main__":
    main()
