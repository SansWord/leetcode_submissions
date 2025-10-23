class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.COL = len(grid)
        self.ROW = len(grid[0])
        self.visited = [ [False]* self.ROW for i in range(self.COL) ]
        self.grid = grid

        res = 0
        for i in range(self.COL):
            for j in range(self.ROW):
                cell = grid[i][j]
                if cell == "1" and not self.visited[i][j]:
                    self.visitIsland(i, j)
                    res += 1

        return res
    
    def visitIsland(self, y: int, x: int):
        if not self.isValidPoint(y, x) or self.visited[y][x] or self.grid[y][x] == "0":
            return

        self.visited[y][x] = True
        self.visitIsland(y, x+1)
        self.visitIsland(y, x-1)
        self.visitIsland(y+1, x)
        self.visitIsland(y-1, x)

    def isValidPoint(self, y: int, x: int) -> bool:
        return x >= 0 and x < self.ROW and y >= 0 and y < self.COL
        
