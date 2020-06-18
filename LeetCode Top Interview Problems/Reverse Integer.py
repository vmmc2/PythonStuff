class Solution:
    def reverse(self, x: int) -> int:
        negative = 0
        if x < 0:
            x = x * (-1)
            negative = 1
        answer = 0
        while x != 0:
            answer = answer * 10
            answer = answer + (x % 10)
            x = x//10
        if negative == 1:
            answer = answer * (-1)
        if answer < -2147483648 or answer > 2147483647:
            return 0
        return answer
        
        
