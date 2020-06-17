name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name, 'r')
counts = {}

for line in handle:
    if line[0:5] == "From ":
        words = line.split()
        counts[words[1]] = counts.get(words[1] , 0) + 1
bigWord = None
bigNum = None
for key,value in counts.items():
    if bigNum == None or value > bigNum:
        bigWord = key
        bigNum = value
print(bigWord, bigNum)
