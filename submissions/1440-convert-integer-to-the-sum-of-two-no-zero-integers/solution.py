class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            a = i
            b = n - a
            if "0" not in str(a) + str(b):
                return [a,b]
