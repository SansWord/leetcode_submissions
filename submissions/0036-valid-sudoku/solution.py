class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0 for i in range(9)]
        columns = [0 for i in range(9)]
        blocks = [0 for i in range(9)]

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != ".":
                    digit = int(cur)
                    curNum = 2**digit

                    # verify ith row
                    if curNum & rows[i] == 0:
                        rows[i] += curNum
                    else:
                        return False
                    # verify ith column
                    if curNum & columns[j] == 0:
                        columns[j] += curNum
                    else:
                        return False

                    # verify x block
                    x = j // 3 + i //3 * 3
                    if curNum & blocks[x] == 0:
                        blocks[x] += curNum
                    else:
                        return False
            
        return True

        
