# Notes

## About the use of the int() type conversion.
* Using int() does not apply a round. It just discards the decimal part of the floating-point number.
* As an example, take a look below:
```python
x = 98.6
y = int(98.6)
print(y) # it is going to print: 98
```
