class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach 2: Using only constant memory
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        candidate = nums[0]
        occurrences = 0
        for i in range(0, len(nums)):
            if occurrences == 0:
                candidate = nums[i]
            if candidate == nums[i]:
                occurrences += 1
            else:
                occurrences -= 1
        return candidate
        
