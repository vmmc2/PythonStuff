import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Treating the corner cases first
        if n < 1:
            return False
        # Considering that the input number n is inside the range [-(2^31) , (2^31) - 1]
        number = 3**(math.floor(math.log(2**31 - 1,3)))
        if number % n == 0:
            return True
        else:
            return False

###################################################################################################################################################################################        
import math

class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        # Corner case.
        if n <= 0:
            return False
        # O problema garante para a gente que todos o numeros fornecidos como input sao de 32 bits.
        # Isso significa que: o maior numero que a gente pode receber eh (2**31) - 1
        # Precisamos descobrir qual eh o maior numero nesse range [0, (2**31) - 1] que eh uma potencia de 3.
        # Para isso, basta fazer logo na base 3.
        exp = math.floor(math.log(2**31 - 1, 3))
        biggestpowerof3 = 3**exp
        # Feito isso, para descobrirmos se um numero X eh uma potencia de 3, basta ver se o resto da divisao de:
        # biggestpowerof3//X == 0
        if biggestpowerof3 % n == 0:
            return True
        else:
            return False
