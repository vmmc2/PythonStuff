# IS SOMETHING IN A LIST?
# -> Python provides two operators that let you check if an element/item
# is inside a list
# -> These operators are: "in" and "not in".
# -> These logical operators return True or False.
# -> They do not modify the list.

lista = [1, 9, 10, 16, 21]
if 9 in lista: # True
    print("9 ta presente na lista")
if 20 not in lista: # True
    print("20 nao ta presente na lista")

# LISTS ARE IN ORDER
# -> A list can hold many items and keeps those items in the order until we
# do something to change the order.
# -> A list can be sorted. This means that we can change the order of the list.
# -> The sort() method (unlike strings) means "sort yourself".

friends = ['Joseph', 'Gleen', 'Sally', 'Benjamin']
print(friends)
friends.sort() # Vai ordenar a list de strings em ordem alfabetica.
print(friends) # ['Benjamin', 'Gleen', 'Joseph', 'Sally']
print(friends[1]) # 'Gleen'


