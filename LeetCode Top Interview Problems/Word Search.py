visited = []
found = False

class Solution:
    def dfs(self, board: List[List[str]], row: int, col: int, cursor: int, tam: int, word: str, m: int, n: int) -> None:
        global found
        if cursor == tam - 1:
            found = True
            return
        global visited
        visited[row][col] = 1
        dx = [1,-1,0, 0]
        dy = [0, 0,1,-1]
        for i in range(0, 4):
            nrow = row + dx[i]
            ncol = col + dy[i]
            if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and visited[nrow][ncol] == 0 and board[nrow][ncol] == word[cursor + 1]:
                print("nrow:", nrow," ncol:", ncol)
                self.dfs(board, nrow, ncol, cursor + 1, tam, word, m, n)
                if found == True:
                    return
        visited[row][col] = 0
        return
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        # First, we must treat the corner cases first...
        if len(board) == 0:
            return False
        if len(board[0]) == 0:
            return False
        if len(word) == 0:
            return False
        # Now, we solve the problem for the general case...
        m = len(board)
        n = len(board[0])
        cursor = 0
        tam = len(word)
        global visited
        visited = [[0 for i in range(0, n)] for j in range(0, m)] 
        global found 
        found = False
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0]:
                    self.dfs(board, i, j, cursor, tam, word, m, n)
                    if found == True:
                        return found
        return found
                
                
