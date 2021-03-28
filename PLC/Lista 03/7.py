class Solver:
    def __init__(self, lista):
        self.carroussel = lista + lista
        self.answer = 1
    
    def getAnswer(self):
        return self.answer 

    def calculateLIS(self):
        curr = 1
        for i in range(0, len(self.carroussel) - 1):
            if self.carroussel[i] < self.carroussel[i + 1]:
                curr += 1
            else:
                self.answer = max(self.answer, curr)
                curr = 1
        return

        
def main():
    n = int(input())
    l = list(map(int, input().split()))
    s = Solver(l)
    s.calculateLIS()
    answer = s.getAnswer()
    print(answer)
    return

if __name__ == "__main__":
    main()
