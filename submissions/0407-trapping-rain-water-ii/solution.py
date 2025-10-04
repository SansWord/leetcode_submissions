import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0

        ROW_WIDTH = len(heightMap)
        COL_WIDTH = len(heightMap[0])

        sum = 0
        maxHeight = 0
        heap = []

        for i in [0, ROW_WIDTH-1]:
            for j in range(COL_WIDTH):
                heapq.heappush(heap, (heightMap[i][j], i, j))
                heightMap[i][j] = -1
        
        for i in range(1, ROW_WIDTH-1):
            for j in [0, COL_WIDTH-1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                heightMap[i][j] = -1
        
        while len(heap):
            smallest_node = heapq.heappop(heap)
            
            h = smallest_node[0]
            x = smallest_node[1]
            y = smallest_node[2]

            if maxHeight > h:
                sum += maxHeight - h
            else:
                maxHeight = h
            
            dirs = [0,1,0,-1,0]
            for k in range(4):
                deltaX = dirs[k]
                deltaY = dirs[k+1]

                i = x + deltaX
                j = y + deltaY
                if (i >= 0 and i < ROW_WIDTH
                    and j >= 0 and j < COL_WIDTH
                    and heightMap[i][j] != -1):

                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

        return sum
