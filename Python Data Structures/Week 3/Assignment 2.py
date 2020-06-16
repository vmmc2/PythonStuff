# Use the file name mbox-short.txt as the file name
counter = 0
soma = 0.000
fname = input("Enter file name: ")
fh = open(fname, "r")
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        counter += 1
        nLine = line[19:]
        nLine = nLine.lstrip()
        fpNumber = float(nLine)
        soma += fpNumber
answer = soma/counter
print("Average spam confidence:", answer)
