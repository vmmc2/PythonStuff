class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Treating the corner case.
        if len(s) <= 1:
            return s
        # Solving the problem for the general case.
        n = len(s)
        answer = s[0]
        dp = [[False for i in range(0, n)] for j in range(0, n)]
        for i in range(0, n):
            dp[i][i] = True
            if i <= n - 2 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
        i = n - 3
        j = i + 2
        mlen = 1
        while i >= 0:
            j = i + 2
            while j < n:
                dp[i][j] = (dp[i+1][j-1] == True and s[i] == s[j])
                j += 1
            i -= 1
        for i in range(0, n):
            for j in range(0, n):
                if dp[i][j] == True:
                    if (j - i + 1) > mlen:
                        mlen = (j - i + 1)
                        answer = s[i: j + 1]
        return answer
