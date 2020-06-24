class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n != 0:
            one = n & 1
            if one == 1:
                counter +=1
            n = n >> 1
        return counter
