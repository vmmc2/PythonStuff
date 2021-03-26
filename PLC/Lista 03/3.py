class Person:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers
        self.hits = 0
    
    def calculateHits(self, lotteryNumbers):
        for i in range(0, len(lotteryNumbers)):
            currentNumber = lotteryNumbers[i]
            for j in range(0, len(self.numbers)):
                if currentNumber == self.numbers[j]:
                    self.hits = self.hits + 1
                    break
    
    def getName(self):
        return self.name

    def getHits(self):
        return self.hits


def main():
    ok = True
    listPeople = []
    finalList = []
    usedNames = {}
    while ok:
        person = input().split()
        if person[0] == "FIM":
            ok = False
        else:
            if person[0] not in usedNames:
                p = Person(person[0], list(map(int, person[1:])))
                listPeople.append(p)
                usedNames[person[0]] = len(listPeople) - 1
            else:
                listPeople[usedNames[person[0]]] = Person(person[0], list(map(int, person[1:])))
    lotteryNumbers = list(map(int, input().split('-')))

    for i in range(0, len(listPeople)):
        listPeople[i].calculateHits(lotteryNumbers)
    for i in range(0, len(listPeople)):
        personName = listPeople[i].getName()
        personHits = listPeople[i].getHits()
        finalList.append((personHits, personName))
    finalList.sort()
    for i in range(0, len(finalList)):
        aux = finalList[i][0]*"+"
        print(finalList[i][1] + " " + aux)
    return


main()
