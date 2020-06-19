class Solution:
    def countAndSay(self, n: int) -> str:
        d = {
            1 : '1',
            2 : '11',
            3 : '21',
            4 : '1211',
            5 : '111221',
        }
        if n in d:
            return d[n]
        else:
            i = 5
            while i <= n:
                a = d[i]
                b = ""
                counter = 1
                for j in range(1, len(a)):
                    if a[j] != a[j - 1]:
                        b += str(counter) + a[j - 1]
                        counter = 1
                        if j == len(a) - 1:
                            b += str(counter) + a[j]
                    else:
                        counter += 1
                        if j == len(a) - 1:
                            b += str(counter) + a[j]
                d[i + 1] = b
                i += 1
            return d[n]
                        
            
