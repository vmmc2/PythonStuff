class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Treating the corner cases first
        if len(matrix) == 0:
            return
        if len(matrix[0]) == 0:
            return
        
        # Now, treating the other cases
        zeroInRow = False
        zeroInColumn = False
        # Checking if there are zeroes inside the first row and inside the first column
        m  = len(matrix)
        n = len(matrix[0])
        for i in range(0, n):
            if matrix[0][i] == 0:
                zeroInRow = True
                break
        for i in range(0, m):
            if matrix[i][0] == 0:
                zeroInColumn = True
                break
        # Now, I do a traversal through the other cells inside the matrix and save the coordinates of the zeroes, if I find one
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,n):
            if matrix[0][i] == 0:
                for j in range(0, m):
                    matrix[j][i] = 0
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(0, n):
                    matrix[i][j] = 0
        if zeroInRow == True:
            for i in range(0, n):
                matrix[0][i] = 0
        if zeroInColumn == True:
            for i in range(0, m):
                matrix[i][0] = 0
        return
        
