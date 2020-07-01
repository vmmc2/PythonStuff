class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Treating the corner cases...
        if len(nums) < 3:
            return []
        # Solving the problem for the general case...
        answer = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            low = i + 1
            high = len(nums) - 1
            while low < high:
                if nums[low] + nums[high] == 0 - nums[i]:
                    answer.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    high -= 1
                elif nums[low] + nums[high] > 0 - nums[i]:
                    high -= 1
                elif nums[low] + nums[high] < 0 - nums[i]:
                    low += 1
            while i <= len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return answer
