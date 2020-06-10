def findMinimumValue(numbers):
  smallest = None # None eh a ausencia de valor. Funciona como o NULL de C/C++
  for element in numbers:
    if smallest == None:
      smallest = element
    elif smallest > element:
      smallest = element
  return smallest


def main():
    numbers = []
    qtd = input("How many numbers in the list?")
    qtd = int(qtd)
    for i in range(0, qtd):
      num = int(input())
      numbers.append(num)
    print(numbers)
    answer = findMinimumValue(numbers)
    print("The minimum value is:", answer)


main()
