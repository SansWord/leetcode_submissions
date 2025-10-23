class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.visited = [ [False] * self.COLS for i in range(self.ROWS) ]
        self.secondVisited = [ [False] * self.COLS for i in range(self.ROWS) ]
        self.grid = grid
        
        if self.isDisconnected(self.visited):
            return 0

        # test if remove a point would make this island disconnected on all points of this island
        for vi in range(self.ROWS):
            for vj in range(self.COLS):
                if self.visited[vi][vj]:
                    self.grid[vi][vj] = 0
                    # test if we have more than one island here
                    # if yes, return 1
                    if self.isDisconnected(self.secondVisited):
                        return 1
                    self.grid[vi][vj] = 1
                    for i in range(self.ROWS):
                        for j in range(self.COLS):
                            self.secondVisited[i][j] = False

        # since remove 1 cell won't make island being disconnected, the answer is 2
        return 2

    def isDisconnected(self, visited:list[list[bool]]) -> bool:

        foundFirstIsland = False
        for i in range(self.ROWS):
            for j in range(self.COLS):
                cell = self.grid[i][j]
                if cell == 1 and not visited[i][j]:
                    if not foundFirstIsland:
                        self.visit(i, j, visited)
                        foundFirstIsland = True
                    else:
                        return True

        # there's no island at all, already disconnected
        if not foundFirstIsland:
            return True

        return False
    
    def visit(self, row: int, col: int, visited:list[list[bool]]):
        if not self.isValidPoint(row, col) or self.grid[row][col] == 0:
            return
        
        if visited[row][col]:
            return

        visited[row][col] = True

        self.visit(row, col+1, visited)
        self.visit(row, col-1, visited)
        self.visit(row+1, col, visited)
        self.visit(row-1, col, visited)

        return
    
    def isValidPoint(self, row: int, col: int) -> bool:
        return row >= 0 and col >= 0 and row < self.ROWS and col < self.COLS
