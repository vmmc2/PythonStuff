class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            # o tamanho do longestCommonPrefix pode ser no maximo o tamanho da menor string na lista.
            # Tem que descobrir qual eh esse valor.
            tam = None
            for element in strs:
                if tam == None or len(element) > tam:
                    tam = len(element)
            # Agora a gente pode comecar a iterar sobre a lista de strings.
            cur = 1
            ok = True
            answer = ""
            while cur <= tam and ok == True:
                current = strs[0][0:cur]
                for element in strs:
                    if current != element[0:cur]:
                        ok = False
                if ok == True:
                    answer = current
                cur += 1
            return answer
                
            
