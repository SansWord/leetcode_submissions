class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2 ** 31 -1
        INT_MIN = -2 ** 31
        if divisor == 1:
            return dividend
        if divisor == -1:
            return min(max(-dividend, INT_MIN), INT_MAX)

        isPositive = True
        if dividend < 0:
            dividend = -dividend
            isPositive = not isPositive
        
        if divisor < 0:
            divisor = -divisor
            isPositive = not isPositive
        
        res = 0
        while dividend >= divisor:
            q = 1
            mul = divisor
            while dividend >= (mul << 1):
                mul <<= 1
                q <<= 1

            dividend -= mul
            res += q

        return min(res, INT_MAX) if isPositive else max(-res, INT_MIN)
        
        
