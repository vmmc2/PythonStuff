class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        real_sum = sum(nums)
        expected_sum = ((1 + len(nums))*len(nums))//2
        answer = expected_sum - real_sum
        return answer
