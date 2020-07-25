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
* Pay attention to the size of the list that we received as an output. It might be possible that there is no substring that matches the regular expression provided. If that's the case, then we are going to receive an empty list. If there is 1 substring that matches the regular expression, then the size of the list is going to be 1. If there are 2 substrings, then the size of the list is going to be 2, and so on...

## Greedy Matching
* Considering the example above, suppose that the value of the string s would be the following:
```python
import re

s = "From: Using the: character"
y = re.findall('^F.+:' , s)
print(y)
```
* Qual seria a substring retornada? Seria "From:" ou seria "From: Using the:" ??? Ao testarmos o codigo escrito acima, vemos que o resultado eh a substring "From: Using the:", isso acontece porque, por definicao, o matching the regular expressions utiliza uma abordagem gulosa conhecida como greedy matching. __Ou seja, quando chamamos a funcao re.findall(), ele tenta encontrar a maior substring que consiga dar match com a regular expression fornecida. Por causa disso que o resultado eh a string "From: Using the:"__
* Em outras palavras, temos que:
  * Greedy Matching: Maior susbstring possivel que case com a regular expression fornecida.
  * Non-Greedy Matching: Menor substring possivel que case com a regular expression fornecida.
