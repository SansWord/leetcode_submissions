class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # MAX = 3**floor(log(2**31-1) / log(3))
        # MAX = 3**19, the biggest number of power of 3 that is less than 2**31-1
        MAX = 1162261467
        return MAX % n == 0
        
