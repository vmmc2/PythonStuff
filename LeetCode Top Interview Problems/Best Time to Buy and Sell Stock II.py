class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0 #received an empty list as an input. So, no profit.
        else:
            profit = 0
            for i in range(0, len(prices) - 1):
                low = prices[i]
                high = prices[i + 1]
                if high > low:
                    profit += (high - low)
            return profit
                
            
