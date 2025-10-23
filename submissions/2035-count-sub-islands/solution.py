class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.ROWS = len(grid1)
        self.COLS = len(grid1[0])
        self.visited = [ [False]* self.COLS for i in range(self.ROWS) ]
        self.grid1 = grid1
        self.grid2 = grid2

        subIsland = 0
        islandCount = 0
        for i in range(self.ROWS):
            for j in range(self.COLS):
                cell = grid2[i][j]
                if cell == 1 and not self.visited[i][j]:
                    islandCount += 1
                    if (self.visitIsland(i, j)):
                        subIsland += 1
        return subIsland
    
    def visitIsland(self, y: int, x: int):
        if not self.isValidPoint(y, x) or self.grid2[y][x] == 0 or self.visited[y][x]:
            return True


        self.visited[y][x] = True
        res1 = self.visitIsland(y, x+1)
        res2 = self.visitIsland(y, x-1)
        res3 = self.visitIsland(y+1, x)
        res4 = self.visitIsland(y-1, x)
        if self.grid1[y][x] == 0:
            return False
        else:
            return res1 and res2 and res3 and res4

    def isValidPoint(self, y: int, x: int) -> bool:
        return x >= 0 and x < self.COLS and y >= 0 and y < self.ROWS
