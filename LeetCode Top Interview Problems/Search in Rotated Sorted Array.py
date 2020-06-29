class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                answer = mid
                return answer
            # Tem que achar qual das duas metades do array ta ordenada...
            if nums[left] <= nums[mid]: # primeira metade ta ordenada
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]: # segunda metade ta ordenada 
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return answer
