class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        digit = None
        while n != 0:
            curr = n % 2
            if digit == curr:
                return False
            digit = curr
            n //= 2
        
        return True
        
