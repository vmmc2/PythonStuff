# THE GET METHOD OF DICTIONARIES IN PYTHON 3

# -> The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common
# that there is a method called get() that does this for us.

taichou = 'Byakuya'
dictionary = {'Ichigo' : 12, 'Aizen': 13}
x = dictionary.get(taichou, 0)
print(x) # It's going to print 0

# Simplifying counting with the get() method: Take a look at the example below.
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
  counts[name] = counts.get(name, 0) + 1
print(counts)
