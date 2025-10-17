class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        hi = 1
        lo = 0
        while hi*hi < num:
            lo = hi
            hi *= 2
        
        # search from lo to hi (exclusive)
        while lo < hi:
            mid = (lo + hi) // 2
            if mid*mid < num:
                lo = mid +1
            else:
                hi = mid
        
            
        return lo * lo == num
        
