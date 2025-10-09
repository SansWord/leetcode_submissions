class Solution:
    def isHappy(self, n: int) -> bool:
        occurrence = set()
        occurrence.add(n)

        while n != 1:
            n = self.nextNumber(n)
            if n in occurrence:
                return False
            occurrence.add(n)

        return True
    
    def nextNumber(self, n: int) -> int:
        result = 0
        while n > 0:
            result += (n%10)**2
            n //= 10
        
        return result
