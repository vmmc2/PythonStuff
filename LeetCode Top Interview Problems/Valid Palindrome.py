# Lembrando que a funcao ord() retorna a posicao na tabela ASCII de um caracter especifico.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        s2 = ""
        for i in range(0, len(s1)):
            if (ord(s1[i]) >= 48 and ord(s1[i]) <= 57) or (ord(s1[i]) >= 65 and ord(s1[i]) <= 90) or (ord(s1[i]) >= 97 and ord(s1[i]) <= 122):
                s2 += s1[i]
        left = 0
        right = len(s2) - 1
        while left <= right:
            if s2[left] != s2[right]:
                return False
            left += 1
            right -= 1
        return True
        
        
