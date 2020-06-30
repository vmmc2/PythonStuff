class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Treating the corner cases first...
        if len(nums) <= 1:
            return
        # Treating the general case...
        low = 0
        curr = 0
        high = len(nums) - 1
        while curr <= high:
            if nums[curr] == 0:
                temp = nums[low]
                nums[low] = nums[curr]
                nums[curr] = temp
                low += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            elif nums[curr] == 2:
                temp = nums[high]
                nums[high] = nums[curr]
                nums[curr] = temp
                high -= 1
        return
