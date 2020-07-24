import re

def searchWithRegex(fileName):
  f = open(fileName)
  for line in f:
    line = line.strip()
    if re.search("^From: ", line) == True:
      print(line)
  return
  
  
def main():
  fileName = "mbox-f.txt"
  searchWithRegex(fileName)
  return

if __init__ == "__main__":
  main()
