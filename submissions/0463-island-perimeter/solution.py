class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.COL = len(grid)
        self.ROW = len(grid[0])
        self.visited = [ [False for i in range(self.ROW)] for j in range(self.COL) ]
        self.grid = grid

        for i in range(self.COL):
            for j in range(self.ROW):
                cell = grid[i][j]
                if cell == 1:
                    # found first island piece
                    return self.calculatePerimeter(i,j)

    def calculatePerimeter(self, y:int, x:int) -> int:
        if not self.isValidPoint(y, x) or self.grid[y][x] == 0:
            return 1

        if self.visited[y][x]:
            return 0

        # step onto an island
        self.visited[y][x] = True

        res =  self.calculatePerimeter(y, x+1)
        res += self.calculatePerimeter(y, x-1)
        res += self.calculatePerimeter(y+1, x)
        res += self.calculatePerimeter(y-1, x)
        
        return res
    
    def isValidPoint(self, y: int, x: int):
        return y >=0 and x >=0 and y < self.COL and x < self.ROW


        
        
