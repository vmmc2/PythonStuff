class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Checking if the array is empty.
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            answer = 0
            cursor = answer + 1
            while cursor < len(nums):
                if nums[cursor] != nums[answer]: 
                    answer += 1
                    nums[answer] = nums[cursor]
                cursor += 1
            return answer + 1
            
            
