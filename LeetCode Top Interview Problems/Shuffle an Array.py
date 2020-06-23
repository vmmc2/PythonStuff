class Solution:

    def __init__(self, nums: List[int]):
        self.rn = nums
        self.og = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.rn = self.og
        self.og = list(self.og)
        return self.rn
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(0, len(self.rn)):
            swap_idx = random.randrange(i, len(self.rn))
            temp = self.rn[i]
            self.rn[i] = self.rn[swap_idx]
            self.rn[swap_idx] = temp
        return self.rn


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
