class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach 2: Using dictionary/hash-map
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        answer = []
        mapa = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in mapa:
                answer = [mapa[complement], i]
            mapa[nums[i]] = i
        return answer
                
