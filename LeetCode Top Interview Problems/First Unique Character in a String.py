class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurrences = {}
        index = {}
        i = len(s) - 1
        while i >= 0:
            occurrences[s[i]] = occurrences.get(s[i], 0) + 1
            index[s[i]] = i
            i -= 1
        answer = None # guarda o index
        for (key,value) in occurrences.items():
            if value == 1:
                if answer == None or index[key] < answer:
                    answer = index[key]
        if answer == None:
            return -1
        else:
            return answer
        
        
