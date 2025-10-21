class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        totalElm = M * N

        # ith elm is at [i // N], [i%N]
        # e.g. 14th for 5x3 is [4][2]

        start = -1
        end = M*N
        while end - start > 1:
            mid = start + (end-start)//2
            i = mid // N
            j = mid % N
            val = matrix[i][j]

            if val <= target:
                start = mid
            else:
                end = mid

        return start != -1 and matrix[start//N][start%N] == target
        
