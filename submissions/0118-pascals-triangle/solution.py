class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        result = [
            [1]
        ]

        if numRows == 1:
            return result

        for i in range(1, numRows):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = result[i-1][j] + result[i-1][j-1]
            result.append(row)
        
        return result
        
