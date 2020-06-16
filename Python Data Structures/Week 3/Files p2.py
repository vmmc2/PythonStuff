# PROCESSING FILES

# File Handles as a Sequence:
# Remember that the file handle works like an interface between our program and the actual file store inside the second memory (hard disk).
# A file handle open for read can be treated as a sequence of strings where
# each line in the file is a string in the sequence.

# We can use the for statement to iterate through a sequence.

# Remember - a sequence is an ordered set.

# Newline in print() statements and in the files:
# -> Each line from the file has a newline at the end.
# -> The print statement adds a newline to each line.
# To solve this, we can use the .rstrip() method from the string library. We can do this because a newline is considered a whitespace.



# It is also possible to read the whole file (newlines and all) at once.
# By doing this, we are going to store the whole file inside a single string.
# If we print this string, we are going to have a formated output because we will now
# where to jump to a new line thanks to the '\n' character.
# To do so, we must use the method .read()
# Take a look at it in the code shown below:

# USING THE "IN" KEYWORD TO SELECT LINES INSIDE A FILE:
# -> We can look for a string anywhere in a line as our selection criteria
# Take a look at the function: find_substring_in_file_line()

#########################################################################
# DEALING WITH A BAD FILE NAME:

fname = input('Enter the file name: ')
try:
    fhand = open(fname, "r")
except:
    print("File cannot be opened:", fname)
    quit()
count = 0
for line in fhand:
    if line.startsWith("Subject:"):
        count += 1
print("There were", count, "subject lines in", fname)
##########################################################################


def find_substring_in_file_line(filename):
    fhand = open(filename, "r")
    for line in fhand:
        line = line.rstrip()
        if "@cin.ufpe.br" in line:
            print(line)
    return



def readAllFileContent(filename):
    archive = open(filename, "r")
    content = archive.read()
    print(content)
    return  

def count_file_number_lines(filename):
    fhandle = open(filename, "r")
    nLines = 0
    for line in fhandle:
        nLines += 1
    print("The number of lines inside this file is:", nLines)
    return

def main():
    # This piece of code is opening a file called "teste.txt" using the read mode
    # and for each line inside this file, we are printing it.
    fhandle = open("teste.txt", "r")
    for line in fhandle:
        line = line.rstrip()
        print(line)
    print("\n")
    count_file_number_lines("teste.txt")


if __init__ == "__main__":
    main()
