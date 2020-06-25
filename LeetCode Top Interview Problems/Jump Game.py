class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # A tecnica para resolver esse problema é percorrer o array de tras para frente...
        # tratando os corner cases antes:
        if len(nums) == 1:
            return True
        i = len(nums) - 1
        lastGoodIndex = i
        while i >= 0:
            if i + nums[i] >= lastGoodIndex:
                lastGoodIndex = i
            i -= 1
        if lastGoodIndex == 0:
            return True
        else:
            return False
            
