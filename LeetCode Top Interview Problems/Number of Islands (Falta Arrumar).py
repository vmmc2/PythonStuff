visited = []
ggrid = []
answer = 0
dx = [1,-1, 0, 0]
dy = [0, 0, 1,-1]

def preprocess(m: int, n: int) -> None:
    global visited
    visited = [[0 for i in range(0, n)] for j in range(0, m)]
    return

def floodfill(i: int, j: int, m: int, n: int) -> None:
    visited[i][j] = 1 # visitando a celula
    for k in range(0, 4):
        global dx
        global dy
        newi = i + dx[k]
        newj = j + dx[k]
        if(newi >= 0 and newi < m and newj >= 0 and newj < n):
            if(visited[newi][newj] == 0 and ggrid[newi][newj] == '1'):
                floodfill(newi, newj, m, n)
    return

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Treating corner cases first...
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0
        # Treating the general cases now...
        preprocess(len(grid), len(grid[0]))
        global ggrid
        ggrid = grid
        global answer
        answer = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if visited[i][j] == 0:
                    floodfill(i, j, len(grid), len(grid[0]))
                    print(visited)
        return answer
