class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [(amount + 1) for i in range(0, amount + 1)]
        coins.sort()
        dp[0] = 0
        for i in range(0, len(dp)):
            for j in range(0, len(coins)):
                if coins[j] > i:
                    break
                else:
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])
        if dp[-1] == amount + 1:
            return -1
        else:
            return dp[-1]
