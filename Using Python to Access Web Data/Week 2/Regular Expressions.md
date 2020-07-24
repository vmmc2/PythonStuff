# Regular Expressions

## Intro
* In computer science, regular expression are also called __regex__ or __regexp__. This is a tool that provides concise and flexible means for matching strings of a text, such as particular characters, words or patterns of characters.
* A regular expression is written in a formal language that can be interpreted by a regular expression processor.

## Regular Expression Quick Guide
* '^' -> Matches the beginning of a line.
* '$' -> Matches the end of the line.
* '.' -> Matches any character.
* '\s' -> Matches whitespace.
* '\S' -> Matches any non-whitespace character.
* '*' -> Repeats a character zero or more times.
* '*?' -> Repeats a character zero or more times (non-greedy).
* '+' -> Repeats a character one or more times.
* '+?' -> Repeats a character one or more times (non-greedy).
* [aeiou] -> Matches a single character in the listed set.
* [^XYZ] -> Matches a single character not in the listed set.
* [a-z0-9] -> Set of characters can include a range.
* '(' -> Indicates where string extraction is to start.
* ')' -> Indicates where string extraction is to end.

## Observations
* In order to use the features of regular expressions, you must first import the module that has all the features to work with it. You can do this in 1 line by using the following statement: 
```python
import re
```
