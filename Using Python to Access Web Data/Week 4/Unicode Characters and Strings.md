# Unicode Characters and Strings

## Representing Simple String
* Each character is represented by a number between 0 and 255 and is stored in 8 bits (1 byte) of memory.
* Remember, we refer to "8 bits of memory" as 1 byte. - i.e (My HardDisk contains 3 Terabytes of memory).
* __IMPORTANT: In Python, the ord() function tells us the numeric value (according to ASCII) of a simple ASCII character.__
* Take a look at the example below:
```python
def mapping()
  print(ord('A')) # It's going to print: 65
  print(ord('a')) # It'll print: 97
  caracter = 'b'
  print(ord(caracter)) # 98
  return
  
  
mapping()
```

## ASCII Table and Unicode.
* We are dealing with character mapping, we must keep in mind that in the 60s and in the 70s, people used to strictly follow the rule of: __1 character = 1 byte of memory.__
* This means that, we always could store a character inside 1 byte of memory. In order words, computers kinda used to work like this:
```
ASCII Table -> 128 characters -> 0 to 127.
Extended ASCII Table -> 256 characters -> 0 to 255.
```
* But nowadays, thins are not so simple. We must deal with hundreds of thousands of characters. In order to do so, Unicode was created. It is basically a new way to represent characters inside the computer.
* Turns out that the Unicode System and the ASCII System overlap when it comes to mapping. So, if you are using just ASCII characters in a Python program, you do not have to worry about it.
* In Python3, we have three different types of strings. We have the normal string, the byte string and the unicode string. Moreover, Python considers that the normal string and the unicode string are part of the String type, so we do not see any difference between them but the byte string is part of the Bytes type.
```python
x = b'abc'  # byte-string
print(type(x)) # <class 'bytes'>
y = 'xyz' # normal-string
print(type(y)) # <class 'str'>
z = u'123' # unicode-string
print(type(z)) # <class 'str'>
```
