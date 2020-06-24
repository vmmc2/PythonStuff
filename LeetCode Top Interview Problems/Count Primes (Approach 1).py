class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True for i in range(0, n)]
        for i in range(0, n):
            if i == 0 or i == 1:
                isPrime[i] = False
            else:
                for j in range(i, n, i):
                    if j != i:
                        isPrime[j] = False
        counter = 0
        for i in range(0, n):
            if isPrime[i] == True:
                counter += 1
        return counter
