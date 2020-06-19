class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # needle eh a substring que eu quero encontrar na string haystack
        found = True
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        else:
            for i in range(0, len(haystack) - len(needle) + 1):
                if needle[0] == haystack[i]:
                    found = True
                    k = 0
                    for j in range(0, len(needle)):
                        if needle[j] != haystack[i + k]:
                            found = False
                            break
                        k += 1
                    if found == True:
                        return i
            return -1
            
        
