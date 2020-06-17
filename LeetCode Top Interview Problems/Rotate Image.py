class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Primeiro passo: Pegar a transposta da matriz
        tamanho = len(matrix)
        for i in range(0, tamanho):
            for j in range(0, tamanho):
                if i >= j: continue
                else:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        # Segundo passo: inverter as linhas.
        for i in range(0, tamanho):
            matrix[i].reverse()
        return
        
