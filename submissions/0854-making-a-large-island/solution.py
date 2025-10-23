class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.grid = grid
        self.visited = [ [False]* self.COLS for i in range(self.ROWS) ]


        # find all islands and label them from 1 to n
        label = 1
        areas = {}
        totalShores = set()
        maxArea = 0
        for i in range(self.ROWS):
            for j in range(self.COLS):
                cell = grid[i][j]
                if cell == 1 and not self.visited[i][j]:
                    area = self.visitIsland(i, j, label, totalShores)
                    areas[label] = area
                    maxArea = max(maxArea, area)
                    label += 1

        if maxArea == 0:
            # there's no island, flip any cell and have 1 area
            return 1

        if maxArea == self.ROWS * self.COLS:
            # every cell are island, return its area
            return maxArea

        for shore in totalShores:
            area = self.connectNearbyIsland(shore[0], shore[1], areas)
            maxArea = max(maxArea, area)
        return maxArea
    
    def visitIsland(self, y: int, x: int, label: int, shores: set[tuple[int, int]]) -> int:
        if not self.isValidPoint(y, x) or self.visited[y][x]:
            return 0
        if self.grid[y][x] == 0:
            shores.add((y,x))
            return 0


        self.visited[y][x] = True
        self.grid[y][x] = label
        area = self.visitIsland(y, x+1, label, shores)
        area += self.visitIsland(y, x-1, label, shores)
        area += self.visitIsland(y+1, x, label, shores)
        area += self.visitIsland(y-1, x, label, shores)
        
        return area + 1

    def connectNearbyIsland(self, y: int, x: int, areas: dict[int, int]) -> None:        
        nearbyCellsIdx = [
            [y, x+1],
            [y, x-1],
            [y+1, x],
            [y-1, x]
        ]
        foundIslands = set()
        for cellIdx in nearbyCellsIdx:
            nearbyY, nearbyX = cellIdx
            if self.isValidPoint(nearbyY, nearbyX):
                cell = self.grid[nearbyY][nearbyX]
                if cell != 0:
                    foundIslands.add(cell)
        area = 1
        for islandLabel in foundIslands:
            area += areas[islandLabel]
        return area

    def isValidPoint(self, y: int, x: int) -> bool:
        return x >= 0 and x < self.COLS and y >= 0 and y < self.ROWS
