class Solution:
    def titleToNumber(self, s: str) -> int:
        # Solucao para a questao:
        # Complexidade Temporal: O(n)
        # Complexidade Espacial: O(1)
        exp = 0
        answer = 0
        curr = len(s) - 1
        while curr >= 0:
            answer += (26**exp) * (ord(s[curr]) - ord('A') + 1)
            curr -= 1
            exp += 1
        return answer
