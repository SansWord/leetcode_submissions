class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x+1
        n = None

        while lo < hi:
            mid = (lo + hi) // 2
            if mid*mid > x:
                hi = mid
            else:
                n = mid
                lo = mid + 1
            
        return n
        
