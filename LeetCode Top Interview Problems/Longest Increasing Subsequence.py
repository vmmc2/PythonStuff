class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Treating the corner cases first...
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        # Treating the general case
        dp = [1] * len(nums)
        for i in range(1, len(dp)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        answer = None
        for element in dp:
            if answer == None or element > answer:
                answer = element
        return answer
