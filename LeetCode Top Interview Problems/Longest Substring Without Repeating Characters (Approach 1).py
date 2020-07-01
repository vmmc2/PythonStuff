class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Treating the corner case:
        if len(s) <= 1:
            return len(s)
        # Treating the general cases:
        n = len(s)
        tams = 0
        answer = -1
        for i in range(0, n):
            d = {}
            tams = 0
            for j in range(i, n):
                if s[j] not in d:
                    d[s[j]] = 1
                    tams += 1
                else:
                    answer = max(answer, tams)
                    break
            answer = max(answer, tams)
        return answer
