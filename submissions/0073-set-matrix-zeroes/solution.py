class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        matrix[k][j] = "a" if matrix[k][j] != 0 else 0
                    for k in range(len(matrix[0])):
                        matrix[i][k] = "a" if matrix[i][k] != 0 else 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "a":
                    matrix[i][j] = 0

        
