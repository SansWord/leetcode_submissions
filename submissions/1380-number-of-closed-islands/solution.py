class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.COL = len(grid)
        self.ROW = len(grid[0])
        self.visited = [ [False]* self.ROW for i in range(self.COL) ]
        self.grid = grid

        res = 0
        for i in range(self.COL):
            for j in range(self.ROW):
                cell = grid[i][j]
                if cell == 0 and not self.visited[i][j]:
                    if (self.visitIsland(i, j)):
                        res += 1

        return res
    
    def visitIsland(self, y: int, x: int) -> bool:
        if not self.isValidPoint(y, x):
            return False
        if self.visited[y][x] or self.grid[y][x] == 1:
            return True
            

        self.visited[y][x] = True
        res1 = self.visitIsland(y, x+1)
        res2 = self.visitIsland(y, x-1)
        res3 = self.visitIsland(y+1, x)
        res4 = self.visitIsland(y-1, x)

        return res1 and res2 and res3 and res4

    def isValidPoint(self, y: int, x: int) -> bool:
        return x >= 0 and x < self.ROW and y >= 0 and y < self.COL
        
