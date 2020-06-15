from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach 2: Using dictionary -> Complexity: O(n)
        mapa = defaultdict(int)
        for i in range(0, len(nums)):
            if nums[i] not in mapa:
                mapa[nums[i]] = 1
            else:
                mapa[nums[i]] += 1
        for key,value in mapa.items():
            if value == 1:
                return key
        
        
