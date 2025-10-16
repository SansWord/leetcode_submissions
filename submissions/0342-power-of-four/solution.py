class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        possible = { 1, 4, 6} 
        return n > 0 and (n & (n-1) == 0) and n % 10 in possible

        
