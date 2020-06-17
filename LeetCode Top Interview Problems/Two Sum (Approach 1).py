class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach 1: Sort the list and apply two pointers.
        # Time Complexity: O(n*log(n))
        # Space Complexity: O(n)
        finale = []
        for i in range(0, len(nums)):
            finale.append((nums[i], i))
        finale.sort()
        left = 0
        right = len(nums) - 1
        answer = []
        while left < right:
            if finale[left][0] + finale[right][0] == target:
                answer.append(finale[left][1])
                answer.append(finale[right][1])
                break
            elif finale[left][0] + finale[right][0] > target:
                right -= 1
            else:
                left += 1
        return answer
                
