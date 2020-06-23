class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: # Empty string is considered a valid string.
            return True
        if len(s) % 2 != 0: # Not a valid string. The brackets must come in pairs
            return False
        stack = []
        for i in range(0, len(s)):
            if s[i] == "{" or s[i] =='(' or s[i] == '[':
                stack.append(s[i])
            else:
                if s[i] == ')':
                    if len(stack) == 0 or stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                elif s[i] == '}':
                    if len(stack) == 0 or stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
                elif s[i] == ']':
                    if len(stack) == 0 or stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
        if len(stack) > 0:
            return False
        return True
