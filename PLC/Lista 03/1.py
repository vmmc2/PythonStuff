# -> Idade do habitante (homem ou mulher) mais velho
# -> Porcentagem (em relacao a todos os habitantes) de mulheres que tenham
# 18 <= idade <= 35, louras e olhos verdes. 

class Person:
    def __init__(self, sex: str, hairColor: str, eyeColor: str, age: int):
        self.sex = sex
        self.eyeColor = eyeColor
        self.hairColor = hairColor
        self.age = age
    
    def getSex(self) -> str:
        return self.sex
    
    def getEyeColor(self) -> str:
        return self.eyeColor

    def getHairColor(self) -> str:
        return self.hairColor 

    def getAge(self) -> int:
        return self.age


class Solver:
    def __init__(self, personsList):
        self.personsList = personsList

    def getOldestHabitant(self) -> Person:
        maxAge = self.personsList[0].getAge()
        answer = self.personsList[0]
        for i in range(1, len(self.personsList)):
            if self.personsList[i].getAge() > maxAge:
                maxAge = self.personsList[i].getAge()
                answer = self.personsList[i]
        return answer

    def countWomenMeetingCriteria(self) -> int:
        counter = 0
        for i in range(0, len(self.personsList)):
            if self.personsList[i].getSex() == "f" and self.personsList[i].getEyeColor() == "v" and self.personsList[i].getHairColor() == "l" and self.personsList[i].getAge() >= 18 and self.personsList[i].getAge() <= 35:
                counter = counter + 1
        return counter

    def getNumberOfPeople(self) -> int:
        return len(self.personsList)


def main():
    ok = True
    listPeople = []
    while ok:
        age = int(input())
        if age == -1:
            break
        features = input().split()
        listPeople.append(Person(features[0], features[1], features[2], age))
    s = Solver(listPeople)
    print("Mais velho:", s.getOldestHabitant().getAge())
    finale = "Mulheres com olhos verdes, loiras com 18 a 35 anos: {:.02f}%".format((s.countWomenMeetingCriteria()/s.getNumberOfPeople())*100)
    print(finale)
    return


main()
