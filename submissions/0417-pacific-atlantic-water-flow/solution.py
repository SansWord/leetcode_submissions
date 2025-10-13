class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # return all (i,j) s.t. from (i,j) there's a path to [(0,k) or (k,0)] and [(n,0) or (0,n)]

        # for each cell, check if it can reach Pacific Ocean
        # for each cell that can reach Pacific Ocean, check if it can reach Atlantic Ocean
        LEN_X = len(heights)
        LEN_Y = len(heights[0])
        can_reach_pacific = [ [False for j in range(LEN_Y)] for i in range(LEN_X)]
        can_reach_atlantic = [ [False for j in range(LEN_Y)] for i in range(LEN_X)]
        seen = [ [[False, False] for j in range(LEN_Y)] for i in range(LEN_X)]
        pacific_queue = []
        atlantic_queue = []

        for i in range(LEN_X):
            can_reach_pacific[i][0] = True
            seen[i][0][0] = True
            heapq.heappush(pacific_queue, (heights[i][0], i, 0))

            can_reach_atlantic[i][LEN_Y-1] = True
            seen[i][LEN_Y-1][1] = True
            heapq.heappush(atlantic_queue, (heights[i][LEN_Y-1], i, LEN_Y-1))

        for j in range(1, LEN_Y-1):
            # should add[0][LEN_Y-1]
            can_reach_pacific[0][j] = True
            seen[0][j][0] = True
            heapq.heappush(pacific_queue, (heights[0][j], 0, j))

            # should add[LEN_X-1][0]
            can_reach_atlantic[LEN_X-1][j] = True
            seen[LEN_X-1][j][1] = True
            heapq.heappush(atlantic_queue, (heights[LEN_X-1][j], LEN_X-1, j))

        # should add[0][LEN_Y-1]
        can_reach_pacific[0][LEN_Y-1] = True
        seen[0][LEN_Y-1][0] = True
        heapq.heappush(pacific_queue, (heights[0][LEN_Y-1], 0, LEN_Y-1))

        # should add[LEN_X-1][0]
        can_reach_atlantic[LEN_X-1][0] = True
        seen[LEN_X-1][0][1] = True
        heapq.heappush(atlantic_queue, (heights[LEN_X-1][0], LEN_X-1, 0))

        dirs = [1,0,-1,0,1]

        while len(pacific_queue) != 0:
            height, x, y = heapq.heappop(pacific_queue)

            if can_reach_pacific[x][y]:
                for k in range(4):
                    deltaX, deltaY = dirs[k:k+2]
                    i = x + deltaX
                    j = y + deltaY
                    if i >=0 and i < LEN_X and j >=0 and j < LEN_Y and not seen[i][j][0]:
                        seen[i][j][0] = True
                        curr_height = heights[i][j]
                        if height <= curr_height:
                            can_reach_pacific[i][j] = True
                        heapq.heappush(pacific_queue, (curr_height, i, j))




        while len(atlantic_queue) != 0:
            height, x, y = heapq.heappop(atlantic_queue)

            if can_reach_atlantic[x][y]:
                for k in range(4):
                    deltaX, deltaY = dirs[k:k+2]
                    i = x + deltaX
                    j = y + deltaY
                    if i >=0 and i < LEN_X and j >=0 and j < LEN_Y and not seen[i][j][1]:
                        seen[i][j][1] = True
                        curr_height = heights[i][j]
                        if height <= curr_height:
                            can_reach_atlantic[i][j] = True
                        heapq.heappush(atlantic_queue, (curr_height, i, j))

        result = []
        for i in range(LEN_X):
            for j in range(LEN_Y):
                if can_reach_atlantic[i][j] and can_reach_pacific[i][j]:
                    result.append([i,j])

        return result
