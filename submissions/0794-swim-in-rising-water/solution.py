import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # shortest path from [0,0] to [n, n] while the path length is the maximum node of the path
        LENGTH = len(grid)

        queue = []
        curr_flood = grid[0][0]
        heapq.heappush(queue, (curr_flood, 0, 0))

        visited = [ [False for i in range(LENGTH)] for i in range(LENGTH) ]
        visited[0][0] = True
        
        while len(queue) != 0:
            height, x, y = heapq.heappop(queue)
            

            dirs = [1,0,-1,0,1]

            for k in range(4):
                i = x + dirs[k]
                j = y + dirs[k+1]

                if (i >= 0 and j >= 0 
                    and i < LENGTH and j < LENGTH 
                    and (not visited[i][j])):

                    visited[i][j] = True
                    new_height = max(height, grid[i][j])
                    grid[i][j] = new_height
                    heapq.heappush(queue, (new_height, i, j))

        return grid[-1][-1]

