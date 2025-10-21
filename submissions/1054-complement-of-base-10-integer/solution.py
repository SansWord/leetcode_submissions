class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        digits = []
        while n > 0:
            digits.append(n % 2)
            n //= 2

        res = 0
        for d in digits[::-1]:
            res *= 2
            res += 0 if d == 1 else 1
        
        return res
        
