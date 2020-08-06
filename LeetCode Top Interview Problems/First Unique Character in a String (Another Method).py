class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0] * 26
        firstapp = [0] * 26
        
        i = len(s) - 1
        while i >= 0:
            freq[ord(s[i]) - ord('a')] += 1
            firstapp[ord(s[i]) - ord('a')] = i
            i -= 1
            
        answer = None
        for i in range(0, 26):
            if freq[i] == 1:
                if answer == None:
                    answer = firstapp[i]
                else:
                    answer = min(answer, firstapp[i])
        if answer == None:
            return -1
        else:
            return answer
        
