class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Second approach, using sorting.
        if len(nums) == 0 or len(nums) == 1:
            return False
        else:
            nums.sort() # Diferente das funcoes de string, a funcao sort() de List nao retorna uma nova list
            for i in range(0, len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    return True
            return False
            
        
