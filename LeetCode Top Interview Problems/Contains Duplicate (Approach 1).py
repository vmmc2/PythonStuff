class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #First approach, using a dictionary.
        if len(nums) == 0 or len(nums) == 1:
            return False
        else:
            mapa = dict()
            for i in range(0, len(nums)):
                if nums[i] not in mapa:
                    mapa[nums[i]] = 1
                else:
                    return True
            return False
            
        
