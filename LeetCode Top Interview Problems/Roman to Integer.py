class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        i = 0
        while i < len(s):
            if s[i] == 'I':
                if i < len(s) - 1:
                    if s[i + 1] == 'V':
                        answer += 4
                        i += 2
                    elif s[i + 1] == 'X':
                        answer += 9
                        i += 2
                    else:
                        answer += 1
                        i += 1
                else:
                    answer += 1
                    i += 1
            elif s[i] == 'V':
                answer += 5
                i += 1
            elif s[i] == 'X':
                if i < len(s) - 1:
                    if s[i + 1] == 'L':
                        answer += 40
                        i += 2
                    elif s[i + 1] == 'C':
                        answer += 90
                        i += 2
                    else:
                        answer += 10
                        i += 1
                else:
                    answer += 10
                    i += 1
            elif s[i] == 'L':
                answer += 50
                i += 1
            elif s[i] == 'C':
                if i < len(s) - 1:
                    if s[i + 1] == 'D':
                        answer += 400
                        i += 2
                    elif s[i + 1] == 'M':
                        answer += 900
                        i += 2
                    else:
                        answer += 100
                        i += 1
                else:
                    answer += 100
                    i += 1
            elif s[i] == 'D':
                answer += 500
                i += 1
            elif s[i] == 'M':
                answer += 1000
                i += 1
        return answer
