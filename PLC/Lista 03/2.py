class Solver:
    def __init__(self, dic, phrases):
        self.dic = dic
        self.phrases = phrases
        self.translatedPhrases = []

    def translatePhrase(self, phrase):
        words = phrase.split()
        translatedWords = []
        for word in words:
            translatedWords.append(self.dic[word])
        answer = " ".join(translatedWords)
        return answer

    def translateEverything(self):
        for i in range(0, len(self.phrases)):
            currentPhrase = self.phrases[i]
            self.translatedPhrases.append(self.translatePhrase(currentPhrase))

    def getTranslatedPhrases(self):
        return self.translatedPhrases


def main():
    dic = {}
    phrases = []
    ok = True
    numberOfWords = int(input())
    for i in range(0, numberOfWords):
        words = input().split()
        dic[words[0]] = words[2]
    while ok:
        phrase = input()
        if phrase == "*":
            ok = False
        else:
            phrases.append(phrase)
    s = Solver(dic, phrases)
    s.translateEverything()
    tnsStrings = s.getTranslatedPhrases()
    for i in range(0, len(tnsStrings)):
        print(tnsStrings[i])
    return


main()
