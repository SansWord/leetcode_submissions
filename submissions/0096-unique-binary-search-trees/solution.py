class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        result = 0
        for i in range(n):
            leftNum = self.numTrees(i)
            rightNum = self.numTrees(n-i-1)
            result += leftNum * rightNum

        return result
        
