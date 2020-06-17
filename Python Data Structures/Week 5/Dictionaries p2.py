# THE GET METHOD OF DICTIONARIES IN PYTHON 3

# -> The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common
# that there is a method called get() that does this for us.

taichou = 'Byakuya'
dictionary = {'Ichigo' : 12, 'Aizen': 13}
x = dictionary.get(taichou, 0)
print(x) # It's going to print 0
