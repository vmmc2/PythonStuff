from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) # dicionario que mapeia para lists...
        for string in strs: # Analisando cada uma das strings
            ht = [0]*26 # Hashtable para os caracteres (letras minusculas)
            for ch in string: # Fazendo uma passagem por cada string...
                ht[ord(ch) - 97] += 1
            # Terminei de fazer a passagem. Hora de guardar no dicionario...
            d[tuple(ht)].append(string) # List eh um tipo de dado unhasheable. Tem que converter para tupla.
        return d.values()
