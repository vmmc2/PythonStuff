class Solution:
    def countAndSay(self, n: int) -> str:
        d = {
            1 : '1',
        }
        # Base case...
        if n == 1:
            return d[n]
        # General case...
        for i in range(2, n + 1):
            prevstring = d[i - 1]
            ns = ''
            counter = 1
            currentchar = prevstring[0]
            for j in range(1, len(prevstring)):
                if currentchar == prevstring[j]:
                    counter += 1
                elif currentchar != prevstring[j]:
                    ns += str(counter) + currentchar
                    counter = 1
                    currentchar = prevstring[j]
            ns += str(counter) + currentchar
            d[i] = ns
        return d[n]
        
