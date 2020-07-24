import re

def stringMatchingNormal():
  f = open("mbox-short.txt")
  for line in f:
    line = line.strip()
    if line.find("From: ") >= 0:
      print(line)
  return

def stringMatchingRegex():
  f = open("mbox-short.txt")
  for line in f:
    line = line.strip()
    if re.search("From: ", line) == True:
      print(line)
  return
  
  
def main():
  stringMatchingNormal()
  stringMatchingRegex()
  return
  
if __init__ == "__main__":
  main()
