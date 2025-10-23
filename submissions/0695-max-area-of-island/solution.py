class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.COL = len(grid)
        self.ROW = len(grid[0])
        self.visited = [ [False]* self.ROW for i in range(self.COL) ]
        self.grid = grid

        maxArea = 0
        for i in range(self.COL):
            for j in range(self.ROW):
                cell = grid[i][j]
                if cell == 1 and not self.visited[i][j]:
                    maxArea = max(maxArea, self.visitIsland(i, j))
                    

        return maxArea
    
    def visitIsland(self, y: int, x: int) -> int:
        if not self.isValidPoint(y, x) or self.visited[y][x] or self.grid[y][x] == 0:
            return 0

        self.visited[y][x] = True
        area = self.visitIsland(y, x+1)
        area += self.visitIsland(y, x-1)
        area += self.visitIsland(y+1, x)
        area += self.visitIsland(y-1, x)
        return area + 1

    def isValidPoint(self, y: int, x: int) -> bool:
        return x >= 0 and x < self.ROW and y >= 0 and y < self.COL
