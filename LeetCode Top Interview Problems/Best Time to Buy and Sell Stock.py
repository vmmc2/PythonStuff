class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Treating the corner cases
        if len(prices) <= 1:
            return 0
        # Treating the general cases
        profit = 0
        minimo = prices[0]
        for i in range(0, len(prices)):
            if prices[i] > minimo:
                profit = max(profit, prices[i] - minimo)
            elif prices[i] < minimo:
                minimo = prices[i]
        return profit
        
        
