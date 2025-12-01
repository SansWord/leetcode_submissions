class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWs = len(board)
        COLs = len(board[0])

        self.ROWs = ROWs
        self.COLs = COLs
        self.board = board
        self.visited = [ [False] * COLs for _ in range(ROWs) ]

        # find potential start
        for row in range(ROWs):
            for col in range(COLs):
                char = board[row][col]
                if not char in word:
                    self.visited[row][col] = False
                else:
                    if char == word[0]:
                        # found first char, start checking
                        if self.findWord(row, col, word):
                            return True
        return False

    def findWord(self, row:int, col:int, word) -> bool:
        if len(word) == 0:
            return True
        if not self.validPoint(row, col):
            return False
        if self.visited[row][col]:
            return False
        
        char = self.board[row][col]
        if word[0] != char:
            return False
        
        self.visited[row][col] = True

        dirs = [
            [1,0],
            [-1,0],
            [0, 1],
            [0, -1]
        ]

        for dir in dirs:
            nextRow = row + dir[0]
            nextCol = col + dir[1]
            found = self.findWord(nextRow, nextCol, word[1:])
            if found:
                return True
        self.visited[row][col] = False
        return False
    
    def validPoint(self, row: int, col: int):
        return row >= 0 and col >= 0 and row < self.ROWs and col < self.COLs



        
