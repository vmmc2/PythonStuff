fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname, 'r')
count = 0
answer = []
for line in fh:
    if line[0:5] == 'From ':
        count += 1
        pseudo = line.split()
        answer.append(pseudo[1])
for element in answer:
    print(element)
print("There were", count, "lines in the file with From as the first word")
