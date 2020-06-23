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
