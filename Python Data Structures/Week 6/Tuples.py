# TUPLES

# -> Different from lists, tuples are immutable. You cannot change a tuple.
# -> When we are working with tuples, we have only two methods: .count() and .index()

# Tuples are more efficient:
# -> Since Python does not have to build tuple structures to be modifiable
# they are simpler and more efficient in terms of memory use and performance than lists.
# -> So in our program when we are making "temporary variables", we prefer
# tuples over lists.

tupla = (1, 2, 3)
print(max(tupla)) # prints the maximum value inside the tuple.

tup = (2, 4, -10, 23)
print(max(tup))

# Tuples and assignments
# -> We can also put a tuple on the left-hand side of an assignment statement
(x, y) = (4, 'fred')
print(x) # x == 4
print(y) # y == 'fred'

for element in tup: # printa todos os elementos da tuple.
    print(element)

# Tuples are comparable.

# Sorting a List of Tuples
# -> We can take advantage of the ability to sort a list of tuples to get a sorted version
# of a dictionary.
# -> First we sort the dictionary by the keys using the .items() method and sorted() function.
# I cannot use the .sort() method. (It won't work).
d = {'b': 23, 'd': 120, 'a': 49, 'c': 12}
l = d.items()
l = sorted(l)
print(l)

# Sorting a dictionary by values instead of sorting by keys
c = {'a': 10, 'b': 1, 'c': 22}
tmp = []
for (key,value) in c.items():
    tmp.append((value, key))
print("Not sorted list:", tmp)
tmp = sorted(tmp, reverse = True)
print("Sorted list:", tmp)
