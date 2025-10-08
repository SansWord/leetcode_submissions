class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        isNegative = x < 0
        x = abs(x)

        while x > 0:
            digit = x % 10
            x //= 10
            result *= 10
            result += digit

        if isNegative:
            result *= -1

        if result > 2**31 -1 or result < -2**31:
            return 0
        
        return result
