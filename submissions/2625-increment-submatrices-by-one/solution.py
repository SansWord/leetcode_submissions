class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        difference = [ [0] * (n+1) for i in range(n+1)]

        for row1, col1, row2, col2 in queries:
            difference[row1][col1] += 1
            difference[row1][col2+1] -= 1
            difference[row2+1][col1] -= 1
            difference[row2+1][col2+1] += 1
        
        matrix = [ [0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                top = matrix[i-1][j] if i != 0 else 0
                left = matrix[i][j-1] if j != 0 else 0
                top_left = matrix[i-1][j-1] if (i != 0 and j != 0) else 0
                matrix[i][j] = difference[i][j] + left + top - top_left

        return matrix
        
