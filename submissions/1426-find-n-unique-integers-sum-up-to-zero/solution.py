class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        last = 0
        for i in range(1, n):
            result.append(i)
            last -= i
        result.append(last)
        return result
        
