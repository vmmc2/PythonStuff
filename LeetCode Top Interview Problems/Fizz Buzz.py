class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 != 0 and i % 5 != 0:
                answer.append(str(i))
            elif i % 3 == 0 and i % 5 != 0:
                answer.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append("FizzBuzz")
        return answer
            
