class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Treating corner cases...
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        answer = False
        row = 0
        column = len(matrix[0]) - 1
        while row < len(matrix) and column >= 0:
            if matrix[row][column] == target:
                answer = True
                return answer
            elif matrix[row][column] > target:
                column -= 1
            elif matrix[row][column] < target:
                row += 1
        return answer
        
