class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tam = len(nums)
        left = 0
        right = 0
        while right < tam:
            if nums[left] == 0:
                if nums[right] != 0:
                    temp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = temp
                    left += 1
                right += 1
            else:
                left += 1
                right += 1
        return
                
