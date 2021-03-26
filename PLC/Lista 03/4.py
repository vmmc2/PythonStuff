from collections import Counter 

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase
        self.phraseLower = phrase.lower()
        self.mapa = Counter(self.phrase)
        self.mapa2 = {}

    def getNumberOfWhitespaces(self):
        return self.mapa[' ']

    def getOccurrencesLetterA(self):
        return (self.mapa['a'] + self.mapa['A'])

    def getMostFrequentPairOfLetters(self):
        for i in range(0, len(self.phraseLower) - 1):
            if self.phraseLower[i].isalpha() and self.phraseLower[i + 1].isalpha():
                self.mapa2[self.phraseLower[i] + self.phraseLower[i + 1]] = self.mapa2.get(self.phraseLower[i] + self.phraseLower[i + 1], 0) + 1
        answer = ["", 0]
        for k,v in self.mapa2.items():
            if v > answer[1]:
                answer[0] = k
                answer[1] = v
        return answer 


def main():
    ok = True
    while ok:
        s = str(input())
        if s == "NAO QUERO MAIS":
            ok = False
        else:
            phr = Phrase(s)
            numWhitespaces = phr.getNumberOfWhitespaces()
            numLetterA = phr.getOccurrencesLetterA()
            ans = phr.getMostFrequentPairOfLetters()
            print(numWhitespaces)
            print(numLetterA)
            if ans[1] == 0:
                print("NENHUM PAR")
            else:
                print(ans[1])
            if ans[0] != "":
                print(ans[0])
    return


main()
