answer = []

class Solution:
    def helper(self, nums: List[int], cursor: int, tam: int, pseudo: List[int]) -> None:
        global answer
        if cursor >= tam:
            answer.append(pseudo)
            return
        self.helper(nums, cursor + 1, tam, pseudo + [nums[cursor]])
        self.helper(nums, cursor + 1, tam, pseudo)
        return
    def subsets(self, nums: List[int]) -> List[List[int]]:
        global answer
        answer = []
        # Treating the corner case...
        if len(nums) == 0:
            return [[]]
        # Treating the general case
        pseudo = []
        cursor = 0
        tam = len(nums)
        self.helper(nums, cursor, tam, pseudo)
        return answer
        
