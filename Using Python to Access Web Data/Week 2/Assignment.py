import re

def analyze():
    answer = 0
    hand = open('regex_sum_836300.txt')
    for line in hand:
        line = line.strip()
        y = re.findall('[0-9]+' , line)
        if len(y) >= 1:
            for element in y:
                answer += int(element)
    print(answer)


analyze()
