import re

def searchWithRegex(fileName):
  f = open(fileName)
  for line in f:
    line = line.strip()
    if re.search("^From: ", line) == True: # Indica que o casamento de strings/padroes deve acontecer logo no inicio da linha. Em outras palavras, o primeiro caractere da linha deve ser 'F'.
      print(line)
  return
  
  
def main():
  fileName = "mbox-f.txt"
  searchWithRegex(fileName)
  return

if __init__ == "__main__":
  main()
