# Opening a File

# Before we can read the contents of a file, we must tell Python which file we are going to work with and also what we will be doing with the file.
# This is done with the open() function.
# This open() function returns a "file handle" - a variable used to perform operations on the file.

# Example

# handle = open(filename, mode)
# -> handle is a variable used to manipulate the file.
# -> filename is the name of the file that we are going to interact with. It is a string.
# -> mode is optional and should be 'r' if we are planning to read the file. Otherwise, it should be 'w' if we are planning to write to the file.
fhand = open('mbox.txt' , 'r')
