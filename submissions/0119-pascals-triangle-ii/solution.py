class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]

        result = [1] * (rowIndex+1)

        for i in range(1, rowIndex):
            # C(rowIndex, i)
            result[i] = math.factorial(rowIndex)//math.factorial(i)//math.factorial(rowIndex-i)

        return result
        
