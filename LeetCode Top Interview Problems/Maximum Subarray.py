class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Treating the corner case.
        if len(nums) == 0:
            return 0
        # Treating the general cases.
        local_max = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            local_max = max(nums[i], local_max + nums[i])
            if local_max > global_max:
                global_max = local_max
        return global_max
            
