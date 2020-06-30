visited = []
ggrid = []

def floodfill(x: int, y: int, m: int, n: int) -> None:
    global visited
    visited[x][y] = 1
    dx = [1,-1, 0, 0]
    dy = [0, 0, 1,-1]
    for i in range(0, 4):
        newx = x + dx[i]
        newy = y + dy[i]
        global ggrid
        if newx >= 0 and newx < m and newy >= 0 and newy < n and ggrid[newx][newy] == "1" and visited[newx][newy] == 0:
            floodfill(newx, newy, m, n)
    return

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Treating the corner cases first:
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0
        # Treating the general cases now...
        answer = 0
        global ggrid
        ggrid = grid
        global visited
        visited = [[0 for i in range(0, len(grid[0]))] for j in range(0, len(grid))]
        print(ggrid)
        print(visited)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if ggrid[i][j] == "1" and visited[i][j] == 0:
                    answer += 1
                    floodfill(i, j, len(grid), len(grid[0]))
        return answer
