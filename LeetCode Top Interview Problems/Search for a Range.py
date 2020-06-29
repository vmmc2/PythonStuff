# if leftRight == False -> busca para a primeira ocorrencia
# if leftRight == True  -> busca para a ultima   ocorrencia
def binarySearch(nums: List[int], left: int, right: int, target: int, leftRight: bool) -> int:
    answer = -1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            answer = mid
            if leftRight == False:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return answer

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # treating the corner case
        if len(nums) == 0:
            return [-1, -1]
        answer = list()
        left = binarySearch(nums, 0, len(nums) - 1, target, False)
        if left == -1: # o numero nao ta presente no array
            return [-1, -1]
        right = binarySearch(nums, 0, len(nums) - 1, target, True)
        answer.append(left)
        answer.append(right)
        return answer
