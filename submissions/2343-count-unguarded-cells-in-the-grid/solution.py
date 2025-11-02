class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        totalUnguarded = [m * n]
        world = [ [-1]*n for i in range(m) ]

        STATE_UNSCANNED = -1
        STATE_R_SCANNED = 1
        STATE_C_SCANNED = 2
        STATE_BOTH_SCANNED = 3
        STATE_WALL = 4
        
        TYPE_ROW = 1
        TYPE_COL = 2

        DIR_LEFT = (-1, 0)
        DIR_RIGHT = (1, 0)
        DIR_UP = (0, 1)
        DIR_DOWN = (0, -1)

        def putGuard(row:int, col:int):
            state = world[row][col]
            
            if state == STATE_UNSCANNED:
                scanRow(row, col)
                scanCol(row, col)
            elif state == STATE_C_SCANNED:
                scanRow(row, col)
            elif state == STATE_R_SCANNED:
                scanCol(row, col)
            elif state == STATE_C_SCANNED:
                scanRow(row, col)

        def scan(row:int, col:int, scanType:int, nextDirection:tuple[int, int]):
            if row < 0 or row >= m or col < 0 or col >= n:
                return
            
            state = world[row][col]
            '''
                    BOTH_SCANNED = 3
                    WALL = 4
            ===============================
                    UNSCANNED = -1
                    R_SCANNED = 1
                    C_SCANNED = 2
            '''
            if state == STATE_BOTH_SCANNED or state == STATE_WALL or state == scanType:
                return
            
            if state == STATE_UNSCANNED:
                totalUnguarded[0] = totalUnguarded[0] - 1
                world[row][col] = scanType
            else:
                world[row][col] = STATE_BOTH_SCANNED
            
            scan(row+nextDirection[0], col+nextDirection[1], scanType, nextDirection)
        
        def scanRow(row:int, col:int):
            scan(row, col, TYPE_ROW, DIR_RIGHT)
            scan(row-1, col, TYPE_ROW, DIR_LEFT)

        def scanCol(row:int, col:int):
            scan(row, col, TYPE_COL, DIR_UP)
            scan(row, col-1, TYPE_COL, DIR_DOWN)

        for wR, wC in walls:
            world[wR][wC] = STATE_WALL
            totalUnguarded[0] = totalUnguarded[0] - 1
        
        for gR, gC in guards:
            putGuard(gR, gC)

        return totalUnguarded[0]

