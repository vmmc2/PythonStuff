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
    
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Para fazer a rotacao de uma matriz seja no sentido horario (clockwise) ou no sentido anti-horario (anti-clockwise), a gente precisa realizar duas etapas. Essas duas etapas mudam de ordem dependendo de qual transformacao estamos efetuando.
        # No caso de uma rotacao clockwise, fazemos o seguinte: Pegamos a matriz, calculamos a sua transposta. Em seguida, invertemos linha por linha.
        # Ja no caso de uma rotacao anti-clockwise, fazemos o seguinte: Pegamos a matriz, invertemos as linha. Em seguida, calculamos a sua transposta.
        
        # Treating the corner case:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return
        # First Step
        for i in range(0, m):
            for j in range(0, n):
                if i == j:
                    continue
                elif i > j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        # Second Step
        for i in range(0, m):
            left = 0
            right = n - 1
            while left < right:
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left += 1
                right -= 1
        return
        
