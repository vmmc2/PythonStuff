class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach number 1: Using a Map/Dictionary.
        # Time Complexity: O(n)
        # Space Complexity: O(k) where k is the quantity of unique numbers inside the nums array.
        d = {}
        for i in range(0, len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
        for (key,value) in d.items():
            if value > len(nums)//2:
                return key
        
