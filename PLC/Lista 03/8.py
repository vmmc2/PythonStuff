class Solver:
    def __init__(self, lista, maxLen, k):
        self.words = lista
        self.maxLen = maxLen 
        self.dic = {}
        self.answer = []
        self.k = k
    
    def calculate(self):
        for i in range(0, len(self.words)):
            for j in range(1, len(self.words[i]) + 1):
                self.dic[self.words[i][:j]] = self.dic.get(self.words[i][:j], 0) + 1
        return
    
    def getAnswer(self):
        ans = []
        for key,value in self.dic.items():
            if value >= self.k:
                ans.append(key)
        ans.sort()
        return ans


def main():
    nk = list(map(int, input().split()))
    n = nk[0]
    k = nk[1]
    words = []
    for i in range(0, n):
        word = input()
        words.append(word)
    maxLen = len(words[-1])
    s = Solver(words, maxLen, k)
    s.calculate()
    finale = s.getAnswer()
    print(len(finale))
    for word in finale:
        print(word)
    return 


if __name__ == "__main__":
    main()
