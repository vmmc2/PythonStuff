class Solver:
    def __init__(self, ss):
        self.string = ss
    
    def firstPass(self):
        aux = ""
        for i in range(0, len(self.string)):
            if self.string[i].isalpha():
                aux += chr(ord(self.string[i]) + 3)
            else:
                aux += self.string[i]
        self.string = aux
        return

    def secondPass(self):
        self.string = self.string[::-1]
        return
    
    def thirdPass(self):
        initial = len(self.string)//2
        firstHalf = self.string[0:initial]
        secondHalf = ""
        for i in range(initial, len(self.string)):
            secondHalf += chr(ord(self.string[i]) - 1)
        self.string = firstHalf + secondHalf
        return
    
    def getEncryptedString(self):
        return self.string

def main():
    n = int(input())
    for i in range(0, n):
        ss = input()
        solver = Solver(ss)
        solver.firstPass()
        solver.secondPass()
        solver.thirdPass()
        print(solver.getEncryptedString())
    return

if __name__ == "__main__":
    main()
