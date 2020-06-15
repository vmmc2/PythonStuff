class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach 1: Using sorting -> Complexity: O(n*log(n))
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        elif nums[-1] != nums[-2]:
            return nums[-1]
        else:
            for i in range(1, len(nums) - 1):
                if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                    return nums[i]
        
