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
