class Solution:
    def aux(self, nums: list, left: int, right: int) -> None:
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
        return
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) == 0:
            return
        times = k % len(nums)
        nums.reverse()
        self.aux(nums, 0, times - 1)
        self.aux(nums, times, len(nums) - 1)
        return
        
