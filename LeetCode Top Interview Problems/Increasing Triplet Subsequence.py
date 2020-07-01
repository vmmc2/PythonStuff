
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Treating the corner cases first:
        if len(nums) <= 2:
            return False
        # Treating the general case:
        primeiro = 2**33
        segundo = 2**33
        for i in range(0, len(nums)):
            if nums[i] < primeiro:
                primeiro = nums[i]
            if nums[i] > primeiro:
                segundo = min(nums[i], segundo)
            if nums[i] > segundo:
                return True
        return False
