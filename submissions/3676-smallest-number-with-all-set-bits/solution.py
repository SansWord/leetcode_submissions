class Solution:
    def smallestNumber(self, n: int) -> int:
        k = 1
        while k < n:
            k = k * 2 + 1
        return k
        
