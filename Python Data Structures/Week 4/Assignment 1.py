fname = input("Enter file name: ")
fh = open(fname, 'r')
lst = list()
for line in fh:
    line = line.strip()
    lista = line.split()
    for word in lista:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
