name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name, 'r')

d = {}
lista = []

for line in handle:
    if line[0:5] == "From ":
        line = line.strip()
        l = line.split()
        time = l[5]
        hour = time.split(":") # hour[0]
        d[hour[0]] = d.get(hour[0], 0) + 1
for (key, value) in d.items():
    lista.append((key, value))
lista = sorted(lista)
for element in lista:
    print(element[0], element[1])

