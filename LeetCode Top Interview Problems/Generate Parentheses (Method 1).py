answer = []

class Solution:
    def checkParenthesis(self, s: str) -> bool:
        stack = []
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True
    
    def helper(self, s: str, cursor: int, tam: int) -> None:
        global answer
        if cursor >= tam:
            if self.checkParenthesis(s) == True:
                answer.append(s)
            return
        self.helper(s + "(", cursor + 1, tam)
        self.helper(s + ")", cursor + 1, tam)
        return
    
    def generateParenthesis(self, n: int) -> List[str]:
        global answer
        answer = []
        # Treating the corner case...
        if n == 0:
            return answer
        # Treating the general cases...
        tam = 2 * n
        cursor = 0
        s = ""
        self.helper(s, cursor, tam)
        return answer
