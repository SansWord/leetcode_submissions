class Solution:
    def findComplement(self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 2)
            num //= 2

        res = 0
        for d in digits[::-1]:
            res *= 2
            res += 0 if d == 1 else 1
        
        return res
        
