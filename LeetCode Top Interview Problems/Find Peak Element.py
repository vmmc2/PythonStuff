class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Treating the corner cases...
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        elif nums[-2] < nums[-1]:
            return (len(nums) - 1)
        # Treating the general cases
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:
                low = mid
            elif nums[mid - 1] > nums[mid] and nums[mid] > nums[mid + 1]:
                high = mid
            elif nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]:
                high = mid
        return -1
            
