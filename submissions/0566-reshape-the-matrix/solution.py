class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        
        result = [ [-1] * c for _ in range(r) ]

        for i in range(m):
            for j in range(n):
                idx = i * n + j
                new_r = idx // c
                new_c = idx % c
                result[new_r][new_c] = mat[i][j]

        return result
        
