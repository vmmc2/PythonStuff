answer = []

class Solution:
    def helper(self, digits: str, cursor: int, tam: int, d: dict, now: str) -> None:
        global answer
        if cursor == tam:
            answer.append(now)
            return
        dig = digits[cursor]
        letters = d[dig]
        for letter in letters:
            self.helper(digits, cursor + 1, tam, d, now + letter)
        return
        
    def letterCombinations(self, digits: str) -> List[str]:
        # Corner case...
        if digits == "":
            return []
        # General cases...
        global answer
        answer = []
        d = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        cursor = 0
        tam = len(digits)
        now = ""
        self.helper(digits, cursor, tam, d, now)
        return answer
