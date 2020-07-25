# Extracting Data with Regex

## Intro
* re.search() returns True or False depending on whether the string matches the regular expression that we provided in the function.
* As we already saw, there is another function called re.findall(). This function is used if we actually want the matching strings to be extracted. To be more specific, we give a bunch a string and we also give a regex to this function (remember that the regex works like a template). Then, the function re.findall() is going to return a list containing all the substring of the provided string that match the regular expression. 
* For more info, take a look below:
```python
import re

s = "My 2 favorite numbers are: 19 and 42"
y = re.findall('[0-9]+' , s)
print(y) 

# The print() function above is going to provide the following result: y = ['2', '19', '42']
```
