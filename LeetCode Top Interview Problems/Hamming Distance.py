class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xr = x ^ y
        counter = 0
        while xr != 0:
            if xr & 1 == 1:
                counter += 1
            xr = xr >> 1
        return counter
        
