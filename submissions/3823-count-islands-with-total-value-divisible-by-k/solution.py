class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.visited = [ [False]*self.COLS for i in range(self.ROWS) ]
        self.k = k
        self.grid = grid

        res = 0
        for i in range(self.ROWS):
            for j in range(self.COLS):
                cell = grid[i][j]
                if cell != 0 and not self.visited[i][j]:
                    if self.visit(i, j) == 0:
                        res += 1
        
        return res
    
    def visit(self, row: int, col: int) -> int:
        if not self.isValidPoint(row, col) or self.visited[row][col] or self.grid[row][col] == 0:
            return 0

        self.visited[row][col] = True
        cell = self.grid[row][col] % self.k
        cell = (cell + self.visit(row, col+1)) % self.k
        cell = (cell + self.visit(row, col-1)) % self.k
        cell = (cell + self.visit(row+1, col)) % self.k
        cell = (cell + self.visit(row-1, col)) % self.k

        return cell
    
    def isValidPoint(self, row:int, col: int) -> bool:
        return row >= 0 and row < self.ROWS and col >= 0 and col < self.COLS
        
