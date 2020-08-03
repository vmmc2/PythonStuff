class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Corner case:
        if len(board) == 0:
            return
        if len(board[0]) == 0:
            return
        # General cases:
        m = len(board)
        n = len(board[0])
        for i in range(0, m):
            for j in range(0, n):
                neighbours = 0
                if board[i][j] == 0:
                    if i == 0 and j == 0:
                        neighbours += board[i + 1][j]
                        neighbours += board[i][j + 1]
                        neighbours += board[i + 1][j + 1]
                    elif i == 0 and j == n - 1:
                        neighbours += board[i + 1][j]
                        neighbours += board[i][j - 1]
                        neighbours += board[i + 1][j - 1]
                    elif i == m - 1 and j == 0:
                        neighbours += board[i - 1][j]
                        neighbours += board[i][j + 1]
                        neighbours += board[i - 1][j + 1]
                    elif i == m - 1 and j == n - 1:
                        neighbours += board[i - 1][j]
                        neighbours += board[i][j - 1]
                        neighbours += board[i - 1][j - 1]
                    elif i == 0 and (j > 0 and j < n - 1):
                        neighbours += board[i][j - 1]
                        neighbours += board[i + 1][j - 1]
                        neighbours += board[i + 1][j]
                        neighbours += board[i + 1][j + 1]
                        neighbours += board[i][j + 1]
                    elif i == m - 1 and (j > 0 and j < n - 1):
                        neighbours += board[i][j - 1]
                        neighbours += board[i - 1][j - 1]
                        neighbours += board[i - 1][j]
                        neighbours += board[i - 1][j + 1]
                        neighbours += board[i][j + 1]
                    elif (i > 0 and i < m - 1) and j == 0:
                        neighbours += board[i - 1][j]
                        neighbours += board[i - 1][j + 1]
                        neighbours += board[i][j + 1]
                        neighbours += board[i + 1][j + 1]
                        neighbours += board[i + 1][j]
                    elif (i > 0 and i < m - 1) and j == n - 1:
                        neighbours += board[i - 1][j]
                        neighbours += board[i - 1][j - 1]
                        neighbours += board[i][j - 1]
                        neighbours += board[i + 1][j - 1]
                        neighbours += board[i + 1][j]
                    if neighbours == 3:
                        board[i][j] = 10
                elif board[i][j] == 1:
                    if i == 0 and j == 0:
                        neighbours += board[i + 1][j]
                        neighbours += board[i][j + 1]
                        neighbours += board[i + 1][j + 1]
                    elif i == 0 and j == n - 1:
                        neighbours += board[i + 1][j]
                        neighbours += board[i][j - 1]
                        neighbours += board[i + 1][j - 1]
                    elif i == m - 1 and j == 0:
                        neighbours += board[i - 1][j]
                        neighbours += board[i][j + 1]
                        neighbours += board[i - 1][j + 1]
                    elif i == m - 1 and j == n - 1:
                        neighbours += board[i - 1][j]
                        neighbours += board[i][j - 1]
                        neighbours += board[i - 1][j - 1]
                    elif i == 0 and (j > 0 and j < n - 1):
                        neighbours += board[i][j - 1]
                        neighbours += board[i + 1][j - 1]
                        neighbours += board[i + 1][j]
                        neighbours += board[i + 1][j + 1]
                        neighbours += board[i][j + 1]
                    elif i == m - 1 and (j > 0 and j < n - 1):
                        neighbours += board[i][j - 1]
                        neighbours += board[i - 1][j - 1]
                        neighbours += board[i - 1][j]
                        neighbours += board[i - 1][j + 1]
                        neighbours += board[i][j + 1]
                    elif (i > 0 and i < m - 1) and j == 0:
                        neighbours += board[i - 1][j]
                        neighbours += board[i - 1][j + 1]
                        neighbours += board[i][j + 1]
                        neighbours += board[i + 1][j + 1]
                        neighbours += board[i + 1][j]
                    elif (i > 0 and i < m - 1) and j == n - 1:
                        neighbours += board[i - 1][j]
                        neighbours += board[i - 1][j - 1]
                        neighbours += board[i][j - 1]
                        neighbours += board[i + 1][j - 1]
                        neighbours += board[i + 1][j]
                    board[i][j] = neighbours
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] >= 2 and board[i][j] <= 3:
                    board[i][j] = 1
                elif board[i][j] > 3 and board[i][j] < 10:
                    board[i][j] = 0
                elif board[i][j] == 10:
                    board[i][j] = 1
        return
        
